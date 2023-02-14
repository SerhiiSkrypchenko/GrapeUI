from selenium.webdriver.common.by import By


class WalletPageLocators(object):
    menu_btn = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/button[1]/span[1]")
    wallet_menu_btn = (By.XPATH, "//body/div[2]/div[1]/div[2]/div[2]/button[1]/span[1]")
    make_transfer_text = "//h2[contains(text(),'Make Transfer')]"


class NewWalletPageLocators(object):
    create_wallet_btn = (By.XPATH, "//span[contains(text(),'Create Wallet')]")
    restore_wallet_btn = "//span[contains(text(),'Restore Wallet')]"
    new_password_field = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    confirm_password_field = "//body/div[@id='root']/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"
    create_btn = "//span[contains(text(),'Create')]"
    secret_recovery_phrase_text = "//div[contains(text(),'Secret Recovery Phrase')]"
    secret_recovery_phrase = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]"
    copy_recovery_phrase_btn = "/html/body/div/div/div[2]/div/div/div[3]/div/button"
    next_btn = "//span[contains(text(),'Next')]"
    restore_wallet_secret_phrase = "//input[@id='passphrase']"
    restore_wallet_next_btn = "//span[contains(text(),'Next')]"
    restore_wallet_password_field = "input"
    restore_wallet_submit_btn = "//span[contains(text(),'Submit')]"
