# -*- coding: utf-8 -*-
from model.contact import Group


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Group(firstname="Petr", lastname="Petrov", nickname="Petya", title="tester", company="Yandex"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Group(firstname="", lastname="", nickname="", title="", company=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)