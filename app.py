import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data(path: str = "olympics_final_final.csv") -> pd.DataFrame:
    df = pd.read_csv(path, index_col=0)
    return df


def main():
    st.set_page_config(page_title="Olympics Explorer", layout="wide")
    st.title("Olympics Performance Explorer")
    st.markdown("Explore the `olympics_final_final.csv` dataset with simple filters and charts.")

    df = load_data()

    # Sidebar filters
    st.sidebar.header("Filters")
    sex_vals = sorted(df['Sex'].dropna().unique())
    selected_sex = st.sidebar.multiselect("Sex (codes)", sex_vals, default=sex_vals)

    min_age = int(np.floor(df['Age'].min())) if pd.notna(df['Age'].min()) else 0
    max_age = int(np.ceil(df['Age'].max())) if pd.notna(df['Age'].max()) else 100
    age_range = st.sidebar.slider("Age range", min_age, max_age, (min_age, max_age))

    medal_vals = sorted(df['Medal_Won'].dropna().unique())
    selected_medals = st.sidebar.multiselect("Medal_Won (codes)", medal_vals, default=medal_vals)

    # For Team, show top 30 codes by frequency to keep the UI usable
    top_teams = df['Team'].value_counts().nlargest(30).index.tolist()
    selected_teams = st.sidebar.multiselect("Team (top 30 codes)", top_teams, default=top_teams[:10])

    # Apply filters
    filtered = df[
        df['Sex'].isin(selected_sex) &
        df['Age'].between(age_range[0], age_range[1]) &
        df['Medal_Won'].isin(selected_medals) &
        df['Team'].isin(selected_teams)
    ]

    st.write(f"Showing {len(filtered):,} rows (filtered from {len(df):,})")

    with st.expander("Data preview (first 200 rows)"):
        st.dataframe(filtered.head(200))

    # Charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Medal counts (filtered)")
        medal_counts = filtered['Medal_Won'].value_counts().sort_index()
        st.bar_chart(medal_counts)

    with col2:
        st.subheader("Age distribution (filtered)")
        fig, ax = plt.subplots()
        sns.histplot(filtered['Age'].dropna(), bins=20, kde=False, ax=ax)
        ax.set_xlabel('Age')
        st.pyplot(fig)

    st.subheader("Height vs Weight (colored by Medal_Won)")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=filtered, x='Height', y='Weight', hue='Medal_Won', palette='tab10', ax=ax, alpha=0.7)
    ax.set_xlabel('Height')
    ax.set_ylabel('Weight')
    st.pyplot(fig)


if __name__ == '__main__':
    main()
