import pytest
from selenium import webdriver
import configuration
from page_objects.wallet_page import WalletPage
from page_objects.header import Header


class Test:
    @pytest.fixture
    def set_up(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(configuration.url)
        yield driver
        driver.quit()

    def test_pytest(self, set_up):
        wallet_page = WalletPage(set_up)
        header = Header(set_up)

        print("assert Title of Luna 1")
        assert wallet_page.is_title_matches(), "Title isn't correct"

        print("Step #1: Click on Open Menu button")
        wallet_page.open_menu()

        print("Step #2: Click on Wallet button in menu")
        wallet_page.click_wallet_section_in_menu()

        print("verify first step page of create new wallet flow")
        assert wallet_page.verify_first_step_of_wallet_creation(), "Missing data on first step of creation wallet flow"

        print("Step #3: Click on Restore Wallet btn on first step")
        wallet_page.click_restore_wallet_btn()

        # print("verify pop-up Restore Wallet window")

        print("Step #4: Input Secret Phrase into field and click Next btn")
        wallet_page.input_recovery_phrase_and_click_next_btn(configuration.recovery_secret_phrase)

        print("Step #6: Set password to encrypt your wallet")
        wallet_page.input_password_and_click_submit_btn(configuration.address_password)

        print("Step #8: Verify home page of wallet")
        assert wallet_page.verify_wallet_main_page(), "Main wallet page is different"

        print("Step #9: Verify correct WalletID")
        assert configuration.address in wallet_page.driver.page_source, "Address of imported wallet is incorrect"

        print("Step # 10: Click on Account menu")
        header.click_account_menu()

        print("Step #11: Click on Lock Wallet btn")
        header.click_lock_wallet_btn_in_account_menu()

        print("Step 12: Verify wallet is locked")
        assert header.verify_lock_wallet_page(), "Unlock btn isn't present on page"


if __name__ == "__main__":
    pytest.main()
