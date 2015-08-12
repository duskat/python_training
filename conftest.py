__author__ = 'Dzmitry'

import pytest
from fixture.application import Application
from fixture.application_contact import Application2

@pytest.fixture (scope = "session")
def app(request):
    fixture = Application()
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture