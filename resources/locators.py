from selenium.webdriver.common.by import By


class HeaderLocators(object):
    # Dashboard elements:
    make_transfer_text = (By.XPATH, "//h2[contains(text(),'Make Transfer')]")
    address_text = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                              "1]/div[1]/div[1]/p[1]")

    # menu elements:
    wallet_menu_btn = (By.XPATH, "//body/div[2]/div[1]/div[2]/div[2]/button[1]/span[1]")
    home_page_menu_btn = (By.XPATH, "//span[contains(text(),'Home page')]")
    smart_contracts_menu_btn = (By.XPATH, "//span[contains(text(),'Smart Contracts')]")
    list_sc_menu_btn = (By.XPATH, "//span[contains(text(),'List')]")
    publish_sc_menu_btn = (By.XPATH, "//span[contains(text(),'Publish')]")
    read_write_sc_menu_btn = (By.XPATH, "//span[contains(text(),'Read/Write')]")
    blockchain_explorer_menu_btn = (By.XPATH, "//span[contains(text(),'Blockchain Explorer')]")
    transactions_by_wallet_menu_btn = (By.XPATH, "//span[contains(text(),'Transactions by Wallet')]")
    connected_nodes_graph_menu_btn = (By.XPATH, "//span[contains(text(),'Connected nodes graph')]")

    # Account menu elements:
    account_menu_btn = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[2]/span[1]")
    add_account_btn = (By.XPATH, "//span[contains(text(),'Add account')]")
    edit_account_btn = (By.XPATH, "//span[contains(text(),'Edit')]")
    import_account_btn = (By.XPATH, "//span[contains(text(),'Import')]")
    export_account_btn = (By.XPATH, "//span[contains(text(),'Export')]")
    lock_wallet_btn = (By.XPATH, "//span[contains(text(),'Lock Wallet')]")
    account_2_name_text = (By.XPATH, "//span[contains(text(),'Account 2')]")

    # lock and unlock wallet elements
    lock_input_field = (By.TAG_NAME, "input")
    unlock_wallet_btn = (By.XPATH, "//span[contains(text(),'Unlock')]")

    # header elements:
    copy_account_address_btn = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/i[1]")
    select_environment_btn = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/button[2]/span[1]")
    menu_btn = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/button[1]/span[1]")


class CreateRestoreWalletLocators(object):
    # Create New wallet elements:
    create_wallet_btn = (By.XPATH, "//span[contains(text(),'Create Wallet')]")
    new_password_input_field = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    confirm_password_input_field = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]")
    # CREATE btn on Step #2 during creation wallet flow
    create_btn = (By.XPATH, "//span[contains(text(),'Create')]")
    # Secret Recovery text during on Step #3
    secret_recovery_phrase_text = (By.XPATH, "//div[contains(text(),'Secret Recovery Phrase')]")
    # Secret Recovery phrase (list of words)
    secret_recovery_phrase = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]")
    # Copy recovery phrase on Step #3
    copy_recovery_phrase_step_3_btn = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div/button")
    # Next btn on Step #3
    next_step_3_btn = (By.XPATH, "//span[contains(text(),'Next')]")

    # Restore Wallet elements:
    restore_wallet_btn = (By.XPATH, "//span[contains(text(),'Restore Wallet')]")
    restore_wallet_secret_phrase_input_field = (By.XPATH, "//input[@id='passphrase']")
    restore_wallet_next_btn = (By.XPATH, "//span[contains(text(),'Next')]")
    restore_wallet_password_input_field = (By.TAG_NAME, "input")
    general_submit_btn = (By.XPATH, "//span[contains(text(),'Submit')]")
