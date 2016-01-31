#!flask/bin/python
from app import db, models
from sqlalchemy import MetaData
import time

# Create users
number_of_rooms = 6
users_in_room = 2
from random import randint
from random import choice

users = models.User.query.all()
if len(users) == 0:

    a = models.Apartment(location='Some location')
    db.session.add(a)
    db.session.commit()
    a = models.Apartment.query.get(1)
    for i in range(0, number_of_rooms):
        r = models.Room(name='Room'+str(i), apartment_id=a.id,price=200)
        db.session.add(r)
        db.session.commit()
        r = models.Room.query.get(i+1)

        for uir in range(0, users_in_room):
            u = models.User(firstName='First' + str(uir)+str(i), lastName='Last'+str(uir)+str(i), email='email'+str(uir)+str(i)+'@email.com', room_id=r.id)
            db.session.add(u)
        db.session.commit()

bill_types = models.BillType.query.all()

if (len(bill_types) == 0):
    bt = models.BillType(name='Prad', chargeable=True, should_calculate=True)
    db.session.add(bt)
    bt = models.BillType(name='Gaz', chargeable=True, should_calculate=True)
    db.session.add(bt)
    bt = models.BillType(name='Woda', chargeable=False, should_calculate=True)
    db.session.add(bt)
    bt = models.BillType(name='Spoldzielnia', chargeable=True, should_calculate=False)
    db.session.add(bt)
    db.session.commit()
    bill_types = models.BillType.query.all()

if models.RentCalculation.query.count() == 0:
    rc = models.RentCalculation(apartment_id=1, notes='Styczen 2015')
    bills = 0

    for i in range(0, len(bill_types)):
        b = models.Bill(bill_type_id=i+1, rent_calculation_id=1, amount=randint(100,300), paid=choice([True, False]))
        db.session.add(b)
        bills += b.amount

    db.session.commit()

    for i in range(0, len(users)):
        u = models.User.query.get(i+1)
        c = models.Charge(bills=bills, rent=u.room.price, paid=choice([True, False]), rent_calculation_id=1)
        db.session.add(c)

    db.session.commit()

