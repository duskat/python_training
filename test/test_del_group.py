__author__ = 'Dzmitry'
from model.group import Group
from random import randrange

def test_delet_some_group(app):
    if app.group.coutn() == 0:
        app.group.create(Group(name="test"))
    odl_groups = app.group.get_group_list()
    index = randrange(len(odl_groups))
    app.group.delet_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(odl_groups)  - 1 == len(new_groups)
    odl_groups[index:index+1] = []
    assert odl_groups == new_groups
