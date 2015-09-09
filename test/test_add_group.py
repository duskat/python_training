# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string
from data.add_group import constan as testdata


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    odl_groups = app.group.get_group_list()
    group = Group(name="adjl", header="dhjh", footer="hhjh")
    app.group.create(group)
    assert len(odl_groups) + 1 == app.group.coutn()
    new_groups = app.group.get_group_list()
    odl_groups.append(group)
    assert sorted(odl_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


