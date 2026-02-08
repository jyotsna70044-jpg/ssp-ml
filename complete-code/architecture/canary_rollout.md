Client Requests
      ↓
Routing Logic (FastAPI / KServe)
      ↓
 ┌───────────────┬────────────────┐
 │ 90%           │ 10%            │
 │ Production    │ Canary         │
 │ Model         │ Model          │
 └───────────────┴────────────────┘
      ↓                ↓
  KPIs + Errors + Latency (MLflow)
              ↓
        Auto Rollback / Promote

5% → 25% → 50% → 100%
