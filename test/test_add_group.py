# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="adjl", header="dhjh", footer="hhjh"))
    app.session.logout()

def test_emp_add_group(app):
    app.group.create(Group(name="", header="", footer=""))
