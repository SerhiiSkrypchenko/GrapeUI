import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import configuration
from page_objects.page import WalletPage
from page_objects import page
from resources.locators import NewWalletPageLocators


class TestWalletPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(configuration.url)

    def test_create_new_wallet(self):
        wallet_page = page.WalletPage(self.driver)


        # assert Title is correct
        self.assertTrue(wallet_page.is_title_matches(), "Luna 1 title doesn't match.")

        print("Step #1: Click on Open Menu button")
        wallet_page.open_menu()

        print("Step #2: Click on Wallet button in menu")
        wallet_page.click_wallet_section_menu()

        """verify first step page of create new wallet flow"""
        # home_page.verify_wallet_page(home_page)

        print("Step #3: Click on Create wallet button")
        wallet_page.click_create_wallet()

        print("Step #4: Input password into New Password")
        wallet_page.input_password_in_new_password_field(configuration.address_password)

        print("Step #5: Input password into Confirm password field")
        wallet_page.input_password_in_confirm_password_field(configuration.address_password)

        print("Step #6: Click on Create button")
        wallet_page.click_create_btn()
        """
        # verify third step page of create new wallet flow
        # new_wallet_page.verify_third_page(self, driver)

        print("Step #7: Copy recovery phrase into list")
        list_of_words = driver.find_element(By.XPATH, NewWalletPage.secret_recovery_phrase).text.split()

        print("Step #8: Click on NEXT button")
        driver.find_element(By.XPATH, NewWalletPage.next_btn).click()"""

        print("Step #9: Fill words in correct order")
        # NewWalletPage.fill_words_in_correct_order(self, list_of_words, driver)

        print("Step #10: Verify home page of wallet")
        # WalletPage.verify_wallet_page(self, driver)

    """def test_import_wallet(self):
        driver = self.driver

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

        print("Step #9: Verify correct WalletID")
        self.assertTrue(configuration.address in driver.page_source)"""

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
