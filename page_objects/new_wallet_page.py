from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""buttons"""
create_wallet_btn = "//span[contains(text(),'Create Wallet')]"
restore_wallet_btn = "//span[contains(text(),'Restore Wallet')]"
new_password_field = "//body/div[@id='root']/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
confirm_password_field = "//body/div[@id='root']/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"
create_btn = "//span[contains(text(),'Create')]"


def verify_first_page(self, driver):
    self.assertTrue("Create Wallet" in driver.page_source)
    self.assertTrue("Restore Wallet" in driver.page_source)
    self.assertTrue("Restore from Secret Recovery Phrase" in driver.page_source)
    self.assertTrue("Create a new wallet and Secret Recovery Phrase" in driver.page_source)
    self.assertTrue("New Wallet ?" in driver.page_source)
