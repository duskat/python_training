__author__ = 'Dzmitry'


def test_delet_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delet_first_contact()
    app.session.logout()
