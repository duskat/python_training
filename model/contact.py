__author__ = 'Dzmitry'
from sys import maxsize

class Group:

    def __init__(self, firstname=None, lastname=None, nickname=None, title=None, company=None, homephone=None, mobilephone=None,
                workphone=None, secondaryphone=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize