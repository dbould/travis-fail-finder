from TravisFailFinder import JobService
from TravisFailFinder import LogService

job_service = JobService().create()
repo_id = job_service.get_repo_id('dbould%2Ftravis-fail-finder')
branch_id = job_service.get_branch_id(str(repo_id), 'master')
job_id = job_service.get_job_id(str(branch_id))
log = job_service.get_log(str(job_id))

log_service = LogService()

print(log_service.get_error_feedback(log['content']))
