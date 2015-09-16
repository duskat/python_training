__author__ = 'Dzmitry'
from model.group import Group
import random

def test_delet_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    odl_groups = db.get_group_list()
    group = random.choice(odl_groups)
    app.group.delet_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(odl_groups)  - 1 == len(new_groups)
    odl_groups.remove(group)
    assert odl_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
