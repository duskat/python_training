__author__ = 'Dzmitry'
from model.group import Group


def test_modify_group_name(app):
    odl_groups = app.group.get_group_list()
    if app.group.coutn() == 0:
        app.group.create(Group(name="test"))
    group = Group(name="New group")
    group.id = odl_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(odl_groups) == len(new_groups)
    odl_groups[0] = group
    assert sorted(odl_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""def test_modify_group_header(app):
    odl_groups = app.group.get_group_list()
    if app.group.coutn() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(odl_groups) == len(new_groups)
"""