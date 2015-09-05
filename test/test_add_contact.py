# -*- coding: utf-8 -*-
from model.contact import Group


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    group = Group(lastname="Doe", firstname="John", nickname="Vanya", title="tester", company="Yandex", address="489 Wateer Oal, NY",
                  email="Doe.John@yandex.ru", email2="Doe.John@google.ru", email3="Doe.John@google.com",
                  homephone="+1768387593", mobilephone="(707)5783737", workphone="(898)879-7865",
                  secondaryphone="7086787609")
    app.contact.create(group)
    assert len(old_contacts) + 1 == app.contact.coutn()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(group)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)


"""def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    group = Group(firstname="", lastname="", nickname="", title="", company="")
    app.contact.create(group)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(group)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)"""
