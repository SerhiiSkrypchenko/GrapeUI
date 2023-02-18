import pyperclip

import configuration
from resources.locators import HeaderLocators, CreateRestoreWalletLocators
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class Header(BasePage):

    def click_account_menu(self):
        self.click(HeaderLocators.account_menu_btn)

    def click_lock_wallet_btn_in_account_menu(self):
        self.click(HeaderLocators.lock_wallet_btn)

    def verify_lock_wallet_page(self):
        self.wait_element_located(HeaderLocators.lock_wallet_btn)
        assert "Unlock" in self.driver.page_source
        return True

    def unlock_wallet(self, password):
        self.enter_text(HeaderLocators.lock_input_field, password)
        self.click(HeaderLocators.unlock_wallet_btn)


