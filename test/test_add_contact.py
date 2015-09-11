# -*- coding: utf-8 -*-
from model.contact import Group



def test_add_contact(app, json_contacts):
    data = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(data)
    assert len(old_contacts) + 1 == app.contact.coutn()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(data)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)