# -*- coding: utf-8 -*-
from model.group import Group



def test_add_group(app, json_groups):
    group = json_groups
    odl_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(odl_groups) + 1 == app.group.coutn()
    new_groups = app.group.get_group_list()
    odl_groups.append(group)
    assert sorted(odl_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


