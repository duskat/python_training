__author__ = 'Dzmitry'
from model.contact import Group


def test_delet_first_contact(app):
    if app.contact.coutn() == 0:
        app.contact.create(Group(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delet_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts