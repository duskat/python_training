__author__ = 'Dzmitry'
from model.group import Group

def test_delet_first_group(app):
    if app.group.coutn() == 0:
        app.group.create(Group(name="test"))
    odl_groups = app.group.get_group_list()
    app.group.delet_first_group()
    new_groups = app.group.get_group_list()
    assert len(odl_groups)  - 1 == len(new_groups)
