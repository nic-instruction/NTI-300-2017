#!/usr/bin/python
import os

def setup_install():
    print('installing pip and virtualenv so we can give django its own version of python')
    os.system('yum -y install python-pip && pip install --upgrade pip')
    os.system('pip install virtualenv')
    os.chdir('/opt')
    os.mkdir('/opt/django')
    os.chdir('/opt/django')
    os.system('virtualenv django-env')
    os.system('chown -R nicolebade /opt/django')   # we're useing shell, because the python builtin chown is kind of lame in this case

def django_install():
    print('activating virtualenv and installing django after pre-requirements have been met')
                                                 # You must activate the virtualenv shell every time you perform a command in order for it to work from python.
    os.system('source /opt/django/django-env/bin/activate && pip install django')
                                                 # confirm install and start a django project
    os.chdir('/opt/django')
    os.system('source /opt/django/django-env/bin/activate ' + \
              '&& django-admin --version ' + \
              '&& django-admin startproject project1')

def django_start():
    print('starting django')
    os.system('sudo -u nicolebade  sh -c "source /opt/django/django/bin/activate && python manage.py runserver 0.0.0.0:8000&"') 

setup_install()
django_install()
django_start()
