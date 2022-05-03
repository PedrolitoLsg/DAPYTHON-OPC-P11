from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


"""Procedure
First: Land on index page and enter a good email and click on connect
2nd: Lands on the page /showSummary, clicks on book for a specific competition
3rd: enters data in the form
4th: Receives confirmation
5th: Logs out and is returned to the index page
"""


url_root = 'http://127.0.0.1:5000/'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def End2End():
    time.sleep(3)
    driver.get(url_root)
    """ Connecting Via Index"""
    email_form = driver.find_element(By.ID, 'email')
    time.sleep(3)
    email_form.clear()
    time.sleep(3)
    email_form.send_keys("john@simplylift.co")
    time.sleep(3)
    button = driver.find_element(By.ID, "button")
    time.sleep(3)
    button.click()
    time.sleep(3)
    """ Choosing Comp on Show Summary"""
    comp = driver.find_element(By.ID, "bookbutton")
    time.sleep(3)
    comp.click()
    time.sleep(3)
    """On Book enter the number of places"""
    form = driver.find_element(By.ID, "spots")
    form.clear()
    form.send_keys(1)
    time.sleep(3)
    button_book = driver.find_element(By.ID, "submitbutton")
    button_book.click()
    """Gives the confirmation page"""
    assert driver.find_element(By.LINK_TEXT, 'Great-booking complete!')
    return True


End2End()
