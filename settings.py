# -*- coding: utf-8 -*-
import os

# MONGO DB SETTINGS
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'test')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'test')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'test')


# Enable reads (GET) FOR COLLECTIONS
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20




# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.

# Importing modules from subdirectories
from model.tenants import tenants

DOMAIN = {
    'tenants': tenants
}