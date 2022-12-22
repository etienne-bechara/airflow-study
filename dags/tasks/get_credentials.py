from airflow.decorators import task

# This should be implemented as a HTTP request to a credentials API, e.g.:
# /credentials?insurer=BRADESCO&status=ACTIVE
#
# Returning data should not contain sensitive information, only the
# credential ids of matching query
#
@task()
def get_credentials(insurer: str):
  return [
    { 'credential_id': 1 },
    { 'credential_id': 2 },
    { 'credential_id': 3 },
    { 'credential_id': 4 },
    { 'credential_id': 5 },
    { 'credential_id': 6 },
    { 'credential_id': 7 },
    { 'credential_id': 8 },
    { 'credential_id': 9 },
    { 'credential_id': 10 },
    { 'credential_id': 11 },
    { 'credential_id': 12 },
    { 'credential_id': 13 },
    { 'credential_id': 14 },
    { 'credential_id': 15 },
    { 'credential_id': 16 },
    { 'credential_id': 17 },
    { 'credential_id': 18 },
    { 'credential_id': 19 },
    { 'credential_id': 20 },
  ]
