


import mlflow
import os
import getpass


# AWS_ACCESS_KEY_ID
os.environ["AWS_ACCESS_KEY_ID"] = "*****" # fill in with your AWS profile. More info: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html#setup-credentials
os.environ["AWS_Secret_access_key".upper()] = "*******"


TRACKING_SERVER_HOST = "13.232.178.120" # fill in with the public DNS of the EC2 instance
mlflow.set_tracking_uri(f"http://{TRACKING_SERVER_HOST}:5000")


print(f"tracking URI: '{mlflow.get_tracking_uri()}'")


print(f"default artifacts URI: '{mlflow.get_artifact_uri()}'")

#mlflow.list_experiments()

import boto3



from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

mlflow.set_experiment("experiment_s3_rds_1")

with mlflow.start_run():

    X, y = load_iris(return_X_y=True)

    params = {"C": 0.1, "random_state": 42}
    mlflow.log_params(params)

    lr = LogisticRegression(**params).fit(X, y)
    y_pred = lr.predict(X)
    mlflow.log_metric("accuracy", accuracy_score(y, y_pred))

    mlflow.sklearn.log_model(lr, artifact_path="models")
    print(f"default artifacts URI: '{mlflow.get_artifact_uri()}'")


from mlflow.tracking import MlflowClient


client = MlflowClient(f"http://{TRACKING_SERVER_HOST}:5000")


client.search_registered_models()
for model in models:
    print(model.name)