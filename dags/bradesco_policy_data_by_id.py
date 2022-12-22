from datetime import datetime

from airflow.decorators import dag, task
from airflow.models.param import Param

from tasks.trigger_robot import trigger_robot

@dag(
  description='Download Bradesco specific policy data by its id',
  start_date=datetime(2022, 1, 1),
  schedule_interval=None,
  params={
    'credential_id': Param(0, type='integer'),
    'policy_id': Param(0, type='integer'),
  },
)
def bradesco_policy_data_by_id():

  # Should also pass policy id in a real world scenario
  raw_data = trigger_robot("{{ params.credential_id }}", operation='POLICY_DATA_BY_ID')

dag = bradesco_policy_data_by_id()
