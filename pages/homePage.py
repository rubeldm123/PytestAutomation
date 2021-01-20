from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link= "//a[@id='welcome']"
        self.logOut_link = "Logout"

    def click_on_Welcome_btn(self):
        element = wait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, self.welcome_link)))
        element.click()
    def click_on_LogOut_link(self):
        element=wait(self.driver,10).until(
            ec.presence_of_element_located((By.LINK_TEXT, self.logOut_link)))
        element.click()