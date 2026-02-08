Production Traffic
        ↓
  ┌───────────────┐
  │ Traffic Split │
  └──────┬────────┘
         ↓
 ┌──────────────┐   ┌──────────────┐
 │ Champion     │   │ Challenger   │
 │ (Production) │   │ (Staging)    │
 └──────┬───────┘   └──────┬───────┘
        ↓                  ↓
   MLflow Metrics     MLflow Metrics
        ↓                  ↓
        └──── Comparison & Decision ──► Promote / Reject
