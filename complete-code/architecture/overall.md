Developer
  └── Git Push / PR
        ↓
GitHub Actions (Docker-based CI)
  ├── dvc pull (data)
  ├── train model
  ├── log metrics → MLflow![img_1.png](img_1.png)
  ├── register model
  ├── drift check
  └── promotion logic
        ↓
MLflow Tracking + Registry
  ├── Experiments
  ├── Model Versions
  └── Stages (Shadow / Staging / Prod)
        ↓
Deployment Layer
  ├── FastAPI / KServe
  ├── Shadow inference
  ├── Canary routing
  └── Production traffic
