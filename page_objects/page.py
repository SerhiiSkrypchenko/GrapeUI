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
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title


class WalletPage(BasePage):
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """

    def open_menu(self):
        self.click(WalletPageLocators.menu_btn)

    def click_wallet_section_menu(self):
        self.click(WalletPageLocators.wallet_menu_btn)

    print("Click on Create wallet button during creating new wallet flow")

    def click_create_wallet(self):
        self.click(NewWalletPageLocators.create_wallet_btn)

    # Input password into New Password field during creating new wallet flow
    def input_password_in_new_password_field(self, password):
        self.enter_text(NewWalletPageLocators.new_password_field, password)

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Luna 1" in self.driver.title
    def verify_wallet_page(self, driver):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, WalletPageLocators.make_transfer_text))
            )
            assert ("Make Transfer" in driver.page_source)
            assert ("Wallet ID" in driver.page_source)
            assert ("Available balance" in driver.page_source)
            assert ("Transaction History" in driver.page_source)
        except:
            capture_path = 'D:/Work/Screenshots from tests/Make transfer money is not present.png'
            driver.save_screenshot(capture_path)
            print("ERROR => Make transfer money is not present !!! See screenshot")

    def fill_words_in_correct_order(self, list_of_words, driver):
        for x in list_of_words:
            driver.find_element(By.XPATH, "//span[contains(text(),'" + x + "')]").click()

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
