__author__ = 'Dzmitry'
from model.contact import Contact

import random

def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    contacts_list = db.get_contact_list()
    contact = random.choice(contacts_list)
    app.contact.select_contact_to_add_to_group(contact.id)
    group_list = db.get_group_list()
    group = random.choice(group_list)
    app.contact.select_group_to_add_contact(group.id)
