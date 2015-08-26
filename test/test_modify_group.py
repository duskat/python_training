__author__ = 'Dzmitry'
from model.group import Group
from random import randrange


def test_modify_group_name(app):
    odl_groups = app.group.get_group_list()
    if app.group.coutn() == 0:
        app.group.create(Group(name="test"))
    group = Group(name="New group")
    index = randrange(len(odl_groups))
    group.id = odl_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(odl_groups) == len(new_groups)
    odl_groups[index] = group
    assert sorted(odl_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""def test_modify_group_header(app):
    odl_groups = app.group.get_group_list()
    if app.group.coutn() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(odl_groups) == len(new_groups)
"""