__author__ = 'Dzmitry'
from model.contact import Contact
from random import randrange

def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="John")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact, index)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


"""def test_modify_contact_lastname(app):
    if app.contact.coutn() == 0:
        app.contact.create(Group(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Group(lastname="Petrov"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)"""