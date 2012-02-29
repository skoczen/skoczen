from fabric.api import *
import os

PROJECT_NAME = "my-new-project"

def run_ve(cmd):
    local("source ~/.virtualenvs/%(project_name)s/bin/activate;cd ~/workingCopy/%(project_name)s/project;%(cmd)s" % {"cmd":cmd, "project_name":PROJECT_NAME})

def deploy():
    run_ve("./manage.py collectstatic --noinput --settings=envs.live")
    run_ve("./manage.py compress --force --settings=envs.live")
    run_ve("./manage.py sync_static --gzip --expires --settings=envs.live")
    deploy_code()

def deploy_code():
    run_ve("git push heroku live:master")
    run_ve("heroku run project/manage.py syncdb")
    run_ve("heroku run project/manage.py migrate")
    run_ve("heroku restart")