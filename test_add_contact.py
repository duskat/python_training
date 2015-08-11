# -*- coding: utf-8 -*-
from contact import Group
import pytest
from application_contact import Application2


@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.creat_new_contact(Group(firstname="Petr", lastname="Petrov", nickname="Petya", title="tester", company="Yandex"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.creat_new_contact(Group(firstname="", lastname="", nickname="", title="", company=""))
    app.logout()

def tearDown(self):
    self.app.destroy()
