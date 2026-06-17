import mlflow

mlflow.set_experiment(
    "Customer Campaign Prediction"
)

with mlflow.start_run():

    mlflow.log_param(
        "model",
        "RandomForest"
    )

    mlflow.log_metric(
        "accuracy",
        85.27
    )

    print(
        "Experiment Logged Successfully"
    )