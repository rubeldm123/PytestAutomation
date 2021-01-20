from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.Username_txt = "txtUsername"
        self.Password_txt = "txtPassword"
        self.Login_btn = "btnLogin"

    def enter_username(self, usename):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.Username_txt)))
        element.send_keys(usename)

    def enter_passowrd(self, password):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.Password_txt)))
        element.send_keys(password)

    def click_on_login(self):
        element=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.ID, self.Login_btn)))
        element.click()
