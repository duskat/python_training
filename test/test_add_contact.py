# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts):
    data = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(data)
    assert len(old_contacts) + 1 == app.contact.coutn()
    new_contacts = db.get_contact_list()
    old_contacts.append(data)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)