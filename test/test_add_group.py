# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    odl_groups = app.group.get_group_list()
    app.group.create(Group(name="adjl", header="dhjh", footer="hhjh"))
    new_groups = app.group.get_group_list()
    assert len(odl_groups) + 1 == len(new_groups)

def test_emp_add_group(app):
    app.group.create(Group(name="", header="", footer=""))
