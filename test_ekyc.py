from seleniumbase import BaseCase
import sys
from faker import Faker
from pathlib import Path
from faker.providers import bank
from faker.providers import automotive
from selenium import webdriver
from seleniumbase import BaseCase
from seleniumbase import SB
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

## Run "pytest test_ekyc.py --var1='xevex21147@fsouda.com' --var2='@Bcd1234' --dashboard --html=report_test-server_superadmin_ekyc_2august.html --reruns=3"
## Run "pytest test_ekyc.py --var1='pemirij500@ezgiant.com' --var2='@Bcd1234' --dashboard --html=report_test-server_itmanager_ekyc_2august.html --reruns=3"
## Run "pytest test_ekyc.py --var1='capaxof217@ekcsoft.com' --var2='@Bcd1234' --dashboard --html=report_test-server_operationmanager_ekyc_2august.html --reruns=3"
## Run "pytest test_ekyc.py --var1='xocec54350@ezgiant.com' --var2='@Bcd1234' --dashboard --html=report_test-server_operationexec_ekyc_2august.html --reruns=3"
## Run "pytest test_ekyc.py --var1='hiyefot540@farebus.com' --var2='@Bcd1234' --dashboard --html=report_test-server_tenantadmin_ekyc_2august.html --reruns=3"
## Run "pytest test_ekyc.py --var1='yadep31398@farebus.com' --var2='@Bcd1234' --dashboard --html=report_test-server_tenantmanager_ekyc_2august.html --reruns=3"


class OverrideDriverTest(BaseCase):
    def get_new_driver(self, *args, **kwargs):

        """self.driver.execute_cdp_cmd(
            "Browser.grantPermissions",
            {
                "origin": 'https://web.snapchat.com',
                "permissions": ["geolocation", "audioCapture", "displayCapture", "videoCapture",
                    "videoCapturePanTiltZoom"]
            },
        )"""
        """ This method overrides get_new_driver() from BaseCase. """
        mobile_emulation = {
            "deviceMetrics": { "width": 412, "height": 915, "pixelRatio": 3 },
            "userAgent": "Mozilla/5.0 (Linux; Android 5.1; S20 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36"
        }
        
        chrome_options = webdriver.ChromeOptions()
        
        chrome_options.add_argument("--use-fake-device-for-media-stream")
        chrome_options.add_argument(r'--use-file-for-fake-video-capture=C:\Users\Fadhil\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\sloth.y4m')
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_camera": 1
        })
        return webdriver.Chrome(options=chrome_options)

    def test_ekyc_homepage(self):
        ekyc.open_homepage(self)
        ekyc.login(self)
        #self.sleep(2000)

        self.click(ekyc.ekyc_sidebutton)
        self.click(ekyc.ekyc_start)
        self.sleep(5)
        self.click(ekyc.off_sidebar)
        self.sleep(5)
        self.click(ekyc.country_bar)
        self.sleep(5)
        
        self.click(ekyc.country_bar)
        self.click(ekyc.country_bar)
        self.click_active_element()
        self.send_keys(ekyc.country_malaysia, "Malaysia\n")
        self.sleep(5)
        self.click(ekyc.ic)
        self.click(ekyc.ekyc_now)
        self.click(ekyc.start_ekyc)
        self.sleep(5)
        self.click(ekyc.snap_photo)
        self.sleep(5)
        self.click(ekyc.snap_photo)
        self.sleep(5)
        self.click(ekyc.edit_details)
        self.send_keys(ekyc.fullname, "Praveen Darren A/L Barkins\n")
        
        self.click(ekyc.nationality)
        self.click(ekyc.nationality)
        self.click_active_element()
        self.send_keys(ekyc.nationality_malaysia, "Malaysia\n")

        self.click(ekyc.gender)
        self.click(ekyc.gender)
        self.click_active_element()
        self.send_keys(ekyc.gender_male, "Male\n")
        self.send_keys(ekyc.address, "37 JPS 10/11C TAMAN DATO HORMAT 46000 PETALING JAYA SELANGOR\n")
        self.scroll_to_bottom()
        self.assert_element(ekyc.confirm_selfie2)
        self.slow_click(ekyc.confirm_selfie2)
        #self.slow_click(ekyc.confirm_selfie2)
        self.sleep(10)
        self.click(ekyc.start_selfie)
        self.sleep(2)
        self.click(ekyc.snap_selfie)
        self.sleep(5)
        #self.slow_click(ekyc.confirm_selfie2)
        self.click(ekyc.submit_ekyc)
        self.sleep(5)

        #self.sleep(2000)"""
        
class ekyc(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    companies_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Companies')]")
    back_button = ("//a[normalize-space()='Back']")
    logout_button = ("//a[@data-rb-event-key='/app/logout']")
    ekyc_sidebutton = ("//span[normalize-space()='e-KYC']")
    ekyc_start = ("//span[normalize-space()='Start']")
    off_sidebar = ("//button[@class='sidebar-toggle btn btn-dark']//*[name()='svg']")
    country_bar = ("//div[@class='select__input-container css-19bb58m']")
    country_malaysia = ("#react-select-3-input")
    ic = ("//button[normalize-space()='Identity Card']")
    passport = ("//button[normalize-space()='Passport']")
    ekyc_now = ("//button[normalize-space()='Now']")
    ekyc_remote = ("//button[normalize-space()='Remote']")
    start_ekyc = ("#root > div > div.page-content.ps-3.pe-3.d-flex.flex-column.justify-content-between > div:nth-child(2) > button")
    snap_photo = ("#root > div > div.page-content.pt-0.pb-0.d-flex.flex-column.justify-content-between > div.d-flex.ps-3.pb-3.align-items-end.position-relative > div.position-absolute.start-50.translate-middle > div > button > svg > path")
    edit_details = ("//button[@class='btn btn-link']//*[name()='svg']")
    fullname = ("//input[@name='full_name']")
    nationality = ("(//div[@class='select__input-container css-19bb58m'])[1]")
    nationality_malaysia = ("#react-select-4-input")
    gender = ("(//div[@class='select__input-container css-19bb58m'])[2]")
    gender_male = ("#react-select-5-input")
    address = ("//textarea[@name='address']")
    confirm_selfie = ("//button[@type='submit']")
    confirm_selfie2 = ("(//button[normalize-space()='Confirm'])[1]")
    start_selfie = ("//button[@type='button']")
    snap_selfie = ("//button[@class='capture-photo-btn btn btn-outline']")
    snap_selfie2 = ("(//*[name()='path'][@fill='currentColor'])[3]")
    submit_ekyc = ("//button[normalize-space()='Submit']")






    


    
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
        self.send_keys(ekyc.email_bar, var1)
        # find login bar and key in email

        self.send_keys(ekyc.password_bar, var2)
        self.click(ekyc.login_button)