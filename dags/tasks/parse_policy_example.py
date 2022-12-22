import random

from airflow.decorators import task

# An example of response when parsing a policy list into DTOs
#
@task()
def parse_policy_example():
  return [
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
    { 'policy_id': random.randint(1000, 9999) },
  ]
