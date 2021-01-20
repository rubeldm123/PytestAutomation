import allure
from selenium import webdriver
import pytest
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utils import data
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(data.UserName)
        lp.enter_passowrd(data.PassWord)
        lp.click_on_login()

    def tes_logout(self):
        driver = self.drive
        hp = HomePage(driver)
        hp.click_on_Welcome_btn()
        hp.click_on_LogOut_link()

    def test_login1(self):
        try:
            driver = self.driver
            lp = LoginPage(driver)
            lp.enter_username(data.UserName)
            lp.enter_passowrd(data.PassWord)
            lp.click_on_login()
            x=driver.title
            assert x=="abc"
        except AssertionError as e:
            print("Assertion Error occurred")
            print(e)
            #Screen capture
            currentTime=moment.now().strftime("%d-%m-%y:%H-%M-%S")
            testName=data.whoami()
            screenshotName=testName+"_"+currentTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            raise
        except:
            print("There was an exception")
            raise
        else:
            print("No exception occured")
        finally:
            print("I am inside finally blok")
    def tes_logout1(self):
        driver = self.drive
        hp = HomePage(driver)
        hp.click_on_Welcome_btn()
        hp.click_on_LogOut_link()
