from git import Repo

# repo_url = 'git@github.com:gore-labs/lab_to_automate.git'
repo_path = '/home/dhimes/lab_to_automate/'


def git_create_branch(repo, branch_name):
    origin = repo.remote()
    repo.create_head(branch_name)
    origin.push(branch_name)


repo = Repo(repo_path)

needed_branches = 10

for x in range(1, needed_branches+1):
    branch_name = f'student_{x}_master'
    git_create_branch(repo, branch_name)
