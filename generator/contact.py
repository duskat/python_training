__author__ = 'Dzmitry'
from model.contact import Contact
import random
import string
import os.path
import json
import jsonpickle

def random_data_symbols(prefix, maxlen):
    symbols = string.ascii_letters  + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_data_digits(prefix, maxlen):
    digits = string.digits + ""*5
    return prefix + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname="", lastname="", nickname="", title="", company="")
           ] + [
    Contact(firstname=random_data_symbols("firstname", 20), lastname=random_data_symbols("lastname", 20),
          nickname=random_data_symbols("nickname", 10), company=random_data_symbols("company", 20),
          address=random_data_symbols("address", 50), homephone=random_data_digits("homephone", 12))
        for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contacts.json")

with open(file,mode="w") as f:
    f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent= 2))

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
