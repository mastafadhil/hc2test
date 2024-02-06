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
        self.assert_elements(ManagePromo.header_code, ManagePromo.header_label, ManagePromo.header_type, ManagePromo.header_status)
        self.click('a[href="#/app/promotions/add"]')
        self.send_keys(ManagePromo.promo_label, fake.first_name().upper()+fake.year())
        self.send_keys(ManagePromo.promo_code, fake.pystr_format(string_format=f"??###??#").upper())
        self.click('//div[3]//div[1]//input[1]')
        self.select_option_by_text("div.modal-body div div:nth-of-type(2) span span select", "February")
        self.select_option_by_text("div.modal-body div div:nth-of-type(2) span span:nth-of-type(3) select", "2025")
        self.click("div.modal-body div div:nth-of-type(3) div:nth-of-type(2) button:nth-of-type(7)")
        self.sleep(5)
        self.click("div.modal-body div div:nth-of-type(3) div:nth-of-type(2) button:nth-of-type(34)")
        self.click('button:contains("Confirm")')
        self.sleep(5)
        self.send_keys(ManagePromo.quantity,  fake.random_int(min=1, max=10))
        self.send_keys(ManagePromo.redemption_per_user,  fake.random_int(min=1, max=10))
        self.send_keys(ManagePromo.percentage_off,  fake.random_int(min=1, max=10))

        #self.send_keys(ManagePromo.promo_code_stripe_voucher_id, fake.pystr_format(string_format=f"??###??#").upper())
        self.send_keys(ManagePromo.promo_code_remarks, fake.sentence())
        #self.click(ManagePromo.promo_code_fixed_amount)
        #self.send_keys(ManagePromo.promo_amount_discount, fake.random_int(min=1, max=10))
        self.choose_file('input[name="tnc_file"]', 'C:\\Users\\Fadhil\\20240130_MAHATHIR_BIN_IDRUS_M_PGL1F6.pdf')
        self.sleep(5)
        self.slow_click(ManagePromo.promo_save)
        self.sleep(10)
       
    
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
    login_button = ("//button[normalize-space()='Log In']")
    promo_sidebar = ("//span[normalize-space()='Promotion']")
    promo_type = ("")
    promo_status = ("")
    header_code = ("//th[normalize-space()='Promo Code']")
    header_label = ("//th[normalize-space()='Promo Label']")
    header_type = ("//th[normalize-space()='Promo Type']")
    header_date_start = ("//th[normalize-space()='Date Start']")
    header_date_end = ("//th[normalize-space()='Date End']")
    header_status = ("//th[normalize-space()='Date End']")
    total_redemption = ("")
    create_promo = ("//a[normalize-space()='Create promotion']")
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
    promo_label = ("//input[@label='Promo Label*']")
    promo_code = ("//input[@label='Promo Code*']")
    quantity = ("//input[@label='Quantity*']")
    redemption_per_user = ("//input[@label='Redemption Per User']")
    percentage_off = ("//input[@label='Percentage Off*']")

    promo_code_date_start_end = ("")
    promo_code_stripe_voucher_id = ("")
    promo_code_remarks = ("//div[@role='tabpanel']//div//form//div//div//textarea")
    promo_amount_discount = ("")
    promo_save = ("//button[normalize-space()='Create']")
    view_promo = ("")
    promo_toggle = ("")
    promo_pdf = ("//button[normalize-space()='Upload Terms & Conditions']")


    def open_homepage(self):
        self.maximize_window()
        self.open("https://app-testing.halocheck.com.my/#/app/search/singlecheck")
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