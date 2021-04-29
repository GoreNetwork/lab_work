from git import Repo
from pprint import pprint

repo_url = 'git@github.com:gore-labs/lab_to_automate.git'
repo_path = '/home/dhimes/lab_to_automate/'


def git_delete_branch(repo, branch_name):
    origin = repo.remote()
    remote = repo.remote(name=branch_name)
    remote.push(refspec=(':delete_me'))


repo = Repo(repo_path)


remote = repo.remote(name='origin')
branch_attribute = repo.remotes.origin.fetch()
for branch in branch_attribute:
    rm_prefix_origin = branch.name.split('/')
    rm_prefix_origin .remove('origin')
    branch_name = '/'.join(rm_prefix_origin)
    pprint(branch_name)
    branch_name = ":" + branch_name
    if "student" not in branch_name:
        continue
    remote.push(refspec=branch_name)
