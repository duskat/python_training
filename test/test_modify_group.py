__author__ = 'Dzmitry'
from model.group import Group
from random import randrange

def test_modify_group_name(app, db, check_ui):
    odl_groups = db.get_group_list()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    new_data= Group(name="New Name of Group")
    index = randrange(len(odl_groups))
    new_data.id = odl_groups[index].id
    app.group.modify_group_by_id(new_data.id, new_data)
    new_groups = db.get_group_list()
    assert len(odl_groups) == len(new_groups)
    odl_groups[index] = new_data
    assert sorted(odl_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        list_group_after_mod = app.group.get_group_list()
        assert sorted(list_group_after_mod, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

