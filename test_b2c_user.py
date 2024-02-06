from seleniumbase import BaseCase
import sys
from faker import Faker
from pathlib import Path
from faker.providers import bank
from faker.providers import automotive
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

## Run "pytest test_b2c_user.py --var1='refap66145@elixirsd.com' --var2='@Bcd1234' --dashboard --html=report_test-server_b2c_user.html --reruns=3"
## this script is to be used with Tenant Exec only
## features tested
## single risk check, bulk risk check, create/delete tenant user, transfer/withdraw credit on tenant user,
## NT on test case name means NOT TESTED(skipped)

class tenant_script(BaseCase):
    def test_single_riskcheck(self):
        SingleRiskCheck.open_homepage(self)
        SingleRiskCheck.login(self)
        
        #self.assert_elements(SingleRiskCheck.halocheck_logo, SingleRiskCheck.home_button, SingleRiskCheck.search_button, SingleRiskCheck.companies_button, SingleRiskCheck.account_button, SingleRiskCheck.logout_button)
        #self.assert_elements(SingleRiskCheck.data_button, SingleRiskCheck.users_button, SingleRiskCheck.settings_button)
        
        #self.click(SingleRiskCheck.search_button)
        #self.click(SingleRiskCheck.single_check)
        self.assert_element(SingleRiskCheck.single_check_title)
        self.sleep(10)
        self.send_keys(SingleRiskCheck.search_bar, "Steve Young")
        #self.click(SingleRiskCheck.category_1)
        #self.click(SingleRiskCheck.category_2)
        #self.click(SingleRiskCheck.category_3)
        #self.click(SingleRiskCheck.category_4)
        #self.click(SingleRiskCheck.category_5)
        self.slow_click(SingleRiskCheck.submit_search_button)
        self.sleep(10)
        #self.assert_elements(SingleRiskCheck.search_results_title, SingleRiskCheck.new_search_button, SingleRiskCheck.high_match_result)
        #self.assert_elements(SingleRiskCheck.number_tab, SingleRiskCheck.match_tab, SingleRiskCheck.country_tab, SingleRiskCheck.category_tab, SingleRiskCheck.subject_tab)
        #self.assert_element(SingleRiskCheck.new_search_button)
        self.click(SingleRiskCheck.download_result_1)
        self.assert_element(SingleRiskCheck.downloaded_notification)
        self.sleep(20)
        # Set the path to the downloaded file
        downloaded_file_path = Path('C:\\Users\\Fadhil\\PycharmProjects\\SeleniumBase\\tests\\HC2\\test-server\\downloaded_files')

        # Use pathlib to find the downloaded file
        for entry in downloaded_file_path.iterdir():
            if entry.is_file():
                file_name = entry.name
                # Perform actions to open the downloaded file using SeleniumBase
                self.open(entry.as_uri())
                self.sleep(5)
                # Add any additional actions you need to perform on the file
                self.assert_pdf_text(pdf=entry.as_uri(),text="Risk Check Report")
                self.assert_pdf_text(pdf=entry.as_uri(),text="Subject Detail")
                self.assert_pdf_text(pdf=entry.as_uri(),text="Name")
                self.assert_pdf_text(pdf=entry.as_uri(),text="ID")
                self.assert_pdf_text(pdf=entry.as_uri(),text="Findings 1 | Official Watchlists")
                self.assert_pdf_text(pdf=entry.as_uri(),text="Disclaimer")
                self.assert_pdf_text(pdf=entry.as_uri(),text="HaloCheck Glossary")
                self.assert_pdf_text(pdf=entry.as_uri(),text="STEVE")
                self.assert_pdf_text(pdf=entry.as_uri(),text="LIU")
    
    def test_bulkcheck(self):
        InternalBulkCheck.open_homepage(self)
        InternalBulkCheck.login(self)
        
        #self.assert_elements(InternalBulkCheck.halocheck_logo, InternalBulkCheck.home_button, InternalBulkCheck.search_button, InternalBulkCheck.companies_button, InternalBulkCheck.account_button, InternalBulkCheck.logout_button)
        #self.assert_elements(InternalBulkCheck.data_button, InternalBulkCheck.users_button, InternalBulkCheck.settings_button)
        
        #self.click(InternalBulkCheck.search_button)
        self.click(InternalBulkCheck.bulk_check_button)
        self.sleep(10)
        #self.assert_element(InternalBulkCheck.bulk_check_title)
        #self.click(InternalBulkCheck.bulk_check_download_template)
        self.click(InternalBulkCheck.bulk_check_settings)
        #file_path = "C://Users//Fadhil//bulk_template.csv"
        self.choose_file(InternalBulkCheck.bulk_check_upload_template, 'C:\\Users\\Fadhil\\HaloCheck_Bulk_Search_Template.csv')
        self.click(InternalBulkCheck.bulk_check_submit_button)
        self.assert_element(InternalBulkCheck.bulk_check_success_notification)
        self.sleep(10)
        self.click(InternalBulkCheck.dashboard_button)
        self.assert_elements(InternalBulkCheck.submitted_names)

    def NT_test_community_watchlist_single_upload(self):
        communityWatchlist_upload.open_homepage(self)
        communityWatchlist_upload.login(self)

        self.sleep(5)
        self.slow_click(communityWatchlist_upload.cw_sidebutton)
        self.slow_click(communityWatchlist_upload.cw_upload)
        #self.sleep(5)
        self.click(communityWatchlist_upload.single_upload)
        self.sleep(5)
        
        fake = Faker()
        fake.add_provider(bank)
        fake.add_provider(automotive)
        self.send_keys(communityWatchlist_upload.name,fake.first_name()+' '+fake.last_name())
        self.send_keys(communityWatchlist_upload.id ,fake.aba()+fake.aba())
        
        self.sleep(1)
        self.slow_click(communityWatchlist_upload.nationality)
        self.click_active_element()
        self.send_keys(communityWatchlist_upload.nationality_selection, fake.country()+"\n")

        self.sleep(1)
        self.slow_click(communityWatchlist_upload.case_category)
        self.click_active_element()
        self.send_keys(communityWatchlist_upload.case_category_fraud, "Fraud\n")

        self.click("div#root > div > main > div > div:nth-of-type(2) > div > form > div:nth-of-type(4) > div:nth-of-type(2) > input")
        self.select_option_by_text("div.modal-body div:nth-of-type(2) span span select", "April")
        self.select_option_by_text("div.modal-body div:nth-of-type(2) span span:nth-of-type(3) select", "2019")
        self.click("div.modal-body div:nth-of-type(3) div:nth-of-type(2) button:nth-of-type(5)")
        self.click('button:contains("Confirm")')
        self.click("//button[normalize-space()='Submit']")
        
        scrollable_popup = self.find_element("//div[@class='form-text p-3']")
        for i in range(5):
            self.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
        self.check_if_unchecked("div.modal-body div:nth-of-type(2) input")
        self.sleep(5)
        self.click('button:contains("I Agree")')
        self.sleep(5)
    
    def NT_test_community_watchlist_bulk_upload(self):
        communityWatchlist_bulk_upload.open_homepage(self)
        communityWatchlist_bulk_upload.login(self)

        self.sleep(5)
        self.slow_click(communityWatchlist_bulk_upload.cw_sidebutton)
        self.slow_click(communityWatchlist_bulk_upload.cw_sidebutton_upload)
        self.slow_click(communityWatchlist_bulk_upload.cw_bulk_upload)
        self.sleep(5)

        self.click(communityWatchlist_bulk_upload.cw_download_bulk_template)
        self.choose_file(communityWatchlist_bulk_upload.cw_upload_bulk_template, 'C:\\Users\\Fadhil\\bulk_cw_template.csv')
        self.click(communityWatchlist_bulk_upload.cw_submit_bulk_upload_template)
        self.sleep(5)
        
        self.assert_element(communityWatchlist_bulk_upload.cw_tnc)
        self.click(communityWatchlist_bulk_upload.cw_tnc_tick)
        self.click(communityWatchlist_bulk_upload.cw_tnc_agree)
        self.sleep(5)

        self.assert_element(communityWatchlist_bulk_upload.cw_bulk_success_notification)
        self.click(communityWatchlist_bulk_upload.cw_bulk_success_notification_close_button)
        self.sleep(5)

    def test_transaction_history_checks(self):
        TransactionHistory.open_homepage(self)
        TransactionHistory.login(self)
        #self.sleep(60)
        
        self.sleep(5)
        self.click(TransactionHistory.transaction_history_sidebar)
        self.click(TransactionHistory.transaction_history_checks_sidebar)
        self.sleep(5)
        self.assert_elements(TransactionHistory.top_date, TransactionHistory.top_subject, TransactionHistory.top_type, TransactionHistory.top_credit, TransactionHistory.top_user, TransactionHistory.top_report)
        self.click(TransactionHistory.download_checks_1)
        self.sleep(5)
        self.click(TransactionHistory.history_tab)
        self.sleep(5)
        self.assert_elements(TransactionHistory.top_period, TransactionHistory.top_credit_used, TransactionHistory.top_history)
        self.click(TransactionHistory.download_history_1)
        self.sleep(10)
    
    def test_transaction_history_credits(self):
        TransactionHistory.open_homepage(self)
        TransactionHistory.login(self)
        #self.sleep(60)
        
        self.sleep(5)
        self.click(TransactionHistory.transaction_history_sidebar)
        self.click(TransactionHistory.transaction_history_credits_sidebar)
        self.sleep(5)
        self.assert_elements(TransactionHistory.top_date, TransactionHistory.top_category, TransactionHistory.top_credits, TransactionHistory.top_description, TransactionHistory.top_performed_by)
        self.click(TransactionHistory.history_tab2)
        self.sleep(5)
        self.assert_elements(TransactionHistory.top_period, TransactionHistory.top_report)
        #self.click(TransactionHistory.download_history_2)
        self.sleep(5)
class createUsercompany(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("//button[normalize-space()='Log In']")
    companies_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Companies')]")
    back_button = ("//a[normalize-space()='Back']")
    logout_button = ("//a[@data-rb-event-key='/app/logout']")
    companies_button = ("//a[@data-rb-event-key='/app/companies']")
    create_company_button  = ('body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
    company_name = ("input[name='tenant_name']")
    edit_company = ("(//*[name()='svg'][@role='img'])[13]")
    users_button = ("//button[normalize-space()='Users']")
    create_user_company_button = ("//a[normalize-space()='User']")
    user_company_username = ("//input[@name='email']")
    update_company_title = ("//span[@class='hero-title']")
    user_company_firstname = ("//input[@name='first_name']")
    user_company_lastname = ("//input[@name='last_name']")
    user_company_contact_number = ("//input[@name='contact_no']")
    user_company_role = ("div[class='select__value-container css-1jpk8o5'] div[class='select__input-container css-19bb58m']")
    user_company_role_tenant_executive = ("#react-select-8-input")
    user_company_status = ("//body[1]/div[1]/div[1]/main[1]/div[2]/div[2]/form[1]/div[7]/div[1]/div[1]/div[1]/div[1]")
    user_company_status_selection = ("#react-select-3-input")
    save_user_company_button = ("//button[@type='submit']")
    account_created_notification = ("//div[@role='alert']")
    account_created_notification_close_button = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    companies_dashboard_url = ('')
    create_user_company_url = ('')

    
    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/")
        self.sleep(1)
    
    def login(self):
        self.sleep(2)

        args = sys.argv[1:]
        var1 = None
        var2 = None
        for arg in args:
            if arg.startswith("--var1="):
                var1 = arg.split("=")[1]
            elif arg.startswith("--var2="):
                var2 = arg.split("=")[1]
        self.send_keys(createUsercompany.email_bar, var1)
        # find login bar and key in email

        self.send_keys(createUsercompany.password_bar, var2)
        self.click(createUsercompany.login_button)

class DeleteTenantUser(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("//button[normalize-space()='Log In']")
    companies_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Companies')]")
    back_button = ("//a[normalize-space()='Back']")
    logout_button = ("//a[@data-rb-event-key='/app/logout']")
    companies_button = ("//a[@data-rb-event-key='/app/companies']")
    create_company_button  = ('body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
    company_name = ("input[name='tenant_name']")
    edit_company = ("(//*[name()='svg'][@role='img'])[13]")
    users_button = ("//button[normalize-space()='Users']")
    update_company_title = ("//span[@class='hero-title']")
    edit_user = ("(//*[name()='svg'][@role='img'])[17]")
    delete_user = ("//button[normalize-space()='Delete']")
    delete_user_confirmation = ("//body/div[@role='dialog']/div/div[1]")
    delete_user_confirm_button = ("//button[normalize-space()='Confirm']")
    delete_user_notification = ("//div[@role='alert']")
    delete_user_notification_close_button = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    page_2 = ("(//a[normalize-space()='2'])[1]")


    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/")
        self.sleep(1)


    def login(self):
        self.sleep(2)

        args = sys.argv[1:]
        var1 = None
        var2 = None
        for arg in args:
            if arg.startswith("--var1="):
                var1 = arg.split("=")[1]
            elif arg.startswith("--var2="):
                var2 = arg.split("=")[1]
        self.send_keys(createUsercompany.email_bar, var1)
        # find login bar and key in email

        self.send_keys(createUsercompany.password_bar, var2)
        self.click(createUsercompany.login_button)

class TransferWithdrawCredit2(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("//button[normalize-space()='Log In']")
    companies_title = ('#root > div > aside > div > div.sidebar-menu-body > div > a:nth-child(8) > span')
    back_button = ("//a[normalize-space()='Back']")
    logout_button = ("a[role='button'] span:nth-child(1)")
    companies_button = ("(//span[normalize-space()='Organisation'])")
    jessica = ("(//*[name()='svg'][@role='img'])[13]")
    list_user = ("(//button[normalize-space()='Users'])[1]")
    page3 = ("(//a[normalize-space()='3'])[1]")
    transfer_credit = ("//tbody/tr[1]/td[7]/a[1]//*[name()='svg']")
    withdraw_credit = ("//tbody/tr[1]/td[7]/a[2]//*[name()='svg']")
    amount_credit = ("(//input[@placeholder='No. of credits'])[1]")
    confirm_button = ("//button[normalize-space()='Confirm']")
    cancel_button = ("//button[normalize-space()='Cancel']")
    topup_popup = ("//body/div[@role='dialog']/div/div[1]")
    deduct_popup = ("//body/div[@role='dialog']/div/div[1]")
    notification = ("//div[@role='alert']")
    notification_close = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    edit_user1 = ("(//*[name()='path'][@fill='currentColor'])[23]")
    
    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/")
        self.sleep(1)

    def open_email(self):
        self.open_new_tab('https://mail.google.com/mail/u/0/#inbox')

    def login(self):
        self.sleep(2)

        args = sys.argv[1:]
        var1 = None
        var2 = None
        for arg in args:
            if arg.startswith("--var1="):
                var1 = arg.split("=")[1]
            elif arg.startswith("--var2="):
                var2 = arg.split("=")[1]
        self.send_keys(TransferWithdrawCredit2.email_bar, var1)
        # find login bar and key in email

        self.send_keys(TransferWithdrawCredit2.password_bar, var2)
        self.click(TransferWithdrawCredit2.login_button)

class SingleRiskCheck(BaseCase):
    halocheck_logo = ("//a[@title='HaloCheck']//img[@alt='HaloCheck']")
    home_button = ("//a[@data-rb-event-key='/app/home']")
    search_button = ("(//span[normalize-space()='Search'])[1]")
    single_check = ("//span[normalize-space()='Single Check']")
    companies_button = ("//a[@data-rb-event-key='/app/companies']")
    account_button = ("//span[contains(text(),'Superadmin')]")
    logout_button = ("//span[normalize-space()='Logout']")
    data_button = ("//span[normalize-space()='Data']")
    settings_button = ("//span[normalize-space()='Settings']")
    users_button = ("//span[normalize-space()='Users']")
    single_check_title = ("//span[@class='hero-title']")
    submit_search_button = ("(//button[@type='submit'])[1]")
    search_bar = ("//input[@placeholder='Enter Name*']")
    country_selection = ("(//div)[50]")
    search_results_title = ("//span[normalize-space()='Search Results']")
    new_search_button = ("//span[normalize-space()='Search Results']")
    high_match_result = ("//img[@src='/assets/images/high-match.png']")
    download_result_1 = ("(//*[name()='svg'][@role='img'])[9]")
    risk_check_tab = ("//button[@role='tab']")
    number_tab = ("//th[normalize-space()='No.']")
    subject_tab = ("//th[normalize-space()='Subject']")
    country_tab = ("//th[normalize-space()='Country']")
    category_tab = ("//th[normalize-space()='Category']")
    match_tab = ("//th[normalize-space()='Match']")
    category_1 = ("input[value='1'][name='category']")
    category_2 = ("input[value='2'][name='category']")
    category_3 = ("input[value='4']")
    category_4 = ("input[value='3'][name='category']")
    category_5 = ("input[value='5']")
    downloaded_notification = ("//div[@role='alert']")

    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/")
        self.sleep(1)


    def login(self):
        args = sys.argv[1:]
        var1 = None
        var2 = None
        for arg in args:
            if arg.startswith("--var1="):
                var1 = arg.split("=")[1]
            elif arg.startswith("--var2="):
                var2 = arg.split("=")[1]
        self.send_keys(createUser.email_bar, var1)
        # find login bar and key in email

        self.send_keys(createUser.password_bar, var2)
        self.click(createUser.login_button)
        self.sleep(2)

class createUser(BaseCase):
    homepage_title = ("halocheck")
    halocheck_logo = ("//*[@id='app']/div/div/div[1]/main/div/div/header/div/div/div/div[1]/div/div/div[3]")
    halocheck_dashboard_logo = ("a[title='HaloCheck'] img[alt='HaloCheck']")
    login_button = ("//button[normalize-space()='Log In']")
    email_bar = ("input[name='username']")
    email = ("sooyee.ngoi91@gmail.com")
    password_bar = ("input[name='password']")
    password = ("HCdevp@$$")
    login_bar = ("//*[@id='app']/div/div/main/div/div/div/div/div[1]/div[5]/div/button/span")
    halocheck_url = ("https://halocheck.xyz/topup/plan")
    usermanagement = ('')
    back_button = ('')
    create_user_button = ("//a[normalize-space()='Create user']")
    create_user_title = ("//span[normalize-space()='Create User']")
    logout_button = ("a[role='button'] span:nth-child(1)")
    dashboard_username = ("//input[@name='email']")
    dashboard_firstname = ("//input[@name='first_name']")
    dashboard_lastname = ("//input[@name='last_name']")
    dashboard_contactnumber = ("//input[@name='contact_no']")
    dashboard_role = ("//div[@class='select__value-container css-1jpk8o5']//div[@class='select__input-container css-19bb58m']")
    dashboard_role_selection = ("#react-select-3-input")
    dashboard_status = ("//div[@class='select__value-container select__value-container--has-value css-1jpk8o5']//div[@class='select__input-container css-19bb58m']")
    dashboard_status_selection = ("#react-select-4-input")
    dashboard_save = ("button[type='submit']")
    dashboard_role_superadmin = ('')
    account_created_notification = ("div[role='alert']")
    dashboard_url = ('https://app-testing.halocheck.com.my//users')
    users_button = ("//a[@data-rb-event-key='/app/users']")
    verification_link = ('')
    account_verification_title = ('')
    account_verification_title2 = ('')
    enter_new_password = ('')
    reenter_new_password = ('')
    save_verification_button = ('')
    account_verified_title = ('')
    account_verified_title2 = ('')
    password_updated_logo = ('')
    account_verified_login_button = ('')
    account_verified_text = ('Your password has been reset successfully. You may now log in to HaloCheck Risk System')


    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/")

    def open_email(self):
        self.open_new_tab('https://mail.google.com/mail/u/0/#inbox')

    def login(self):
        args = sys.argv[1:]
        var1 = None
        var2 = None
        for arg in args:
            if arg.startswith("--var1="):
                var1 = arg.split("=")[1]
            elif arg.startswith("--var2="):
                var2 = arg.split("=")[1]
        self.send_keys(createUser.email_bar, var1)
        # find login bar and key in email

        self.send_keys(createUser.password_bar, var2)
        self.click(createUser.login_button)
        self.sleep(2)

class InternalBulkCheck(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("//button[normalize-space()='Log In']")
    halocheck_logo = ("//a[@title='HaloCheck']//img[@alt='HaloCheck']")
    home_button = ("//a[@data-rb-event-key='/app/home']")
    search_button = ("//span[normalize-space()='Search']")
    companies_button = ("//a[@data-rb-event-key='/app/companies']")
    account_button = ("//span[contains(text(),'Superadmin')]")
    logout_button = ("//span[normalize-space()='Logout']")
    data_button = ("//span[normalize-space()='Data']")
    settings_button = ("//span[normalize-space()='Settings']")
    users_button = ("//span[normalize-space()='Users']")
    single_check_title = ("//span[@class='hero-title']")
    submit_search_button = ("(//button[@type='submit'])[1]")
    search_bar = ("//input[@placeholder='e.g. John Doe']")
    country_selection = ("(//div)[50]")
    search_results_title = ("//span[normalize-space()='Search Results']")
    new_search_button = ("//span[normalize-space()='Search Results']")
    high_match_result = ("//img[@src='/assets/images/high-match.png']")
    download_result_1 = ("(//*[name()='svg'][@role='img'])[11]")
    risk_check_tab = ("//button[@role='tab']")
    number_tab = ("//th[normalize-space()='No.']")
    subject_tab = ("//th[normalize-space()='Subject']")
    country_tab = ("//th[normalize-space()='Country']")
    category_tab = ("//th[normalize-space()='Category']")
    match_tab = ("//th[normalize-space()='Match']")
    bulk_check_button = ("//span[normalize-space()='Bulk Check']")
    bulk_check_title = ("")
    bulk_check_download_template = ("//button[normalize-space()='Download']")
    bulk_check_settings = ("//button[normalize-space()='Check Settings']")
    bulk_check_upload_template = ("(//input[@name='file'])[1]")
    bulk_check_submit_button = ("//button[@type='submit']")
    bulk_check_success_notification = ("//div[@role='alert']")
    dashboard_button = ("(//button[normalize-space()='Dashboard'])[1]")
    submitted_names = ("//th[normalize-space()='Submitted Names']")
    

    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/")
        self.sleep(1)


    def login(self):
        args = sys.argv[1:]
        var1 = None
        var2 = None
        for arg in args:
            if arg.startswith("--var1="):
                var1 = arg.split("=")[1]
            elif arg.startswith("--var2="):
                var2 = arg.split("=")[1]
        self.send_keys(InternalBulkCheck.email_bar, var1)
        # find login bar and key in email
        self.send_keys(InternalBulkCheck.password_bar, var2)
        self.click(InternalBulkCheck.login_button)

class communityWatchlist_upload(BaseCase):
    homepage_title = ("halocheck")
    halocheck_logo = ("//*[@id='app']/div/div/div[1]/main/div/div/header/div/div/div/div[1]/div/div/div[3]")
    halocheck_dashboard_logo = ("a[title='HaloCheck'] img[alt='HaloCheck']")
    login_button = ("//button[normalize-space()='Log In']")
    email_bar = ("input[name='username']")
    email = ("sooyee.ngoi91@gmail.com")
    password_bar = ("input[name='password']")
    password = ("HCdevp@$$")
    login_bar = ("//*[@id='app']/div/div/main/div/div/div/div/div[1]/div[5]/div/button/span")
    users_button = ("//a[@data-rb-event-key='/app/users']")
    users_dashboard_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Users')]")
    back_button = ("//a[normalize-space()='Back']")
    cw_sidebutton = ("//span[normalize-space()='Community Reference']")
    cw_upload = ("//span[normalize-space()='Upload']")
    cw_single_upload = ("(//*[name()='path'][@fill='currentColor'])[7]")
    single_upload = ("//span[normalize-space()='Single Upload']")
    name = ("//input[@name='subject_name']")
    id = ("//input[@name='subject_id']")
    nationality = ("(//div[@class='select__value-container css-1jpk8o5'])[1]")
    nationality_selection = ("#react-select-3-input")
    case_category = ("(//div[@class='select__input-container css-19bb58m'])[2]")
    case_category_fraud = ("#react-select-4-input")
    case_date = ("//input[@class='form-control datepicker-field form-control']")
    select_year = ("//span[@class='rdrYearPicker']//select")
    select_year_2020 = ("")
    select_date = ("(//span[@class='rdrDayNumber'])[4]")
    additional_info = ("")
    phone = ("")
    bankname = ("")
    bankno = ("")
    email_cw = ("")
    address_cw = ("")
    website_cw  = ("")
    vehicleno = ("")
    others_cw = ("")
    cw_next = ("")
    cw_tick_agree = ("")
    cw_agree_button = ("")
    cw_case_date_confirm = ("")

    
    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/")

    def login(self):
        args = sys.argv[1:]
        var1 = None
        var2 = None
        for arg in args:
            if arg.startswith("--var1="):
                var1 = arg.split("=")[1]
            elif arg.startswith("--var2="):
                var2 = arg.split("=")[1]
        self.send_keys(communityWatchlist_upload.email_bar, var1)
        # find login bar and key in email
        self.send_keys(communityWatchlist_upload.password_bar, var2)
        self.click(communityWatchlist_upload.login_button)

class communityWatchlist_management(BaseCase):
    homepage_title = ("halocheck")
    halocheck_logo = ("//*[@id='app']/div/div/div[1]/main/div/div/header/div/div/div/div[1]/div/div/div[3]")
    halocheck_dashboard_logo = ("a[title='HaloCheck'] img[alt='HaloCheck']")
    login_button = ("//button[@name='action']")
    email_bar = ("input[name='username']")
    email = ("sooyee.ngoi91@gmail.com")
    password_bar = ("input[name='password']")
    password = ("HCdevp@$$")
    login_bar = ("//*[@id='app']/div/div/main/div/div/div/div/div[1]/div[5]/div/button/span")
    users_button = ("//a[@data-rb-event-key='/app/users']")
    users_dashboard_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Users')]")
    back_button = ("//a[normalize-space()='Back']")
    cw_sidebutton = ("")
    cw_management = ("")
    cw_management_filter =("")
    cw_filter = ("")
    cw_filter_apply_filter = ("")
    cw_filter_all_user = ("")
    cw_filter_company = ("")
    cw_filter_all_company = ("")
    cw_case_1 = ("")
    cw_case_2 = ("")
    cw_status = ("")
    cw_status_active = ("")
    cw_status_inactive = ("")
    cw_status_expiring = ("")
    cw_status_retired = ("")
    cw_status_expired = ("")
    cw_case_save_button = ("")
    cw_history_tab = ("")
    cw_last_update = ("")
    cw_item = ("")
    cw_performed_by = ("")



    
    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/")

    def login(self):
        args = sys.argv[1:]
        var1 = None
        var2 = None
        for arg in args:
            if arg.startswith("--var1="):
                var1 = arg.split("=")[1]
            elif arg.startswith("--var2="):
                var2 = arg.split("=")[1]
        self.send_keys(communityWatchlist_management.email_bar, var1)
        # find login bar and key in email
        self.send_keys(communityWatchlist_management.password_bar, var2)
        self.click(communityWatchlist_management.login_button)

class communityWatchlist_bulk_upload(BaseCase):
    homepage_title = ("halocheck")
    halocheck_logo = ("//*[@id='app']/div/div/div[1]/main/div/div/header/div/div/div/div[1]/div/div/div[3]")
    halocheck_dashboard_logo = ("a[title='HaloCheck'] img[alt='HaloCheck']")
    login_button = ("//button[@name='action']")
    email_bar = ("input[name='username']")
    email = ("sooyee.ngoi91@gmail.com")
    password_bar = ("input[name='password']")
    password = ("HCdevp@$$")
    login_bar = ("//*[@id='app']/div/div/main/div/div/div/div/div[1]/div[5]/div/button/span")
    users_button = ("//a[@data-rb-event-key='/app/users']")
    users_dashboard_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Users')]")
    back_button = ("//a[normalize-space()='Back']")
    cw_sidebutton = ("")
    cw_sidebutton_upload = ("")
    cw_single_upload = ("")
    cw_bulk_upload = ("")
    cw_download_bulk_template = ("")
    cw_upload_bulk_template = ("")
    cw_submit_bulk_upload_template = ("")
    cw_bulk_success_notification = ("")
    cw_bulk_success_notification_close_button = ("")
    cw_tnc = ("")
    cw_tnc_tick = ("")
    cw_tnc_agree = ("")

    



    
    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/")

    def login(self):
        args = sys.argv[1:]
        var1 = None
        var2 = None
        for arg in args:
            if arg.startswith("--var1="):
                var1 = arg.split("=")[1]
            elif arg.startswith("--var2="):
                var2 = arg.split("=")[1]
        self.send_keys(communityWatchlist_bulk_upload.email_bar, var1)
        # find login bar and key in email
        self.send_keys(communityWatchlist_bulk_upload.password_bar, var2)
        self.click(communityWatchlist_bulk_upload.login_button)

class TransactionHistory(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("//button[normalize-space()='Log In']")
    transaction_history_sidebar = ("//span[normalize-space()='Transaction History']")
    transaction_history_checks_sidebar =("//span[normalize-space()='Checks']")
    transaction_history_credits_sidebar = ("//span[normalize-space()='Credits']")
    top_date = ("//th[normalize-space()='Date']")
    top_subject = ("//th[normalize-space()='Subject']")
    top_type = ("//th[normalize-space()='Type']")
    top_credit = ("//th[normalize-space()='Credit']")
    top_user = ("//th[normalize-space()='User']")
    top_report = ("//th[normalize-space()='Report']")
    download_checks_1 = ("(//*[name()='svg'][@role='img'])[10]")
    history_tab = ("(//a[normalize-space()='History'])[1]")
    top_period = ("//th[normalize-space()='Period']")
    top_credit_used = ("//th[normalize-space()='Total Credit Used']")
    top_history = ("//th[normalize-space()='History']")
    download_history_1 = ("//td[@role='cell']//a//*[name()='svg']")
    top_category = ("//th[normalize-space()='Category']")
    top_credits = ("//th[normalize-space()='Credits']")
    top_description = ("//th[normalize-space()='Description']")
    top_performed_by = ("//th[normalize-space()='Performed By']")
    download_history_2 = ("//td[@role='cell']//a//*[name()='svg']")
    history_tab2 = ("//a[normalize-space()='History']")

    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/")
        self.sleep(1)

    def open_email(self):
        self.open_new_tab('https://mail.google.com/mail/u/0/#inbox')

    def login(self):
        self.sleep(2)

        args = sys.argv[1:]
        var1 = None
        var2 = None
        for arg in args:
            if arg.startswith("--var1="):
                var1 = arg.split("=")[1]
            elif arg.startswith("--var2="):
                var2 = arg.split("=")[1]
        self.send_keys(TransactionHistory.email_bar, var1)
        # find login bar and key in email

        self.send_keys(TransactionHistory.password_bar, var2)
        self.click(TransactionHistory.login_button)


