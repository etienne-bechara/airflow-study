from datetime import datetime

from airflow.decorators import dag, task
from airflow.models.param import Param

from tasks.trigger_dag import trigger_dag
from tasks.trigger_robot import trigger_robot
from tasks.parse_policy_example import parse_policy_example

@dag(
  description='Download Bradesco policies list of target credential',
  start_date=datetime(2022, 1, 1),
  schedule_interval=None,
  params={
    'credential_id': Param(0, type='integer'),
  },
)
def bradesco_policy_list_by_credential_id():

  raw_data = trigger_robot("{{ params.credential_id }}", operation='POLICY_SUMMARY')
  policy_id_list = parse_policy_example()

  trigger_dag(dag_id='bradesco_policy_data_by_id', confs=policy_id_list)

dag = bradesco_policy_list_by_credential_id()
