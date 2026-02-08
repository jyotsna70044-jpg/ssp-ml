# ssp-ml
# mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri postgresql://DB_USER:DB_PASSWORD@DB_ENDPOINT:5432/DB_NAME --default-artifact-root s3://mlflow-artifacts-pkt
# mlflow server -h 0.0.0.0 -p 5000  --default-artifact-root s3://mlflow-artifacts-pkt
dvc repro


# install dvc 
pip install 'dvc[s3]'
dvc init
dvc remote add -d storage s3://mlflow-artifacts-pkt
git add .dvc .gitignore
git commit -m "init dvc"

# Track data:
dvc add data/raw.csv
git add data/raw.csv.dvc
git commit -m "track raw data"

# Push to remote:
dvc push

# Unified Deployment Strategy
=============================

Train → Validate → Shadow → Champion–Challenger → Canary → Production
            ↑         ↑             ↑                ↑
        Drift check   Live metrics   Approval gate    Auto deploy

MLflow = source of truth
GitHub Actions = orchestrator
FastAPI / KServe = runtime