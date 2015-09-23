__author__ = 'Dzmitry'
from model.contact import Contact
import re

def test_info_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    for i in contact_from_home_page:
        clear2(i)
    for a in contact_from_db:
        clear2(a)
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)

def clear(s):
    return re.sub("[() -]", "", s)

def clear2(contact):
    return map(lambda x: clear(x), [contact.firstname, contact.lastname])