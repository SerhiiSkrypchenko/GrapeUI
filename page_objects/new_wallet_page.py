from logging import root

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import BaseCase


class NewWalletPage(BaseCase):
    create_wallet_btn = "//span[contains(text(),'Create Wallet')]"
    restore_wallet_btn = "//span[contains(text(),'Restore Wallet')]"
    new_password_field = "//body/div[@id='root']/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    confirm_password_field = "//body/div[@id='root']/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"
    create_btn = "//span[contains(text(),'Create')]"
    secret_recovery_phrase_text = "//div[contains(text(),'Secret Recovery Phrase')]"
    secret_recovery_phrase = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]"
    copy_recovery_phrase_btn = "/html/body/div/div/div[2]/div/div/div[3]/div/button"
    next_btn = "//span[contains(text(),'Next')]"

    def fill_words_in_correct_order(self, list_of_words, driver):
        for x in list_of_words:
            driver.find_element(By.XPATH, "//span[contains(text(),'" + x + "')]").click()


def verify_first_page(self, driver):
    self.assertTrue("Create Wallet" in driver.page_source)
    self.assertTrue("Restore Wallet" in driver.page_source)
    self.assertTrue("Restore from Secret Recovery Phrase" in driver.page_source)
    self.assertTrue("Create a new wallet and Secret Recovery Phrase" in driver.page_source)
    self.assertTrue("New Wallet ?" in driver.page_source)


def verify_third_page(self, driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, NewWalletPage.secret_recovery_phrase_text))
    )
    self.assertTrue("Secret Recovery Phrase" in driver.page_source)
    self.assertTrue("Copy" in driver.page_source)
    self.assertTrue("Next" in driver.page_source)
    # assert (WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, NewWalletPage.copy_recovery_phrase_btn))))
    # assert (WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, NewWalletPage.next_btn))))


