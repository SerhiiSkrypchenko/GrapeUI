from qaseio.pytest import qase
from resources.locators import HeaderLocators, CreateRestoreWalletLocators
from page_objects.base_page import BasePage


class Header(BasePage):

    @qase.step("Click on Account Menu btn")
    def click_account_menu(self):
        self.click(HeaderLocators.account_menu_btn)

    @qase.step("Click on LOCK btn in Account Menu btn")
    def click_lock_wallet_btn_in_account_menu(self):
        self.click(HeaderLocators.lock_wallet_btn)

    @qase.step("Verify that wallet is locked")
    def verify_lock_wallet_page(self):
        self.wait_element_located(HeaderLocators.lock_wallet_btn)
        assert "Unlock" in self.driver.page_source
        return True

    @qase.step("Unlock wallet")
    def unlock_wallet(self, password):
        self.enter_text(HeaderLocators.lock_input_field, password)
        self.click(HeaderLocators.unlock_wallet_btn)

    @qase.step("Click on Add account in Account Menu")
    def click_add_account_in_account_menu(self):
        self.click(HeaderLocators.add_account_btn)

    @qase.step("Input password to proceed and click on SUBMIT btn")
    def confirm_action(self, password):
        self.enter_text(HeaderLocators.lock_input_field, password)
        self.click(CreateRestoreWalletLocators.general_submit_btn)

    @qase.step("Verify correct page of address #2 of Wallet")
    def verify_home_page_account_2(self, address):
        self.wait_element_located(HeaderLocators.address_text)
        print(address)
        assert address in self.driver.page_source
        assert "Account 2" in self.driver.page_source
        return True




