import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configuration
from page_objects import home_page
from page_objects import new_wallet_page


class TestHomePage(unittest.TestCase):

    def test_create_new_wallet(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(configuration.url)
        password = "12345678"

        # assert title
        self.assertTrue("Luna 1" in driver.title)

        print("Step #1: Click on Open Menu button")
        driver.find_element(By.XPATH, home_page.open_menu_btn_route).click()

        print("Step #2: Click on Wallet button in menu")
        driver.find_element(By.XPATH, home_page.wallet_menu_btn_route).click()

        # verify first step page of create new wallet page
        new_wallet_page.verify_first_page(self, driver)

        print("Step #3: Click on Create wallet button")
        driver.find_element(By.XPATH, new_wallet_page.create_wallet_btn).click()

        print("Step #4: Input password into New Password")
        driver.find_element(By.XPATH, new_wallet_page.new_password_field).clear()
        driver.find_element(By.XPATH, new_wallet_page.new_password_field).send_keys(password)

        print("Step #5: Input password into Confirm password field")
        driver.find_element(By.XPATH, new_wallet_page.confirm_password_field).clear()
        driver.find_element(By.XPATH, new_wallet_page.confirm_password_field).send_keys(password)

        print("Step #6: Click on Create button")
        driver.find_element(By.XPATH, new_wallet_page.create_btn).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Secret Recovery Phrase')]"))
        )
        self.assertTrue("Secret Recovery Phrase" in driver.page_source)

        recovery_phrase = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]")
        list_of_words = recovery_phrase.text.split()

        next_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        next_btn.click()

        for x in list_of_words:
            word = driver.find_element(By.XPATH, "//span[contains(text(),'" + x + "')]")
            word.click()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Make Transfer')]"))
            )
            self.assertTrue("Make Transfer" in driver.page_source)
            self.assertTrue("Wallet ID" in driver.page_source)
            self.assertTrue("Available balance" in driver.page_source)
            self.assertTrue("Transaction History" in driver.page_source)
        except:
            capture_path = 'D:/Work/Screenshots from tests/Make transfer money is not present.png'
            driver.save_screenshot(capture_path)
            print("ERROR => Make transfer money is not present !!! See screenshot")

        driver.close()
