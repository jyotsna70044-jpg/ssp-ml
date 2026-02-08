import os
import yaml
import pickle
import mlflow
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment("dvc-mlflow-demo")

params = yaml.safe_load(open("../params.yaml"))

df = pd.read_csv("data/raw.csv")
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

with mlflow.start_run():
    model = LogisticRegression(
        lr=params["train"]["lr"],
        max_iter=params["train"]["max_iter"]
    )
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    mlflow.log_metric("accuracy", acc)
    mlflow.log_params(params["train"])

    os.makedirs("../models", exist_ok=True)
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    mlflow.log_artifact("models/model.pkl")