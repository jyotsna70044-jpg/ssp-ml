Incoming Request
      ↓
FastAPI Gateway
      ↓
+-----------------------------+
| Champion (Production) Model |
+-----------------------------+
      ↓
   Response to User
      ↓
+-----------------------------+
| Shadow Model (Async, Silent)|
+-----------------------------+
      ↓
 MLflow Metrics / Logs
