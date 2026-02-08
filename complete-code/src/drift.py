import yaml, numpy as np, mlflow
from mlflow.tracking import MlflowClient
from scipy.stats import entropy

MODEL = "iris-classifier"
METRIC = "psi"

client = MlflowClient()
params = yaml.safe_load(open("params.yaml"))
max_psi = params["promotion"]["max_psi"]

def psi(p, q):
    return entropy(p, q)

prod = client.get_latest_versions(MODEL, ["Production"])
if not prod:
    print("No production model → skip drift check")
    exit(0)

prod_run = client.get_run(prod[0].run_id)
new = client.get_latest_versions(MODEL, ["None"])[-1]
new_run = client.get_run(new.run_id)

p = np.array(list(prod_run.data.metrics.values()))
q = np.array(list(new_run.data.metrics.values()))

value = psi(p + 1e-6, q + 1e-6)
mlflow.log_metric(METRIC, value)

if value > max_psi:
    raise RuntimeError("❌ Data drift too high")
