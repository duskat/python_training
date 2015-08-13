# -*- coding: utf-8 -*-
from model.contact import Group


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Group(firstname="Petr", lastname="Petrov", nickname="Petya", title="tester", company="Yandex"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Group(firstname="", lastname="", nickname="", title="", company=""))
    app.session.logout()
