# -*- coding: utf-8 -*-
from model.contact import Group
from sys import maxsize


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    group = Group(firstname="Petr", lastname="Petrov", nickname="Petya", title="tester", company="Yandex")
    app.contact.create(group)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(group)
    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize
    assert sorted(old_contacts, key=id_or_max) == sorted(new_contacts, key=id_or_max)


    #def test_add_empty_contact(app):
    #old_contacts = app.contact.get_contact_list()
    #app.contact.create(Group(firstname="", lastname="", nickname="", title="", company=""))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)