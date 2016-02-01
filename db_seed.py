#!flask/bin/python
from app import db, models
from sqlalchemy import MetaData
import time
import names

# Create users
number_of_apartments = 3
number_of_rooms_in_apartment = 2
users_in_room = 2
from random import randint
from random import choice

users = models.User.query.all()
if len(users) == 0:
    for i in range (0, number_of_apartments):
        a = models.Apartment(location='Some location ' + str(i))
        db.session.add(a)
        db.session.commit()
        a = models.Apartment.query.get(i+1)
        for ir in range(0, number_of_rooms_in_apartment):
            r = models.Room(name='Room'+str(ir), apartment_id=a.id,price=200)
            db.session.add(r)
            db.session.commit()
            r = models.Room.query.get((i * number_of_rooms_in_apartment)+ir+1)

            for uir in range(0, users_in_room):
                u = models.User(firstName=names.get_first_name(), lastName=names.get_last_name(), email='email'+str(i)+str(uir)+str(ir)+'@email.com', room_id=r.id)
                db.session.add(u)
            db.session.commit()

apartments = models.Apartment.query.all()
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
    for ai in range(0, len(apartments)):
        apartment = models.Apartment.query.get(ai+1)

        for ri in range (0, 10):
            rc = models.RentCalculation(apartment_id=apartment.id, notes=str(ri+1)+'/2015')
            db.session.add(rc)
            db.session.commit()

            rc = models.RentCalculation.query.get((ai * 10)+ri+1)
            bills = 0

            for i in range(0, len(bill_types)):
                b = models.Bill(bill_type_id=i+1, rent_calculation_id=rc.id, amount=randint(100,300), paid=choice([True, False]))
                db.session.add(b)
                bills += b.amount

            db.session.commit()

            for i in range(0, users_in_room*number_of_rooms_in_apartment):
                u = models.User.query.get((ai * number_of_rooms_in_apartment)+i+1)
                c = models.Charge(bills=bills, rent=u.room.price, paid=choice([True, False]), rent_calculation_id=rc.id, user_id=u.id)
                db.session.add(c)

            db.session.commit()

