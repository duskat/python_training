__author__ = 'Dzmitry'
from model.contact import Group

def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.coutn() == 0:
        app.contact.create(Group(firstname="test"))
    group = Group(firstname="Petya")
    group.id = old_contacts[0].id
    app.contact.modify_first_contact(Group(firstname="Petya"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = group
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)


"""def test_modify_contact_lastname(app):
    if app.contact.coutn() == 0:
        app.contact.create(Group(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Group(lastname="Petrov"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)"""