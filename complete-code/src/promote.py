import os, yaml, mlflow
from mlflow.tracking import MlflowClient

MODEL = "iris-classifier"
METRIC = "accuracy"

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
client = MlflowClient()
params = yaml.safe_load(open("params.yaml"))
threshold = params["promotion"]["min_accuracy_gain"]

new = client.get_latest_versions(MODEL, ["None"])[-1]
new_acc = client.get_run(new.run_id).data.metrics[METRIC]

prod = client.get_latest_versions(MODEL, ["Production"])

if prod:
    prod_acc = client.get_run(prod[0].run_id).data.metrics[METRIC]
else:
    prod_acc = -1

if new_acc >= prod_acc + threshold:
    print("Promoting to STAGING (Challenger)")
    client.transition_model_version_stage(
        MODEL, new.version, "Staging"
    )
else:
    raise RuntimeError("❌ Accuracy regression")
