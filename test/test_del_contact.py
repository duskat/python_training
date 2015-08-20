__author__ = 'Dzmitry'
from model.contact import Group


def test_delet_first_contact(app):
    if app.concatc.coutn() == 0:
        app.concatc.create(Group(firstname="test"))
    app.contact.delet_first_contact()
