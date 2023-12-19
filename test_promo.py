from seleniumbase import BaseCase
import sys
from faker import Faker
from pathlib import Path
from faker.providers import bank
from faker.providers import automotive
from faker.providers import company
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

## Run "pytest test_admin.py --var1='xevex21147@fsouda.com' --var2='@Bcd1234' --dashboard --html=report_test-server_superadmin.html --reruns=3"
## Run "pytest test_admin.py --var1='pemirij500@ezgiant.com' --var2='@Bcd1234' --dashboard --html=report_test-server_itmanager.html --reruns=3"
## Run "pytest test_admin.py --var1='capaxof217@ekcsoft.com' --var2='@Bcd1234' --dashboard --html=report_test-server_operationmanager.html --reruns=3"
## SuperAdmin "sooyee@halocheck.xyz", password "HCdevp@$$"
## IT Manager "matod75457@webonoid.com", password "@Bcd1234"
## Operation Manager "sokih76263@v3dev.com", password "@Bcd1234" 
## this script is to be used with Superadmin, IT Manager, and Operation Manager only
## all of the features are tested unless not ready
## NT on test case name means NOT TESTED(skipped)

class admin_script(BaseCase):
    def test_create_promo(self):
        ManagePromo.open_homepage(self)
        ManagePromo.login(self)

        fake = Faker()
        self.click(ManagePromo.promo_sidebar)
        self.sleep(3)
        self.assert_elements(ManagePromo.promo_code, ManagePromo.promo_label, ManagePromo.promo_type, ManagePromo.promo_status)
        self.click(ManagePromo.create_promo)
        self.sleep(5)
        self.send_keys(ManagePromo.promo_label, fake.first_name().upper()+fake.year())
        self.send_keys(ManagePromo.promo_code, fake.pystr_format(string_format=f"??###??#").upper())
        self.send_keys(ManagePromo.promo_code_stripe_voucher_id, fake.pystr_format(string_format=f"??###??#").upper())
        self.click(ManagePromo.promo_code_date_start_end)
        self.send_keys(ManagePromo.promo_code_remarks, fake.sentence())
        self.click(ManagePromo.promo_code_fixed_amount)
        self.send_keys(ManagePromo.promo_amount_discount, fake.random_int(min=1, max=10))
        self.click(ManagePromo.promo_save)
    
    def test_duplicate_promo(self):
        ManagePromo.open_homepage(self)
        ManagePromo.login(self)

        fake = Faker()
        self.click(ManagePromo.promo_sidebar)
        self.sleep(3)
        self.assert_elements(ManagePromo.promo_code, ManagePromo.promo_label, ManagePromo.promo_type, ManagePromo.promo_status)
        self.click(ManagePromo.duplicate_promo)
        self.assert_elements(ManagePromo.duplicate_notification, ManagePromo.duplicate_confirm, ManagePromo.duplicate_cancel)
        self.click(ManagePromo.duplicate_confirm)
        self.sleep(5)
        self.send_keys(ManagePromo.promo_code, fake.pystr_format(string_format=f"??###??#").upper())
        self.send_keys(ManagePromo.promo_code_stripe_voucher_id, fake.pystr_format(string_format=f"??###??#").upper())
        self.click(ManagePromo.promo_code_date_start_end)
        self.click(ManagePromo.promo_save)

    


        

class ManagePromo(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    promo_sidebar = ("")
    header_code = ("")
    header_label = ("")
    header_type = ("")
    header_date_start = ("")
    header_date_end = ("")
    header_status = ("")
    total_redemption = ("")
    create_promo = ("")
    promo_filter = ("")
    filter_discount = ("")
    filter_free_trial = ("")
    filter_free_paidcredit = ("")
    filter_active = ("")
    filter_inactive = ("")
    filter_expired = ("")
    filter_fully_redeemed = ("")
    filter_date_range = ("")
    apply_filter = ("")
    duplicate_promo = ("")
    duplicate_notification = ("")
    duplicate_confirm = ("")
    duplicate_cancel = ("")
    promo_label = ("")
    promo_code = ("")
    promo_code_date_start_end = ("")
    promo_code_stripe_voucher_id = ("")
    promo_code_remarks = ("")
    promo_amount_discount = ("")
    promo_save = ("")
    view_promo = ("")
    promo_toggle = ("")


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
        self.send_keys(ManagePromo.email_bar, var1)
        # find login bar and key in email

        self.send_keys(ManagePromo.password_bar, var2)
        self.click(ManagePromo.login_button)