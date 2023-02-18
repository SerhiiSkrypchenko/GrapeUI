import pyperclip
from resources.locators import WalletPageLocators, NewWalletPageLocators
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class WalletPage(BasePage):
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """

    """Open Menu"""

    def open_menu(self):
        self.click(WalletPageLocators.menu_btn)

    """Click on Wallet section in MENU"""

    def click_wallet_section_in_menu(self):
        self.click(WalletPageLocators.wallet_menu_btn)

    """Click on Create wallet button during Creating New Wallet flow"""
    def click_create_wallet(self):
        self.click(NewWalletPageLocators.create_wallet_btn)

    def click_restore_wallet_btn(self):
        self.click(NewWalletPageLocators.restore_wallet_btn)

    # Input password in fields and click on Create btn during wallet creation flow
    def input_password_and_click_create_btn(self, password):
        self.enter_text(NewWalletPageLocators.new_password_field, password)
        self.enter_text(NewWalletPageLocators.confirm_password_field, password)
        self.click(NewWalletPageLocators.create_btn)

    # Input secret recovery phrase and click NEXT btn during Recovery wallet proccess STEP #1 (pop-up window)
    def input_recovery_phrase_and_click_next_btn(self, secret_phrase):
        self.enter_text(NewWalletPageLocators.restore_wallet_secret_phrase, secret_phrase)
        self.click(NewWalletPageLocators.restore_wallet_next_btn)

    def input_password_and_click_submit_btn(self, password):
        self.enter_text(NewWalletPageLocators.restore_wallet_password_field, password)
        self.click(NewWalletPageLocators.restore_wallet_submit_btn)

    # Copy Secret Recovery Phrase on Step #3 during creation new wallet
    def copy_secret_recovery_phrase_step_3(self):
        self.click(NewWalletPageLocators.copy_recovery_phrase_btn_step_3)
        list_of_words = pyperclip.paste()
        correct_list_of_words = list_of_words.split()
        return correct_list_of_words

    # Click on NEXT btn on Step #3 during creation new wallet
    def click_next_btn_step_3(self):
        self.click(NewWalletPageLocators.next_btn_step_3)

    def is_title_matches(self):
        """Verifies that the hardcoded text "Luna 1" appears in page title"""

        return "Luna 1" in self.driver.title

    def verify_wallet_main_page(self):
        self.wait_element_located(WalletPageLocators.make_transfer_text)
        assert "Make Transfer" in self.driver.page_source
        assert "Available balance" in self.driver.page_source
        assert "Transaction History" in self.driver.page_source
        return True

    def fill_words_in_correct_order(self, list_of_words):
        for word in list_of_words:
            by_locator = (By.XPATH, "//span[contains(text(),'" + word + "')]")
            self.click(by_locator)

    def verify_first_step_of_wallet_creation(self):
        self.wait_element_located(NewWalletPageLocators.restore_wallet_btn)
        assert ("Create Wallet" in self.driver.page_source)
        assert ("Restore Wallet" in self.driver.page_source)
        assert ("Restore from Secret Recovery Phrase" in self.driver.page_source)
        assert ("Create a new wallet and Secret Recovery Phrase" in self.driver.page_source)
        assert ("New Wallet ?" in self.driver.page_source)
        return True

    def verify_third_step_of_new_wallet_creation(self):
        self.wait_element_located(NewWalletPageLocators.secret_recovery_phrase_text)
        assert ("Secret Recovery Phrase" in self.driver.page_source)
        assert ("Copy" in self.driver.page_source)
        assert ("Next" in self.driver.page_source)
        return True
