# -*- coding: utf-8 -*-
from model.group import Group



def test_add_group(app):
    odl_groups = app.group.get_group_list()
    group = Group(name="adjl", header="dhjh", footer="hhjh")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(odl_groups) + 1 == len(new_groups)
    odl_groups.append(group)
    assert sorted(odl_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_emp_add_group(app):
    odl_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(odl_groups) + 1 == len(new_groups)
    odl_groups.append(group)
    assert sorted(odl_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
