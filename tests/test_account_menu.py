from time import sleep

import pytest
from qaseio.pytest import qase
from selenium import webdriver
import configuration
from page_objects.wallet_page import WalletPage
from page_objects.header import Header
from webdriver_manager.chrome import ChromeDriverManager


class TestAccountMenu:
    @pytest.fixture
    def set_up(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(configuration.url)


        yield driver

        driver.quit()

    @qase.id(17)
    @qase.title("Lock Wallet")
    @qase.description("Lock wallet")
    def test_lock_wallet(self, set_up):
        wallet_page = WalletPage(set_up)
        header = Header(set_up)

        # assert Title of Luna 1
        assert wallet_page.is_title_matches(), "Title isn't correct"

        # Step #1: Click on Open Menu button
        wallet_page.open_menu()

        # Step #2: Click on Wallet button in menu
        wallet_page.click_wallet_section_in_menu()

        # verify first step page of create new wallet flow
        assert wallet_page.verify_first_step_of_wallet_creation(), "Missing data on first step of creation wallet flow"

        # Step #3: Click on Restore Wallet btn on first step
        wallet_page.click_restore_wallet_btn()

        # print("verify pop-up Restore Wallet window")

        # Step #4: Input Secret Phrase into field and click Next btn
        wallet_page.input_recovery_phrase_and_click_next_btn(configuration.recovery_secret_phrase)

        # Step #5: Set password to encrypt your wallet
        wallet_page.input_password_and_click_submit_btn(configuration.address_password)

        # Step #6: Verify home page of wallet
        assert wallet_page.verify_wallet_main_page(), "Main wallet page is different"

        # Step #7: Verify correct WalletID
        assert configuration.address in wallet_page.driver.page_source, "Address of imported wallet is incorrect"

        # Step # 8: Click on Account menu
        header.click_account_menu()

        # Step #9: Click on Lock Wallet btn
        header.click_lock_wallet_btn_in_account_menu()

        # Step 12: Verify wallet is locked
        assert header.verify_lock_wallet_page(), "Unlock btn isn't present on page"

    @qase.id(18)
    @qase.title("Unlock Wallet")
    @qase.description("Unlock wallet")
    def test_unlock_lock_wallet(self, set_up):
        wallet_page = WalletPage(set_up)
        header = Header(set_up)

        # assert Title of Luna 1
        assert wallet_page.is_title_matches(), "Title isn't correct"

        # Step #1: Click on Open Menu button
        wallet_page.open_menu()

        # Step #2: Click on Wallet button in menu
        wallet_page.click_wallet_section_in_menu()

        # verify first step page of create new wallet flow
        assert wallet_page.verify_first_step_of_wallet_creation(), "Missing data on first step of creation wallet flow"

        # Step #3: Click on Restore Wallet btn on first step
        wallet_page.click_restore_wallet_btn()

        # print("verify pop-up Restore Wallet window")

        # Step #4: Input Secret Phrase into field and click Next btn
        wallet_page.input_recovery_phrase_and_click_next_btn(configuration.recovery_secret_phrase)

        # Step #5: Set password to encrypt your wallet
        wallet_page.input_password_and_click_submit_btn(configuration.address_password)

        # Step #6: Verify home page of wallet
        assert wallet_page.verify_wallet_main_page(), "Main wallet page is different"

        # Step #7: Verify correct WalletID
        assert configuration.address in wallet_page.driver.page_source, "Address of imported wallet is incorrect"

        # Step # 8: Click on Account menu
        header.click_account_menu()

        # Step #9: Click on Lock Wallet btn
        header.click_lock_wallet_btn_in_account_menu()

        # Step 12: Verify wallet is locked
        assert header.verify_lock_wallet_page(), "Unlock btn isn't present on page"

        # Step 13: Unlock wallet with correct password
        header.unlock_wallet(configuration.address_password)

        # Step 14: Verify wallet page
        assert wallet_page.verify_wallet_main_page(), "Main wallet page is different"

        # Step 15: Verify correct WalletID
        assert configuration.address in wallet_page.driver.page_source, "Address of imported wallet is incorrect"

    @qase.id(6)
    @qase.title("Add new account to Wallet")
    @qase.description("Add new account to Wallet")
    def test_add_new_account(self, set_up):
        wallet_page = WalletPage(set_up)
        header = Header(set_up)

        # assert Title of Luna 1
        assert wallet_page.is_title_matches(), "Title isn't correct"

        # Step #1: Click on Open Menu button
        wallet_page.open_menu()

        # Step #2: Click on Wallet button in menu
        wallet_page.click_wallet_section_in_menu()

        # verify first step page of create new wallet flow
        assert wallet_page.verify_first_step_of_wallet_creation(), "Missing data on first step of creation wallet flow"

        # Step #3: Click on Restore Wallet btn on first step
        wallet_page.click_restore_wallet_btn()

        # print("verify pop-up Restore Wallet window")

        # Step #4: Input Secret Phrase into field and click Next btn
        wallet_page.input_recovery_phrase_and_click_next_btn(configuration.recovery_secret_phrase)

        # Step #5: Set password to encrypt your wallet
        wallet_page.input_password_and_click_submit_btn(configuration.address_password)

        # Step #6: Verify home page of wallet
        assert wallet_page.verify_wallet_main_page(), "Main wallet page is different"

        # Step #7: Verify correct WalletID
        assert configuration.address in wallet_page.driver.page_source, "Address of imported wallet is incorrect"

        # Step # 8: Click on Account menu
        header.click_account_menu()

        # Step #9: Click on Add account in account menu
        header.click_add_account_in_account_menu()

        # Step 10: Confirm password
        header.confirm_action(configuration.address_password)

        # Step 11: Verify wallet page of Account 2
        assert header.verify_home_page_account_2, "Account address of Account #2 is INCORRECT"


if __name__ == "__main__":
    pytest.main()
