import os, yaml, mlflow, mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment("full-mlops")

params = yaml.safe_load(open("params.yaml"))

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y)

with mlflow.start_run() as run:
    model = LogisticRegression(max_iter=params["train"]["max_iter"])
    model.fit(Xtr, ytr)

    acc = accuracy_score(yte, model.predict(Xte))
    mlflow.log_metric("accuracy", acc)

    mlflow.sklearn.log_model(
        model,
        "model",
        registered_model_name="iris-classifier"
    )

    print("RUN_ID=", run.info.run_id)
    print("ACCURACY=", acc)
