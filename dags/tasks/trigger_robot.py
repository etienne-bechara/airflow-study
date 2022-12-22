from airflow.decorators import task

# This triggers starts a synchronous bot job which returns raw data
# from the scraping procedure, for instance a HTML containing a table
# which lists all policies at target data
#
# There should be more inputs to this task related to scraping params
# like start date, end date, etc
#
@task()
def trigger_robot(credential_id: int, operation: str):
  return '<html>'
