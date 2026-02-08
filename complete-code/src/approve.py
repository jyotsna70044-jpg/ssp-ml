import os, mlflow
from mlflow.tracking import MlflowClient

MODEL = "iris-classifier"

if os.environ.get("APPROVED") != "true":
    raise RuntimeError("Awaiting manual approval")

client = MlflowClient()
staging = client.get_latest_versions(MODEL, ["Staging"])[0]

prod = client.get_latest_versions(MODEL, ["Production"])
if prod:
    client.transition_model_version_stage(
        MODEL, prod[0].version, "Archived"
    )

client.transition_model_version_stage(
    MODEL, staging.version, "Production"
)

print("🚀 Model promoted to Production")
