#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import sys
import os

help_text='''
    == Local Dev Environment ==\n
    Options to use: \n\t{start|stop|init|status|destroy|update|logs}
    Example: \n\t./run.py {project_name} {options}
	'''

if len(sys.argv) <= 1:
    print help_text
    sys.exit(1)

path_stacks='./'
main_stack=sys.argv[1]
option=sys.argv[2]
prefix_project_name='alex_'

config_files='-f ' + path_stacks + main_stack + '.yml '
config_project_name='-p ' + prefix_project_name + ' '


# OPTIONS
if option == 'start':
    os.system('docker-compose ' + config_files + config_project_name + ' start')

elif option == 'stop':
    os.system('docker-compose ' + config_files + config_project_name +  ' stop')

elif option == 'init':
    os.system('docker-compose ' + config_files + config_project_name +  ' up -d')

elif option == 'status':
    os.system('docker-compose ' + config_files + config_project_name +  ' ps')

elif option == 'destroy':
    os.system('docker-compose ' + config_files + config_project_name +  ' stop')
    os.system('docker-compose ' + config_files + config_project_name +  ' rm')

elif option == 'update':
    os.system('docker-compose ' + config_files + config_project_name +  ' stop')
    os.system('docker-compose ' + config_files + config_project_name +  ' build')
    os.system('docker-compose ' + config_files + config_project_name +  ' up -d')

elif option == 'logs':
    os.system('docker-compose ' + config_files + config_project_name +  ' logs')

else:
    print help_text
