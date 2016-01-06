# rent-apartments-manager-restapi

Contributors:
Marek Stabla

Tenants-manager is application for the management of the tenants in the apartment.It allows you to track rent, bills, and other expenses for the residents and the landlord.

This project uses Flask, Flask-REST-ful

### Installation

* Install Python (https://www.python.org/downloads/)
* Install pip (https://pip.pypa.io/en/stable/installing/)
* Install virtual env ```pip install virtualenv```
* Clone repository, and navigate to it
* Create virtual env for project while in root directory ```virtualenv flask```
* Install requirements (```flask/bin/pip install -r requirements.txt``` for OSX/Linux) and ```flask\Scripts\pip install -r requirements``` for Windows)
* Run ```db_creation.py``` to create database, and ```db_upgrade.py``` to upgrade the schema
* Navigate to project root directory and run service using ```run.py```