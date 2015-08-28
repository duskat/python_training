__author__ = 'Dzmitry'
from model.contact import Group

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit new contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.list_contact_cache = None

    def modify_first_contact(self, new_contact_date):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_date):
        wd = self.app.wd
        self.select_contact_by_index(index)
        #click edit contact
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #fill out form
        self.fill_contact_form(new_contact_date)
        #submit update
        wd.find_element_by_xpath(".//*[@id='content']/form[1]/input[1]").click()
        wd.get("http://localhost/addressbook/")
        self.list_contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)

    def change_field_value(self, fild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fild_name).click()
            wd.find_element_by_name(fild_name).clear()
            wd.find_element_by_name(fild_name).send_keys(text)

    def delet_first_contact(self):
        self.delet_contact_by_index(0)

    def delet_contact_by_index(self, index):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        self.select_contact_by_index(index)
        #delet element
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #confirm deletion
        wd.switch_to_alert().accept()
        self.list_contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
         self.select_contact_by_index()

    def coutn(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        return len(wd.find_elements_by_name("selected[]"))

    list_contact_cache = None

    def get_contact_list(self):
        if self.list_contact_cache is None:
            wd = self.app.wd
            wd.get("http://localhost/addressbook/")
            self.list_contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                """cells = element.find_elements_by_tag_name("td")
                text_firstname = cells[1].text
                text_lastname = cells[2].text"""
                id = element.find_element_by_name("selected[]").get_attribute("id")
                text_firstname=element.find_element_by_css_selector('tr[name="entry"] td:nth-of-type(3)').text
                text_lastname= element.find_element_by_css_selector('tr[name="entry"] td:nth-of-type(2)').text
                self.list_contact_cache.append(Group(id=id, lastname=text_lastname, firstname=text_firstname))
        return list(self.list_contact_cache)


