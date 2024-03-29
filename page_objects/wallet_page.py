import pyperclip
from qaseio.pytest import qase

from resources.locators import HeaderLocators, CreateRestoreWalletLocators
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class WalletPage(BasePage):
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """

    @qase.step("Open Menu")
    def open_menu(self):
        self.click(HeaderLocators.menu_btn)

    @qase.step("Verify menu sections")
    def verify_menu(self):
        self.wait_element_located(HeaderLocators.home_page_menu_btn)
        assert "Home page" in self.driver.page_source
        assert "Smart Contracts" in self.driver.page_source
        assert "Blockchain Explorer" in self.driver.page_source
        assert "Transactions by Wallet" in self.driver.page_source
        assert "Connected nodes graph" in self.driver.page_source
        return True

    @qase.step("Click on Wallet section in Menu")
    def click_wallet_section_in_menu(self):
        self.click(HeaderLocators.wallet_menu_btn)

    @qase.step("Click on Create wallet button during Creating New Wallet flow")
    def click_create_wallet(self):
        self.click(CreateRestoreWalletLocators.create_wallet_btn)

    @qase.step("Click on Restore Wallet button")
    def click_restore_wallet_btn(self):
        self.click(CreateRestoreWalletLocators.restore_wallet_btn)

    @qase.step("Fill password and confirm password fields and click on Create btn during wallet creation flow")
    def input_password_and_click_create_btn(self, password):
        self.enter_text(CreateRestoreWalletLocators.new_password_input_field, password)
        self.enter_text(CreateRestoreWalletLocators.confirm_password_input_field, password)
        self.click(CreateRestoreWalletLocators.create_btn)

    @qase.step("Input secret recovery phrase and click NEXT btn during Recovery wallet process STEP #1 (pop-up window)")
    def input_recovery_phrase_and_click_next_btn(self, secret_phrase):
        self.enter_text(CreateRestoreWalletLocators.restore_wallet_secret_phrase_input_field, secret_phrase)
        self.click(CreateRestoreWalletLocators.restore_wallet_next_btn)

    @qase.step("Input password and click submit btn")
    def input_password_and_click_submit_btn(self, password):
        self.enter_text(CreateRestoreWalletLocators.restore_wallet_password_input_field, password)
        self.click(CreateRestoreWalletLocators.general_submit_btn)

    @qase.step("Copy Secret Recovery Phrase on Step #3 during creation new wallet")
    def copy_secret_recovery_phrase_step_3(self):
        self.click(CreateRestoreWalletLocators.copy_recovery_phrase_step_3_btn)
        list_of_words = pyperclip.paste()
        correct_list_of_words = list_of_words.split()
        return correct_list_of_words

    @qase.step("Click on NEXT btn on Step #3 during creation new wallet")
    def click_next_btn_step_3(self):
        self.click(CreateRestoreWalletLocators.next_step_3_btn)

    @qase.step("Verifies that the hardcoded text Luna 1 appears in page title")
    def is_title_matches(self):
        """Verifies that the hardcoded text "Luna 1" appears in page title"""

        return "Grape Wallet" in self.driver.title

    @qase.step("Verify wallet main page")
    def verify_wallet_main_page(self):
        self.wait_element_located(HeaderLocators.make_transfer_text)
        assert "Make Transfer" in self.driver.page_source
        assert "Available balance" in self.driver.page_source
        assert "Transaction History" in self.driver.page_source
        return True

    @qase.step("Fill words from Recovery Secret Phrase in correct order")
    def fill_words_in_correct_order(self, list_of_words):
        for word in list_of_words:
            by_locator = (By.XPATH, "//span[contains(text(),'" + word + "')]")
            self.click(by_locator)

    @qase.step("Verify Step #1 Page during wallet creation process")
    def verify_first_step_of_wallet_creation(self):
        self.wait_element_located(CreateRestoreWalletLocators.restore_wallet_btn)
        assert ("Create Wallet" in self.driver.page_source)
        assert ("Restore Wallet" in self.driver.page_source)
        assert ("Restore from Secret Recovery Phrase" in self.driver.page_source)
        assert ("Create a new wallet and Secret Recovery Phrase" in self.driver.page_source)
        assert ("New Wallet ?" in self.driver.page_source)
        return True

    @qase.step("Verify Step #3 Page during wallet creation process")
    def verify_third_step_of_new_wallet_creation(self):
        self.wait_element_located(CreateRestoreWalletLocators.secret_recovery_phrase_text)
        assert ("Secret Recovery Phrase" in self.driver.page_source)
        assert ("Copy" in self.driver.page_source)
        assert ("Next" in self.driver.page_source)
        return True
