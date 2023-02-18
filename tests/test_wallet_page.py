import unittest
from selenium import webdriver
import configuration
from page_objects.wallet_page import WalletPage


class TestWalletPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(configuration.url)

    def test_create_new_wallet(self):
        wallet_page = WalletPage(self.driver)

        print("verify Title is correct")
        self.assertTrue(wallet_page.is_title_matches(), "Luna 1 title doesn't match.")

        print("Step #1: Click on Open Menu button")
        wallet_page.open_menu()

        print("Step #2: Click on Wallet button in menu")
        wallet_page.click_wallet_section_in_menu()

        print("verify first step page of create new wallet flow")
        wallet_page.verify_first_step_of_wallet_creation()

        print("Step #3: Click on Create wallet button")
        wallet_page.click_create_wallet()

        print("Step #4: Input password, confirm password and click Create btn")
        wallet_page.input_password_and_click_create_btn(configuration.address_password)

        print("verify third step page of create new wallet flow")
        self.assertTrue(wallet_page.verify_third_step_of_new_wallet_creation(), "Required data isn't present on third "
                                                                                "step of creating new wallet")

        print("Step #7: Copy recovery phrase into list")
        list_of_words = wallet_page.copy_secret_recovery_phrase_step_3()

        print("Step #8: Click on NEXT button")
        wallet_page.click_next_btn_step_3()

        print("Step #9: Fill words in correct order")
        wallet_page.fill_words_in_correct_order(list_of_words)

        print("Step #10: Verify home page of wallet")
        self.assertTrue(wallet_page.verify_wallet_main_page(), "Required Texts on Wallet Page are not present on "
                                                               "Wallet Page")

    def test_import_wallet(self):
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

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
