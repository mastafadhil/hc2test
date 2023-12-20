from seleniumbase import BaseCase
import sys
from faker import Faker
from pathlib import Path
from faker.providers import bank
from faker.providers import automotive
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

## Run "pytest test_subscription_prepaid.py --var1='hiyefot540@farebus.com' --var2='@Bcd1234' --var3='basic' --data='monthly' -k test_subscription_tenants"
## Run "pytest test_subscription_prepaid.py --var1='hiyefot540@farebus.com' --var2='@Bcd1234' --var3='standard' --data='monthly' -k test_subscription_tenants"
## Run "pytest test_subscription_prepaid.py --var1='hiyefot540@farebus.com' --var2='@Bcd1234' --var3='pro' --data='monthly' -k test_subscription_tenants"
## Run "pytest test_subscription_prepaid.py --var1='hiyefot540@farebus.com' --var2='@Bcd1234' --var3='basic' --data='yearly' -k test_subscription_tenants"
## Run "pytest test_subscription_prepaid.py --var1='hiyefot540@farebus.com' --var2='@Bcd1234' --var3='standard' --data='yearly' -k test_subscription_tenants"
## Run "pytest test_subscription_prepaid.py --var1='hiyefot540@farebus.com' --var2='@Bcd1234' --var3='pro' --data='yearly' -k test_subscription_tenants"
## this script is to be used with Tenant Admin, Tenant Manager, Tenant Executive, Individual Users only
## all of the features are tested unless not ready
## NT on test case name means NOT TESTED(skipped)

class tenant_admin_script(BaseCase):
    def test_subscription_tenants(self):
        Subscription.open_homepage(self)
        Subscription.login(self)
        #self.sleep(60)

        self.click(Subscription.subscription_button)
        self.sleep(5)
        self.assert_elements(Subscription.Subscribe_Topup, Subscription.BillingHistory, Subscription.PaymentSettings, Subscription.CancelPlan)
        #self.click(Subscription.subscribe_now)
        """
        if (sys.argv[4]== "--var3=monthly"):
            self.click(Subscription.monthly_tab)
        elif(sys.argv[4]== "--var3=yearly"): 
            self.click(Subscription.yearly_tab)
        else :
            print('Wrong Input')"""
        css_selector = ("(//div[contains(@class,'d-flex justify-content-between section-header')])[3]")
        self.sleep(5)
        arg1 = self.var3
        arg2 = self.data
        
        if arg1 == 'basic' and arg2 == 'monthly':
            self.click(Subscription.basic_monthly)
        elif arg1 == 'standard' and arg2 == 'monthly':
            self.click(Subscription.standard_monthly)
        elif arg1 == 'pro' and arg2 == 'monthly':
            self.click(Subscription.pro_monthly)
        elif arg1 == 'basic' and arg2 == 'yearly':
            self.click(Subscription.yearly_tab)
            self.click(Subscription.basic_yearly)
        elif arg1 == 'standard' and arg2 == 'yearly':
            self.click(Subscription.yearly_tab)
            self.click(Subscription.standard_yearly)
        elif arg1 == 'pro' and arg2 == 'yearly':
            self.click(Subscription.yearly_tab)
            self.click(Subscription.pro_yearly)
        else:
            print('Wrong Input')
        
        self.click(Subscription.continue_button)
        """
        if (sys.argv[6]== "--var3=basic"):
            self.assert_element(Subscription.rm20)
        elif (sys.argv[6]== "--var3=standard"):
            self.assert_element(Subscription.rm50)
        elif (sys.argv[6]== "--var3=pro"):
            self.assert_element(Subscription.rm100)"""
        self.sleep(10)
        
        self.click(Subscription.pay_button)
        self.sleep(10)
        """self.send_keys(Subscription.card_info, "1234 1234 1234 1234")
        self.send_keys(Subscription.card_expiry_date, "12/24")
        self.send_keys(Subscription.cvc, "1234")

        self.send_keys(Subscription.name_on_card, "Muhammad Fadhil Bin Ali Kutty")
        self.click(Subscription.secure_save_info)"""
        self.click(Subscription.subscribe)

        """self.send_keys(Subscription.confirmation_code, "abcd1234")
        self.click(Subscription.confirm_payment)"""
        self.sleep(20)

        self.assert_element(Subscription.Successful)

    def test_subscription_tenant_renew(self):
        SubscriptionRenew.open_homepage(self)
        SubscriptionRenew.login(self)
        #self.sleep(60)

        self.click(SubscriptionRenew.subscription_button)
        self.sleep(5)
        self.assert_elements(SubscriptionRenew.Subscribe_Topup, SubscriptionRenew.BillingHistory, SubscriptionRenew.PaymentSettings, SubscriptionRenew.CancelPlan)
        self.click(SubscriptionRenew.renew_now)
        
        if (sys.argv[4]== "--var3=monthly"):
            self.click(SubscriptionRenew.monthly_tab)
        elif(sys.argv[4]== "--var3=yearly"): 
            self.click(SubscriptionRenew.yearly_tab)
        else :
            print('Wrong Input')

        if (sys.argv[5]== "--data='basic'"):
            self.click(SubscriptionRenew.basic)
        elif (sys.argv[5]== "--data='standard'"):
            self.click(SubscriptionRenew.standard)
        elif (sys.argv[5]== "--data='pro'"):
            self.click(SubscriptionRenew.pro)
        else :
            print('Wrong Input')
        
        self.click(SubscriptionRenew.continue_button)
        
        if (sys.argv[4]== "--var3=monthly") and (sys.argv[5]== "--data='basic'"):
            self.assert_element(SubscriptionRenew.rm20)
        elif (sys.argv[4]== "--var3=monthly") and (sys.argv[5]== "--data='standard'"):
            self.assert_element(SubscriptionRenew.rm50)
        elif (sys.argv[4]== "--var3=monthly") and (sys.argv[5]== "--data='pro'"):
            self.assert_element(SubscriptionRenew.rm100)
        elif (sys.argv[4]== "--var3=yearly") and (sys.argv[5]== "--data='basic'"):
            self.assert_element(SubscriptionRenew.rm230)
        elif (sys.argv[4]== "--var3=yearly") and (sys.argv[5]== "--data='standard'"):
            self.assert_element(SubscriptionRenew.rm570)
        elif (sys.argv[4]== "--var3=yearly") and (sys.argv[5]== "--data='pro'"):
            self.assert_element(SubscriptionRenew.rm1080)
        
        self.click(SubscriptionRenew.pay_button)
        self.sleep(10)
        self.send_keys(SubscriptionRenew.card_info, "1234 1234 1234 1234")
        self.send_keys(SubscriptionRenew.card_expiry_date, "12/24")
        self.send_keys(SubscriptionRenew.cvc, "1234")

        self.send_keys(SubscriptionRenew.name_on_card, "Muhammad Fadhil Bin Ali Kutty")
        self.click(SubscriptionRenew.secure_save_info)
        self.click(SubscriptionRenew.subscribe)

        self.send_keys(SubscriptionRenew.confirmation_code, "abcd1234")
        self.click(SubscriptionRenew.confirm_payment)
        self.sleep(5)

        self.assert_element(SubscriptionRenew.Successful)

    def test_subscription_billing_history(self):
        BillingHistory.open_homepage(self)
        BillingHistory.login(self)
        #self.sleep(60)

        self.click(BillingHistory.subscription_button)
        self.sleep(5)
        self.assert_elements(Subscription.Subscribe_Topup, Subscription.BillingHistory, Subscription.PaymentSettings, Subscription.CancelPlan)
        self.click(BillingHistory.billing_history_tab)
        self.assert_elements(BillingHistory.date, BillingHistory.invoice,BillingHistory.amount,BillingHistory.status,BillingHistory.history)
        self.click(BillingHistory.download_history_1)
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
                self.assert_pdf_text(pdf=entry.as_uri(),text="Billing History")

    def test_subscription_cancel_plan(self):
        CancelPlan.open_homepage(self)
        CancelPlan.login(self)
        #self.sleep(60)

        self.click(CancelPlan.subscription_button)
        self.sleep(5)
        self.click(CancelPlan.cancel_plan_tab)
        self.sleep(5)
        self.click(CancelPlan.confirm)
        self.assert_element(CancelPlan.popup_notification)
        self.click(CancelPlan.cancelled_ok)

    def test_organisation_credit_pricing(self):
        self.sleep()   

    def test_subscription_tenants_promo(self):
        Subscription.open_homepage(self)
        Subscription.login(self)
        #self.sleep(60)

        self.click(Subscription.subscription_button)
        self.sleep(5)
        self.assert_elements(Subscription.Subscribe_Topup, Subscription.BillingHistory, Subscription.PaymentSettings, Subscription.CancelPlan)
        #self.click(Subscription.subscribe_now)
        """
        if (sys.argv[4]== "--var3=monthly"):
            self.click(Subscription.monthly_tab)
        elif(sys.argv[4]== "--var3=yearly"): 
            self.click(Subscription.yearly_tab)
        else :
            print('Wrong Input')"""
        css_selector = ("(//div[contains(@class,'d-flex justify-content-between section-header')])[3]")
        self.sleep(5)
        arg1 = self.var3
        arg2 = self.data
        
        if arg1 == 'basic' and arg2 == 'monthly':
            self.click(Subscription.basic_monthly)
        elif arg1 == 'standard' and arg2 == 'monthly':
            self.click(Subscription.standard_monthly)
        elif arg1 == 'pro' and arg2 == 'monthly':
            self.click(Subscription.pro_monthly)
        elif arg1 == 'basic' and arg2 == 'yearly':
            self.click(Subscription.yearly_tab)
            self.click(Subscription.basic_yearly)
        elif arg1 == 'standard' and arg2 == 'yearly':
            self.click(Subscription.yearly_tab)
            self.click(Subscription.standard_yearly)
        elif arg1 == 'pro' and arg2 == 'yearly':
            self.click(Subscription.yearly_tab)
            self.click(Subscription.pro_yearly)
        else:
            print('Wrong Input')
        
        self.click(Subscription.continue_button)
        """
        if (sys.argv[6]== "--var3=basic"):
            self.assert_element(Subscription.rm20)
        elif (sys.argv[6]== "--var3=standard"):
            self.assert_element(Subscription.rm50)
        elif (sys.argv[6]== "--var3=pro"):
            self.assert_element(Subscription.rm100)"""
        self.sleep(10)
        self.send_keys(Subscription.Promo_code, "ABC1234")
        self.click(Subscription.pay_button)
        self.sleep(10)
        """self.send_keys(Subscription.card_info, "1234 1234 1234 1234")
        self.send_keys(Subscription.card_expiry_date, "12/24")
        self.send_keys(Subscription.cvc, "1234")

        self.send_keys(Subscription.name_on_card, "Muhammad Fadhil Bin Ali Kutty")
        self.click(Subscription.secure_save_info)"""
        self.click(Subscription.subscribe)

        """self.send_keys(Subscription.confirmation_code, "abcd1234")
        self.click(Subscription.confirm_payment)"""
        self.sleep(20)

        self.assert_element(Subscription.Successful)

                

class Subscription(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    subscription_button = ("//span[@class='sidebar-menu-nav-title'][normalize-space()='Subscription']")
    Subscribe_Topup = ("(//button[normalize-space()='Subscribe / Top-Up'])[1]")
    BillingHistory = ("(//button[normalize-space()='Billing History'])[1]")
    PaymentSettings = ("(//button[normalize-space()='Payment Settings'])[1]")
    CancelPlan = ("(//button[normalize-space()='Cancel Plan'])[1]")
    subscribe_now = ("//a[normalize-space()='Subscribe Now']")
    monthly_tab = ("(//button[normalize-space()='Monthly'])[1]")
    yearly_tab = ("(//button[normalize-space()='Yearly'])[1]")
    basic_monthly = ("(//div[contains(@class,'d-flex justify-content-between section-header')])[2]")
    standard_monthly = ("(//div[contains(@class,'d-flex justify-content-between section-header')])[3]")
    pro_monthly = ("(//div[contains(@class,'d-flex justify-content-between section-header')])[4]")
    basic_yearly = ("(//div[contains(@class,'d-flex justify-content-between section-header')])[5]")
    standard_yearly = ("(//div[contains(@class,'d-flex justify-content-between section-header')])[6]")
    pro_yearly = ("(//div[contains(@class,'d-flex justify-content-between section-header')])[7]")
    continue_button = ("//button[normalize-space()='Continue']")
    rm20 = ("(//div[contains(@class,'section-main-price')][normalize-space()='RM20.00'])[1]")
    rm50 = ("(//div[contains(@class,'section-main-price')][normalize-space()='RM50.00'])[1]")
    rm100 = ("(//div[contains(@class,'section-main-price')][normalize-space()='RM100.00'])[1]")
    rm230 = ("(//div[contains(@class,'section-main-price')][normalize-space()='RM230.00'])[1]")
    rm570 = ("(//div[contains(@class,'section-main-price')][normalize-space()='RM570.00'])[1]")
    rm1080 = ("(//div[contains(@class,'section-main-price')][normalize-space()='RM1080.00'])[1]")
    pay_button = ("//button[normalize-space()='Pay']")
    card_info = ("")
    card_expiry_date = ("")
    cvc = ("")
    name_on_card = ("")
    secure_save_info = ("")
    subscribe = ("//div[@class='SubmitButton-IconContainer']")
    confirmation_code = ("")
    confirm_payment = ("")
    Successful = ("(//span[@class='mt-3 mb-3 text-center'])[1]")
    Promo_code = ("")

    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/index.html/#/app/search/singlecheck")
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
        self.send_keys(Subscription.email_bar, var1)
        # find login bar and key in email

        self.send_keys(Subscription.password_bar, var2)
        self.click(Subscription.login_button)

class SubscriptionRenew(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    subscription_button = ("")
    Subscribe_Topup = ("")
    BillingHistory = ("")
    PaymentSettings = ("")
    CancelPlan = ("")
    subscribe_now = ("")
    monthly_tab = ("")
    yearly_tab = ("")
    basic = ("")
    standard = ("")
    pro = ("")
    continue_button = ("")
    rm20 = ("")
    rm50 = ("")
    rm100 = ("")
    rm230 = ("")
    rm570 = ("")
    rm1080 = ("")
    pay_button = ("")
    card_info = ("")
    card_expiry_date = ("")
    cvc = ("")
    name_on_card = ("")
    secure_save_info = ("")
    subscribe = ("")
    confirmation_code = ("")
    confirm_payment = ("")
    Successful = ("")
    renew_now = ("")

    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/index.html/#/app/search/singlecheck")
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
        self.send_keys(SubscriptionRenew.email_bar, var1)
        # find login bar and key in email

        self.send_keys(SubscriptionRenew.password_bar, var2)
        self.click(SubscriptionRenew.login_button)

class BillingHistory(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    subscription_button = ("")
    Subscribe_Topup = ("")
    BillingHistory = ("")
    PaymentSettings = ("")
    CancelPlan = ("")
    billing_history_tab = ("")
    date = ("")
    invoice = ("")
    amount = ("")
    status = ("")
    history = ("")
    download_history_1 = ("")

    
    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/index.html/#/app/search/singlecheck")
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
        self.send_keys(BillingHistory.email_bar, var1)
        # find login bar and key in email

        self.send_keys(BillingHistory.password_bar, var2)
        self.click(BillingHistory.login_button)

class CancelPlan(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    subscription_button = ("")
    Subscribe_Topup = ("")
    BillingHistory = ("")
    PaymentSettings = ("")
    CancelPlan = ("")
    cancel_plan_tab = ("")
    confirm = ("")
    popup_notification = ("")
    cancelled_ok = ("")

    
    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/index.html/#/app/search/singlecheck")
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
        self.send_keys(CancelPlan.email_bar, var1)
        # find login bar and key in email

        self.send_keys(CancelPlan.password_bar, var2)
        self.click(CancelPlan.login_button)

class OrgCreditPricing(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    organisation_button = ("")
    Subscribe_Topup = ("")
    BillingHistory = ("")
    PaymentSettings = ("")
    CancelPlan = ("")
    cancel_plan_tab = ("")
    confirm = ("")
    popup_notification = ("")
    cancelled_ok = ("")

    
    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/index.html/#/app/search/singlecheck")
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
        self.send_keys(OrgCreditPricing.email_bar, var1)
        # find login bar and key in email

        self.send_keys(OrgCreditPricing.password_bar, var2)
        self.click(OrgCreditPricing.login_button)