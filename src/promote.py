import os
import mlflow
from mlflow.tracking import MlflowClient

MODEL_NAME = "iris-classifier"
METRIC_NAME = "accuracy"
THRESHOLD = 0.0  # set to e.g. 0.01 for +1% improvement

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
client = MlflowClient()

# Latest model version (just registered)
latest_versions = client.get_latest_versions(
    MODEL_NAME, stages=["None"]
)

if not latest_versions:
    raise RuntimeError("No new model version found")

new_model = latest_versions[-1]
new_run = client.get_run(new_model.run_id)
new_acc = new_run.data.metrics[METRIC_NAME]

print("New model accuracy:", new_acc)

# Fetch current Production model
prod_versions = client.get_latest_versions(
    MODEL_NAME, stages=["Production"]
)

if prod_versions:
    prod_model = prod_versions[0]
    prod_run = client.get_run(prod_model.run_id)
    prod_acc = prod_run.data.metrics[METRIC_NAME]
else:
    print("No production model found — auto-promoting first model")
    prod_acc = -1

print("Production accuracy:", prod_acc)

# Promotion decision
if new_acc >= prod_acc + THRESHOLD:
    print("Promoting model to Production 🚀")

    # Archive old production model
    if prod_versions:
        client.transition_model_version_stage(
            name=MODEL_NAME,
            version=prod_model.version,
            stage="Archived"
        )

    client.transition_model_version_stage(
        name=MODEL_NAME,
        version=new_model.version,
        stage="Production"
    )
else:
    print("Model did not meet promotion criteria ❌")
