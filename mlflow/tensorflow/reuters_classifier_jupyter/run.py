import papermill as pm
import mlflow

pm.execute_notebook('reuters_clf.ipynb', 'out_reuters_clf.ipynb')

# #parameters=dict(alpha=0.6, ratio=0.1)

with mlflow.start_run():
    mlflow.log_metric("testkey", 42)
    mlflow.log_artifact("out_reuters_clf.ipynb")
