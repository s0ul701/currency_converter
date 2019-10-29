import os

from fabric.api import *


def makemigrations(app=''):
    local("docker exec -i $(docker ps | grep server | awk '{{ print $1 }}') python manage.py makemigrations {}".format(app))


def migrate(app=''):
    local("docker exec -i $(docker ps | grep server | awk '{{ print $1 }}') python manage.py migrate {}".format(app))


def createsuperuser():
    local("docker exec -it $(docker ps | grep server | awk '{{ print $1 }}') python manage.py createsuperuser")


def kill():
    local("docker kill $(docker ps -q)")
