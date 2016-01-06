# rent-apartments-manager-restapi

Contributors:
Marek Stabla

Tenants-manager is application for the management of the tenants in the apartment.It allows you to track rent, bills, and other expenses for the residents and the landlord.

### Installation

* Install Python (https://www.python.org/downloads/)
* Install pip (https://pip.pypa.io/en/stable/installing/)
* Install virtual env
  * ```pip install virtualenv```
* Clone repository, and navigate to it
* Create virtual env for project while in root directory 
  * ```python -m virtualenv flask```
* Install requirements
  * For OSX/Linux ```flask/bin/pip install -r requirements.txt```
  * For Windows ```flask\Scripts\pip install -r requirements.txt```
* Create database by running creation script and then upgrade the schema
  * For OSX/Linux ```db_creation.py```* and ```db_upgrade.py```*
  * For Windows ```flask\Scripts\python db_creation.py```, ```flask\Scripts\python db_upgrade.py```
* Run service
  * For OSX/Linux ```run.py```*
  * For Windows ```flask\Scripts\python run.py```
  
 
*Indicate that files are executable before you run it, f.e: ```chmod a+x run.py```