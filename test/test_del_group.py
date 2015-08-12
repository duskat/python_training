__author__ = 'Dzmitry'


def test_delet_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delet_first_group()
    app.session.logout()
