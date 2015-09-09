# -*- coding: utf-8 -*-
from model.contact import Group
import pytest
import random
import string

def random_data_symbols(prefix, maxlen):
    symbols = string.ascii_letters  + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_data_digits(prefix, maxlen):
    digits = string.digits + ""*5
    return prefix + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])


testdata = [
     Group(lastname="Doe", firstname="John", nickname="Vanya", title="tester", company="Yandex", address="489 Wateer Oal, NY",
                  email="Doe.John@yandex.ru", email2="Doe.John@google.ru", email3="Doe.John@google.com",
                  homephone="+1768387593", mobilephone="(707)5783737", workphone="(898)879-7865",
                  secondaryphone="7086787609"),
    Group(lastname="Ivanon", firstname="Pert", nickname="Petka", title="tester", company="Google", address="1600 Amphitheatre Parkway,Mountain View, CA 94043",
                  email="Ivanon.Pert@yandex.ru", email2="Ivanon.Pert@google.ru", email3="Ivanon.Pert@google.com",
                  homephone="+1547786737593", mobilephone="(707)47368736", workphone="(898)434-4345",
                  secondaryphone="548782987"),
    Group(firstname="", lastname="", nickname="", title="", company="")
           ] + [
    Group(firstname=random_data_symbols("firstname", 20), lastname=random_data_symbols("lastname", 20),
          nickname=random_data_symbols("nickname", 10), company=random_data_symbols("company", 20),
          address=random_data_symbols("address", 50), homephone=random_data_digits("homephone", 12))
        for i in range(5)
]

@pytest.mark.parametrize("data", testdata, ids=[repr(i) for i in testdata])

def test_add_contact(app, data):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(data)
    assert len(old_contacts) + 1 == app.contact.coutn()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(data)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)