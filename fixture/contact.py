__author__ = 'Dzmitry'
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
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
        #wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        rows = wd.find_elements_by_css_selector("tr[name='entry']")
        row = rows[index]
        row.find_element_by_css_selector("img[alt='Edit']").click()
        #fill out form
        self.fill_contact_form(new_contact_date)
        #submit update
        wd.find_element_by_xpath(".//*[@id='content']/form[1]/input[1]").click()
        wd.find_element_by_link_text("home")
        wd.get("http://localhost/addressbook/")
        self.list_contact_cache = None

    def modify_contact_by_id(self, id, new_contact_date, index):
        wd = self.app.wd
        self.select_contact_by_id(id)
        #click edit contact
        #wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        rows = wd.find_elements_by_css_selector("tr[name='entry']")
        row = rows[index]
        row.find_element_by_css_selector("img[alt='Edit']").click()
        #fill out form
        self.fill_contact_form(new_contact_date)
        #submit update
        wd.find_element_by_xpath(".//*[@id='content']/form[1]/input[1]").click()
        wd.find_element_by_link_text("home")
        wd.get("http://localhost/addressbook/")
        self.list_contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)

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
        self.app.open_home_page()
        self.select_contact_by_index(index)
        #delet element
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #confirm deletion
        wd.switch_to_alert().accept()
        self.list_contact_cache = None

    def delet_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        #delet element
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #confirm deletion
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home")
        self.list_contact_cache = None

    def select_contact_to_add_to_group(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        #select group to add contact
        self.select_group_to_add_contact(id)
        wd.find_element_by_css_selector("input[value='Add to']").click()

    def select_group_to_add_contact(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//div[@class='right']/select//option['%s']" % id).click()


    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_first_contact(self):
         self.select_contact_by_index()

    def coutn(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    list_contact_cache = None

    def get_contact_list(self):
        if self.list_contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.list_contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                text_lastname = cells[1].text
                text_firstname = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                address = cells[3].text
                email = cells[4].text
                all_phones = cells[5].text
                self.list_contact_cache.append(Contact(id=id, lastname=text_lastname, firstname=text_firstname, address=address, email=email,
                                                     all_phones_from_home_page=all_phones))
        return list(self.list_contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_viewt_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                     email=email, email2=email2,  email3=email3,
                     homephone=homephone, mobilephone=mobilephone,
                     workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_viewt_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        #if homephone is not None:
            #homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                     workphone=workphone, secondaryphone=secondaryphone)
