from datetime import datetime
import requests
from airflow.decorators import dag

from tasks.get_credentials import get_credentials
from tasks.trigger_dag import trigger_dag

@dag(
  description ='Download Bradesco policies of all credentials',
  start_date=datetime(2022, 1, 1),
  schedule_interval='@daily',
  catchup=False,
)
def bradesco_policy_all():

  credentials_list = get_credentials(insurer='BRADESCO')
  trigger_dag(dag_id='bradesco_policy_list_by_credential_id', confs=credentials_list)

dag = bradesco_policy_all()
