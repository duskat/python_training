# -*- coding: utf-8 -*-
from model.contact import Group


testdata = [
    Group(lastname="Doe", firstname="John", nickname="Vanya", title="tester", company="Yandex", address="489 Wateer Oal, NY",
                  email="Doe.John@yandex.ru", email2="Doe.John@google.ru", email3="Doe.John@google.com",
                  homephone="+1768387593", mobilephone="(707)5783737", workphone="(898)879-7865",
                  secondaryphone="7086787609"),
    Group(lastname="Ivanon", firstname="Pert", nickname="Petka", title="tester", company="Google", address="1600 Amphitheatre Parkway,Mountain View, CA 94043",
                  email="Ivanon.Pert@yandex.ru", email2="Ivanon.Pert@google.ru", email3="Ivanon.Pert@google.com",
                  homephone="+1547786737593", mobilephone="(707)47368736", workphone="(898)434-4345",
                  secondaryphone="548782987")
]

