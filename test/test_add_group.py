# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def rendom_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Group(name="", header="", footer="")] + [
        Group(name=rendom_string("name", 10), header=rendom_string("header", 20), footer=rendom_string("footer", 20))
        for i in range(5)
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    odl_groups = app.group.get_group_list()
    group = Group(name="adjl", header="dhjh", footer="hhjh")
    app.group.create(group)
    assert len(odl_groups) + 1 == app.group.coutn()
    new_groups = app.group.get_group_list()
    odl_groups.append(group)
    assert sorted(odl_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


