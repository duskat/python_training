__author__ = 'Dzmitry'
from model.contact import Group

def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Group(firstname="Petya"))

def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Group(lastname="Petrov"))