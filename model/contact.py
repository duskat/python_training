__author__ = 'Dzmitry'

class Group:

    def __init__(self, firstname=None, lastname=None, nickname=None, title=None, company=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname,self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname
