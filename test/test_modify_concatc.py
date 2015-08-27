__author__ = 'Dzmitry'
from model.contact import Group

def test_modify_contact_firstname(app):
    if app.contact.coutn() == 0:
        app.contact.create(Group(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Group(firstname="Petya"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_lastname(app):
    if app.contact.coutn() == 0:
        app.contact.create(Group(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Group(lastname="Petrov"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)