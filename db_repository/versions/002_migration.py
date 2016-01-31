from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
bill_types = Table('bill_types', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('chargeable', Boolean),
    Column('should_calculate', Boolean),
)

bills = Table('bills', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('bill_type_id', Integer),
    Column('notes', String(length=64)),
    Column('paid', Boolean),
    Column('rent_calculation_id', Integer),
)

rent_calculations = Table('rent_calculations', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('apartment_id', Integer),
    Column('notes', String(length=64)),
)

charges = Table('charges', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('amount', FLOAT),
    Column('reason', VARCHAR(length=64)),
    Column('paid', BOOLEAN),
    Column('user_id', INTEGER),
)

charges = Table('charges', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('bills', Float),
    Column('rent', Float),
    Column('notes', String(length=64)),
    Column('paid', Boolean),
    Column('user_id', Integer),
    Column('rent_calculation_id', Integer),
)

rooms = Table('rooms', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('apartment_id', Integer),
    Column('price', Float),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['bill_types'].create()
    post_meta.tables['bills'].create()
    post_meta.tables['rent_calculations'].create()
    pre_meta.tables['charges'].columns['amount'].drop()
    pre_meta.tables['charges'].columns['reason'].drop()
    post_meta.tables['charges'].columns['bills'].create()
    post_meta.tables['charges'].columns['notes'].create()
    post_meta.tables['charges'].columns['rent'].create()
    post_meta.tables['charges'].columns['rent_calculation_id'].create()
    post_meta.tables['rooms'].columns['price'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['bill_types'].drop()
    post_meta.tables['bills'].drop()
    post_meta.tables['rent_calculations'].drop()
    pre_meta.tables['charges'].columns['amount'].create()
    pre_meta.tables['charges'].columns['reason'].create()
    post_meta.tables['charges'].columns['bills'].drop()
    post_meta.tables['charges'].columns['notes'].drop()
    post_meta.tables['charges'].columns['rent'].drop()
    post_meta.tables['charges'].columns['rent_calculation_id'].drop()
    post_meta.tables['rooms'].columns['price'].drop()
