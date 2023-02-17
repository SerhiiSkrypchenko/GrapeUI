import pyperclip
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from resources.locators import WalletPageLocators, NewWalletPageLocators
from selenium.webdriver.common.by import By


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        """ Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title


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

    # Input password into New Password field during creating new wallet flow
    def input_password_in_new_password_field(self, password):
        self.enter_text(NewWalletPageLocators.new_password_field, password)

    # Input password into Confirm Password field during creating new wallet flow
    def input_password_in_confirm_password_field(self, password):
        self.enter_text(NewWalletPageLocators.confirm_password_field, password)

    """Click on CREATE btn during creating wallet flow on STEP #2 (PASSWORD)"""

    def click_create_btn(self):
        self.click(NewWalletPageLocators.create_btn)

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

    def verify_wallet_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(WalletPageLocators.make_transfer_text))
        try:
            assert "Make Transfer" in self.driver.page_source
            assert "Available balance" in self.driver.page_source
            assert "Transaction History" in self.driver.page_source
            return True
        except:
            return False

    def fill_words_in_correct_order(self, list_of_words):
        for word in list_of_words:
            by_locator = (By.XPATH, "//span[contains(text(),'" + word + "')]")
            self.click(by_locator)

    def verify_first_page(self, driver):
        assert ("Create Wallet" in driver.page_source)
        assert ("Restore Wallet" in driver.page_source)
        assert ("Restore from Secret Recovery Phrase" in driver.page_source)
        assert ("Create a new wallet and Secret Recovery Phrase" in driver.page_source)
        assert ("New Wallet ?" in driver.page_source)

    def verify_third_page(self, driver):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, NewWalletPageLocators.secret_recovery_phrase_text))
        )
        assert ("Secret Recovery Phrase" in driver.page_source)
        assert ("Copy" in driver.page_source)
        assert ("Next" in driver.page_source)
        # assert (WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, NewWalletPage.copy_recovery_phrase_btn))))
        # assert (WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, NewWalletPage.next_btn))))
