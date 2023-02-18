import unittest
from time import sleep

from selenium import webdriver
import configuration
from page_objects.wallet_page import WalletPage
from page_objects.header import Header


class TestAccountMenu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(configuration.url)

    def test_lock_wallet(self):
        wallet_page = WalletPage(self.driver)

        print("assert Title of Luna 1")
        self.assertTrue(wallet_page.is_title_matches(), "Title isn't correct")

        print("Step #1: Click on Open Menu button")
        wallet_page.open_menu()

        print("Step #2: Click on Wallet button in menu")
        wallet_page.click_wallet_section_in_menu()

        print("verify first step page of create new wallet flow")
        self.assertTrue(wallet_page.verify_first_step_of_wallet_creation(), "Missing data on first step of creation "
                                                                            "wallet flow")

        print("Step #3: Click on Restore Wallet btn on first step")
        wallet_page.click_restore_wallet_btn()

        # print("verify pop-up Restore Wallet window")

        print("Step #4: Input Secret Phrase into field and click Next btn")
        wallet_page.input_recovery_phrase_and_click_next_btn(configuration.recovery_secret_phrase)

        print("Step #6: Set password to encrypt your wallet")
        wallet_page.input_password_and_click_submit_btn(configuration.address_password)

        print("Step #8: Verify home page of wallet")
        self.assertTrue(wallet_page.verify_wallet_main_page(), "Main wallet page is different")

        print("Step #9: Verify correct WalletID")
        self.assertTrue(configuration.address in self.driver.page_source, "Address of imported wallet is incorrect")

        header = Header(self.driver)

        print("Step # 10: Click on Account menu")
        header.click_account_menu()

        print("Step #11: Click on Lock Wallet btn")
        header.click_lock_wallet_btn_in_account_menu()

        print("Step 12: Verify wallet is locked")
        self.assertTrue(header.verify_lock_wallet_page(), "Unlock btn isn't present on page")

    def test_unlock_lock_wallet(self):
        wallet_page = WalletPage(self.driver)
        header = Header(self.driver)

        print("assert Title of Luna 1")
        self.assertTrue(wallet_page.is_title_matches(), "Title isn't correct")

        print("Step #1: Click on Open Menu button")
        wallet_page.open_menu()

        print("Step #2: Click on Wallet button in menu")
        wallet_page.click_wallet_section_in_menu()

        print("verify first step page of create new wallet flow")
        self.assertTrue(wallet_page.verify_first_step_of_wallet_creation(), "Missing data on first step of creation "
                                                                            "wallet flow")

        print("Step #3: Click on Restore Wallet btn on first step")
        wallet_page.click_restore_wallet_btn()

        # print("verify pop-up Restore Wallet window")

        print("Step #4: Input Secret Phrase into field and click Next btn")
        wallet_page.input_recovery_phrase_and_click_next_btn(configuration.recovery_secret_phrase)

        print("Step #6: Set password to encrypt your wallet")
        wallet_page.input_password_and_click_submit_btn(configuration.address_password)

        print("Step #8: Verify home page of wallet")
        self.assertTrue(wallet_page.verify_wallet_main_page(), "Main wallet page is different")

        print("Step #9: Verify correct WalletID")
        self.assertTrue(configuration.address in self.driver.page_source, "Address of imported wallet is incorrect")

        print("Step # 10: Click on Account menu")
        header.click_account_menu()

        print("Step #11: Click on Lock Wallet btn")
        header.click_lock_wallet_btn_in_account_menu()

        print("Step 12: Verify wallet is locked")
        self.assertTrue(header.verify_lock_wallet_page(), "Unlock btn isn't present on page")

        print("Step 13: Unlock wallet with correct password")
        header.unlock_wallet(configuration.address_password)

        print("Step 14: Verify wallet page")
        self.assertTrue(wallet_page.verify_wallet_main_page(), "Main wallet page is different")

        print("Step 15: Verify correct WalletID")
        self.assertTrue(configuration.address in self.driver.page_source, "Address of imported wallet is incorrect")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
