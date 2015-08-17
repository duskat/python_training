__author__ = 'Dzmitry'
from model.group import Group

def test_delet_first_group(app):
    if app.group.coutn() == 0:
        app.group.create(Group(name="test"))
    app.group.delet_first_group()
