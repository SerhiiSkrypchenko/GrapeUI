import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import configuration
from page_objects import new_wallet_page
from page_objects.new_wallet_page import NewWalletPage
from page_objects.wallet_page import WalletPage


class TestWalletPage(unittest.TestCase):

    def test_create_new_wallet(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(configuration.url)

        # assert title
        self.assertTrue("Luna 1" in driver.title)

        print("Step #1: Click on Open Menu button")
        driver.find_element(By.XPATH, WalletPage.open_menu_btn_route).click()
        #BasePage.click(driver, WalletPage.open_menu_btn)

        print("Step #2: Click on Wallet button in menu")
        driver.find_element(By.XPATH, WalletPage.wallet_menu_btn_route).click()

        # verify first step page of create new wallet flow
        new_wallet_page.verify_first_page(self, driver)

        print("Step #3: Click on Create wallet button")
        driver.find_element(By.XPATH, NewWalletPage.create_wallet_btn).click()

        print("Step #4: Input password into New Password")
        driver.find_element(By.XPATH, NewWalletPage.new_password_field).clear()
        driver.find_element(By.XPATH, NewWalletPage.new_password_field).send_keys(configuration.address_password)

        print("Step #5: Input password into Confirm password field")
        driver.find_element(By.XPATH, NewWalletPage.confirm_password_field).clear()
        driver.find_element(By.XPATH, NewWalletPage.confirm_password_field).send_keys(configuration.address_password)

        print("Step #6: Click on Create button")
        driver.find_element(By.XPATH, NewWalletPage.create_btn).click()

        # verify third step page of create new wallet flow
        new_wallet_page.verify_third_page(self, driver)

        print("Step #7: Copy recovery phrase into list")
        list_of_words = driver.find_element(By.XPATH, NewWalletPage.secret_recovery_phrase).text.split()

        print("Step #8: Click on NEXT button")
        driver.find_element(By.XPATH, NewWalletPage.next_btn).click()

        print("Step #9: Fill words in correct order")
        NewWalletPage.fill_words_in_correct_order(self, list_of_words, driver)

        print("Step #10: Verify home page of wallet")
        WalletPage.verify_wallet_page(self, driver)

        # Closing driver
        driver.close()

    def test_import_wallet(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(configuration.url)

        # assert title
        self.assertTrue("Luna 1" in driver.title)

        print("Step #1: Click on Open Menu button")
        driver.find_element(By.XPATH, WalletPage.open_menu_btn_route).click()

        print("Step #2: Click on Wallet button in menu")
        driver.find_element(By.XPATH, WalletPage.wallet_menu_btn_route).click()

        # verify first step page of create new wallet flow
        new_wallet_page.verify_first_page(self, driver)

        print("Step #3: Click on Restore Wallet btn")
        driver.find_element(By.XPATH, NewWalletPage.restore_wallet_btn).click()

        # verify pop-up Restore Wallet window

        print("Step #4: Input Secret Phrase into field and click Next btn")
        driver.find_element(By.XPATH, NewWalletPage.restore_wallet_secret_phrase).clear()
        driver.find_element(By.XPATH, NewWalletPage.restore_wallet_secret_phrase).send_keys(
            configuration.recovery_secret_phrase)

        print("Step #5: Click Next btn")
        driver.find_element(By.XPATH, NewWalletPage.restore_wallet_next_btn).click()

        print("Step #6: Set password to encrypt your wallet")
        driver.find_element(By.TAG_NAME, NewWalletPage.restore_wallet_password_field).clear()
        driver.find_element(By.TAG_NAME, NewWalletPage.restore_wallet_password_field).send_keys(
            configuration.address_password)

        print("Step #7: Click Submit btn")
        driver.find_element(By.XPATH, NewWalletPage.restore_wallet_submit_btn).click()

        print("Step #8: Verify home page of wallet")
        WalletPage.verify_wallet_page(self, driver)

        # Closing driver
        driver.close()


if __name__ == "__main__":
    unittest.main()
