from qaseio.pytest import qase
from selenium import webdriver
import configuration
from page_objects.wallet_page import WalletPage
import pytest
from webdriver_manager.chrome import ChromeDriverManager


class TestCreateRestoreWallet:
    @pytest.fixture
    def set_up(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(configuration.url)
        yield driver
        driver.quit()

    @qase.id(2)
    @qase.title("Create New Wallet")
    @qase.description("Create new wallet")
    def test_create_new_wallet(self, set_up):
        wallet_page = WalletPage(set_up)

        # verify Title is correct
        assert wallet_page.is_title_matches(), "Title isn't correct"

        # Step #1: Open MENU"
        wallet_page.open_menu()

        # verify menu sections are present
        assert wallet_page.verify_menu(), "Not all menu sections are present"

        # STep #2: Select Wallet section in Menu
        wallet_page.click_wallet_section_in_menu()

        # verify first step page of create new wallet flow
        assert wallet_page.verify_first_step_of_wallet_creation(), "First Step Page of creating wallet is incorrect"

        # Step #3: Click on Create wallet button
        wallet_page.click_create_wallet()

        # Step #4: Input password, confirm password and click Create btn
        wallet_page.input_password_and_click_create_btn(configuration.address_password)

        # verify third step page of create new wallet flow
        assert wallet_page.verify_third_step_of_new_wallet_creation(), "Required data isn't present on third step of " \
                                                                       "creating new wallet"

        # Step #5: Copy recovery phrase
        list_of_words = wallet_page.copy_secret_recovery_phrase_step_3()

        # Step #6: Click on NEXT button
        wallet_page.click_next_btn_step_3()

        # Step #7: Fill words in correct order
        wallet_page.fill_words_in_correct_order(list_of_words)

        # Verify home page of wallet
        assert wallet_page.verify_wallet_main_page(), "Required Texts on Wallet Page are not present on Wallet Page"

    @qase.id(3)
    @qase.title("Restore Wallet")
    @qase.description("Restore Wallet")
    def test_restore_wallet(self, set_up):
        wallet_page = WalletPage(set_up)

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

        """should be added Verify pop-up Restore Wallet window"""

        # Step #4: Input Secret Phrase into field and click Next btn
        wallet_page.input_recovery_phrase_and_click_next_btn(configuration.recovery_secret_phrase)

        # Step #5: Set password to encrypt your wallet
        wallet_page.input_password_and_click_submit_btn(configuration.address_password)

        # Step #6: Verify home page of wallet
        assert wallet_page.verify_wallet_main_page(), "Main wallet page is different"

        # Step #7: Verify correct WalletID
        assert configuration.address in wallet_page.driver.page_source, "Address of imported wallet is incorrect"


if __name__ == "__main__":
    pytest.main()
