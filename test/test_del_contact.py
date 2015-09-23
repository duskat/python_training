__author__ = 'Dzmitry'
from model.contact import Contact
import random
import re


def test_delet_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delet_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    for i in old_contacts:
        clear2(i)
    for a in new_contacts:
        clear2(a)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def clear(s):
    return re.sub("[() -]", "", s)

def clear2(contact):
    return map(lambda x: clear(x), [contact.firstname, contact.lastname])