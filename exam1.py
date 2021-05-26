# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class FINALEXAM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            r"C:\Users\theze\OneDrive\Bureau\VSCODE\PerformanceData\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []

    def test_authorized(self):
        driver = self.driver
        driver.get(
            "http://admin:admin@the-internet.herokuapp.com/basic_auth")
        text = driver.find_element_by_class_name('example').text
        print(text)
        driver.save_screenshot("BasicAuth.png")

    def test_anauthorized(self):
        driver = self.driver
        driver.get(
            "https://the-internet.herokuapp.com/basic_auth")
        error = driver.find_element_by_xpath("/html/body").text
        print(error)

        driver.save_screenshot("Error.png")

    def teardown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":

    # unittest.main(defaultTest="FINALEXAM.test_anauthorizeds")
    unittest.main(defaultTest="FINALEXAM.test_authorized")
