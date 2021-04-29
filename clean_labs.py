from functions import *
from creds import *
from pprint import pprint

lab_folder = "~/labs"
git_labs_url = 'https://github.com/gore-labs/lab_to_automate.git'
main_work_folder = git_labs_url.split('/')[-1]
main_work_folder = main_work_folder.split('.')[0]

connection = create_connection()
commands_list = [
    f'cd  {lab_folder}',
    f'cd {main_work_folder}',

]
for command in commands_list:
    print(command)
    output = connection.send_command(command, expect_string='@')

branches = connection.send_command('git branch -a', expect_string='@')
branches = branches.replace(' ', '')
branches = branches.split('\n')
pprint(branches)
for branch in branches:
    if "student" in branch:
        branch = branch.split('/')[-1]
        branch = branch.replace("*", '')
        # rm local branch
        command = f'git checkout main'
        print(connection.send_command(command, expect_string='@'))
        command = f'git branch -d {branch}'
        print(connection.send_command(command, expect_string='@'))
        # rm remote branch
        command = f'git push origin --delete  {branch}'
        print(command)
        print(connection.send_command(command, expect_string="':"))
        print(connection.send_command(github_user, expect_string="':"))
        print(connection.send_command(github_password, expect_string="$ "))
