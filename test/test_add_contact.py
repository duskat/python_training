# -*- coding: utf-8 -*-
from model.contact import Contact
from data.contacts import testdata


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    data = testdata
    for i in data:
        app.contact.create(i)
    assert len(old_contacts) + len(data) == app.contact.coutn()
    new_contacts = app.contact.get_contact_list()
    for n in data:
        old_contacts.append(n)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)