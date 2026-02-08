Model passes automated checks
        ↓
Promotion paused
        ↓
PR Comment:
  /approve-model
        ↓
GitHub Action Listener
        ↓
MLflow Stage Transition
        ↓
Production


CONTROL PLANE
─────────────
GitHub Actions
MLflow Registry
Promotion Logic
Approvals

DATA PLANE
──────────
FastAPI / KServe
Live Traffic
Predictions


Control plane decides
Data plane serves