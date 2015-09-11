# -*- coding: utf-8 -*-
from model.contact import Group
import pytest
from data.add_contact import costant as testdata


@pytest.mark.parametrize("data", testdata, ids=[repr(i) for i in testdata])

def test_add_contact(app, data):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(data)
    assert len(old_contacts) + 1 == app.contact.coutn()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(data)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)