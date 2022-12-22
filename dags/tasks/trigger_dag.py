import requests

from airflow.decorators import task

# Triggers a DAG multiple times with target configurations using Airflow API
# The example uses basic authentication with the airflow:airflow user
#
@task()
def trigger_dag(dag_id: str, confs: list):
  url = f"http://host.docker.internal:8080/api/v1/dags/{dag_id}/dagRuns"
  headers_dict = {'Authorization': 'Basic YWlyZmxvdzphaXJmbG93'}

  for conf in confs:
    json_dict = {'conf': conf}
    response = requests.post(url, json=json_dict, headers=headers_dict)
