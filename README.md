# Olympics Performance Prediction — Streamlit App

This repository contains data and notebooks for Olympics performance analysis. I added a minimal Streamlit app to explore `olympics_final_final.csv` and instructions to deploy on Streamlit Cloud.

Quick start (local):

1. Create and activate a Python environment (PowerShell examples):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

2. To deploy on Streamlit Cloud (recommended):
   - Push this repo to GitHub.
   - Go to https://streamlit.io/cloud and create a new app, connect your GitHub repo and choose the branch and `app.py` as the entrypoint.

Notes:
- The `app.py` loads `olympics_final_final.csv` from the repository root. Keep the CSV in the root or update the path in `app.py`.
- Team and Event columns appear as numeric codes in this dataset — consider joining with `keysToTeam.csv` or `keysToEvent.csv` to display human-readable names.
- Team and Event columns appear as numeric codes in this dataset — consider joining with `keysToTeam.csv` or `keysToEvent.csv` to display human-readable names.

I added container and CI helpers to this repo to help with deployments:

- `Dockerfile` — builds a container that runs the Streamlit app.
- `Procfile` — useful for platforms like Heroku or Render.
- `.github/workflows/docker-publish.yml` — GitHub Actions workflow that builds and pushes a Docker image to Docker Hub on pushes to `main`.

Docker / CI usage notes:

- To build and run locally with Docker:

```powershell
docker build -t olympic_prediction:local .
docker run -p 8501:8501 olympic_prediction:local
```

- To publish via GitHub Actions, add these repository secrets in GitHub:
   - `DOCKERHUB_USERNAME` — your Docker Hub username
   - `DOCKERHUB_TOKEN` — a Docker Hub access token or password

- After secrets are set, pushing to `main` will build and push the image to `DOCKERHUB_USERNAME/olympic_prediction:latest`.

If you'd like, I can also:
- Wire a GitHub Actions deployment step to Render or another host (requires service keys).
- Lookup and join `keysToTeam.csv`/`keysToEvent.csv` so the app shows readable names instead of numeric codes.

