__author__ = 'Dzmitry'
from model.contact import Group
from random import randrange

def test_modify_contact_firstname(app):
    if app.contact.coutn() == 0:
        app.contact.create(Group(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    group = Group(firstname="John")
    group.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, group)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = group
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)


"""def test_modify_contact_lastname(app):
    if app.contact.coutn() == 0:
        app.contact.create(Group(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Group(lastname="Petrov"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)"""