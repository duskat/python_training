__author__ = 'Dzmitry'
from model.contact import Group

def test_modify_contact_firstname(app):
    if app.contact.coutn() == 0:
        app.contact.create(Group(firstname="test"))
    app.contact.modify_first_contact(Group(firstname="Petya"))

def test_modify_contact_lastname(app):
    if app.contact.coutn() == 0:
        app.contact.create(Group(firstname="test"))
    app.contact.modify_first_contact(Group(lastname="Petrov"))