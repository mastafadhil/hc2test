from seleniumbase import BaseCase
import sys
from faker import Faker
from pathlib import Path
from faker.providers import bank
from faker.providers import automotive
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
    def test_create_tenant_user(self):
        createUsercompany.open_homepage(self)
        createUsercompany.login(self)

        self.click(createUsercompany.companies_button)
        #self.assert_element(createUsercompany.companies_title, createUsercompany.logout_button)
        self.sleep(5)
        self.slow_click(createUsercompany.edit_company)
        self.sleep(10)
        self.assert_element(createUsercompany.update_company_title, createUsercompany.back_button)
        self.click(createUsercompany.users_button)
        self.click(createUsercompany.create_user_company_button)

        fake = Faker()
        self.send_keys(createUsercompany.user_company_username, fake.first_name()+"@gmail.com")
        self.send_keys(createUsercompany.user_company_firstname, "Z"+fake.first_name())
        self.send_keys(createUsercompany.user_company_lastname, fake.last_name())
        self.send_keys(createUsercompany.user_company_contact_number, "012345678")
        #self.sleep(60)
        self.slow_click(createUsercompany.user_company_role)
        self.slow_click(createUsercompany.user_company_role)
        self.click_active_element()
        self.send_keys(createUsercompany.user_company_role_tenant_executive, "Tenant - Executive\n")

        #self.slow_click(createUsercompany.user_company_status)
        #self.click_active_element()
        #self.send_keys(createUsercompany.user_company_status_selection, "Inactive\n")

        self.click(createUsercompany.save_user_company_button)
        self.assert_element(createUsercompany.account_created_notification)
        self.click(createUsercompany.account_created_notification_close_button)
        
        self.assert_element(createUsercompany.update_company_title)
        self.assert_element(createUsercompany.back_button)

    def test_create_tenants(self):
        createCompany.open_homepage(self)
        createCompany.login(self)

        self.click(createCompany.companies_button)
        #self.assert_elements(createCompany.companies_title, createCompany.logout_button)
        self.click(createCompany.create_company_button)
        #self.sleep(500)
        fake = Faker()
        self.send_keys(createCompany.company_name,"ZZ"+fake.first_name()+" "+"Sdn.Bhd")
        self.send_keys(createCompany.business_registration_number, fake.phone_number())
        self.scroll_to_bottom()
        
        self.sleep(1)
        self.slow_click(createCompany.country)
        self.slow_click(createCompany.country)
        self.click_active_element()
        self.send_keys(createCompany.country_malaysia, "Malaysia\n")
        self.sleep(5)
        
        self.slow_click(createCompany.timezone)
        self.slow_click(createCompany.timezone)
        self.click_active_element()
        self.send_keys(createCompany.country_timezone, "Asia/Kuala_Lumpur\n")
        
        self.send_keys(createCompany.address, fake.address())
        
        self.send_keys(createCompany.city, fake.city())
        self.send_keys(createCompany.postcode, fake.postcode())
        self.send_keys(createCompany.state, fake.state())
        
        self.click(createCompany.company_type)
        self.click_active_element()
        self.send_keys(createCompany.company_type_selection, "Legal & Finance\n")
        

        self.click(createCompany.payment_type)
        self.click_active_element()
        self.send_keys(createCompany.payment_type_selection, "Prepaid\n")
        
        self.click(createCompany.status_type)
        self.click_active_element()
        self.send_keys(createCompany.status_type_selection, "Inactive\n")

        self.click(createCompany.create_button)
        self.assert_element(createCompany.company_created_notification)
        self.click(createCompany.company_created_notification_close)

        current_url = self.get_current_url()
        #self.assert_equal(current_url, createCompany.companies_dashboard_url)
    
    def test_create_admin_user(self):
        createUser.open_homepage(self)
        createUser.login(self)
        
        self.click(createUser.users_button)
        self.assert_element(createUser.halocheck_dashboard_logo)
        #self.assert_element(createUser.logout_button)
        self.click(createUser.create_user_button)
        self.assert_element(createUser.create_user_title)
        fake = Faker()
        self.send_keys(createUser.dashboard_username, fake.email())
        self.send_keys(createUser.dashboard_firstname, "Z"+fake.first_name())
        self.send_keys(createUser.dashboard_lastname, fake.last_name())
        self.send_keys (createUser.dashboard_contactnumber, "01791324234")
        self.sleep(5)
        
        
        self.slow_click(createUser.dashboard_role)
        self.click_active_element()
        self.send_keys(createUser.dashboard_role_selection, "Operation Executive\n")

        self.click(createUser.dashboard_status)
        self.click_active_element()
        self.send_keys(createUser.dashboard_status_selection, "Inactive\n")
        self.sleep(1)

        self.click(createUser.dashboard_save)
        self.sleep(5)
        #self.assert_element(createUser.account_created_notification)

        #createUser.open_email(self)

        #self.click(createUser.verification_link)
        #self.assert_element(createUser.account_verification_title)
        #self.assert_element(createUser.account_verification_title2)
        #self.send_keys(createUser.enter_new_password, "Abcd1234!@#$")
        #self.send_keys(createUser.reenter_new_password, "Abcd1234!@#$")
        #self.click(createUser.save_verification_button)

        #self.assert_elements(createUser.account_verified_title, createUser.account_verified_title2, createUser.account_verified_login_button, createUser.account_verified_text)

        current_url = self.get_current_url()
        #self.assert_equal(current_url, createUser.dashboard_url)

    def test_delete_tenant_user(self):
        DeleteTenantUser.open_homepage(self)
        DeleteTenantUser.login(self)
        
        self.click(DeleteTenantUser.companies_button)
        #self.assert_element(DeleteTenantUser.companies_title, DeleteTenantUser.logout_button)
        self.click(DeleteTenantUser.edit_company)
        self.sleep(5)
        self.assert_element(DeleteTenantUser.update_company_title, DeleteTenantUser.back_button)
        self.slow_click(DeleteTenantUser.users_button)
        self.sleep(5)
        self.click(DeleteTenantUser.edit_user)
        self.click(DeleteTenantUser.delete_user)
        self.sleep(10)
        self.assert_element(DeleteTenantUser.delete_user_confirmation)
        self.click(DeleteTenantUser.delete_user_confirm_button)
        self.assert_element(DeleteTenantUser.delete_user_notification)
        self.click(DeleteTenantUser.delete_user_notification_close_button)
        self.assert_element(DeleteTenantUser.update_company_title, DeleteTenantUser.back_button)
    
    def NT_test_delete_tenants(self):
        DeleteCompany.open_homepage(self)
        DeleteCompany.login(self)

        self.click(DeleteCompany.companies_button)
        self.sleep(5)
        self.click(DeleteCompany.scroll_last_page)
        self.sleep(5)
        self.double_click(DeleteCompany.edit_company)
        self.click(DeleteCompany.delete_company)
        self.click(DeleteCompany.confirm_delete_company)
        self.assert_element(DeleteCompany.company_created_notification)
        self.click(DeleteCompany.company_created_notification_close)

    def test_delete_admin_user(self):
        deleteAccount.open_homepage(self)
        deleteAccount.login(self)

        self.click(deleteAccount.users_button)

        dashboard_current_url = self.get_current_url()
        #self.assert_equal(deleteAccount.dashboard_url, dashboard_current_url)

        #self.assert_elements(deleteAccount.logout_button, deleteAccount.users_dashboard_title)
        #self.sleep(60)
        self.click(deleteAccount.entry_per_page)
        #self.click(deleteAccount.entry_50)
        self.click(deleteAccount.page3)
        self.click(deleteAccount.edit_user1)
        #self.sleep(60)
        self.click(deleteAccount.delete_button)
        self.assert_element(deleteAccount.confirm_delete_account_notification)
        #self.send_keys(deleteAccount.enter_password_confirmation_bar, "HCdevp@$$")
        self.sleep(10)
        self.click(deleteAccount.confirm_delete_account)
        self.assert_element(deleteAccount.account_deleted_notification)

        dashboard_current_url = self.get_current_url()
        #self.assert_equal(deleteAccount.dashboard_url, dashboard_current_url)
    
    def test_create_adverse_media_category(self):
        AdverseMediaCategory.open_homepage(self)
        AdverseMediaCategory.login(self)

        self.assert_element(AdverseMediaCategory.halocheck_dashboard_logo)
        self.click(AdverseMediaCategory.settings_button)
        self.click(AdverseMediaCategory.adverse_media_button)
        self.assert_elements(AdverseMediaCategory.adverse_media_title, AdverseMediaCategory.settings_title)
        self.click(AdverseMediaCategory.add_category_button)
        self.assert_elements(AdverseMediaCategory.add_category_notification, AdverseMediaCategory.confirm_add_adverse_media_category, AdverseMediaCategory.cancel_add_adverse_media_category)
        
        fake = Faker()
        self.send_keys(AdverseMediaCategory.adverse_media_category_name_bar,"ZZZ"+fake.first_name())
        self.click(AdverseMediaCategory.confirm_add_adverse_media_category)
        self.sleep(5)
        self.assert_element(AdverseMediaCategory.delete_adverse_media_category_success_notification)
        self.assert_element(AdverseMediaCategory.close_delete_adverse_media_category_success_notification_button)
        self.click(AdverseMediaCategory.close_delete_adverse_media_category_success_notification_button)
    
    def test_create_data_category(self):
        DataCategory.open_homepage(self)
        DataCategory.login(self)

        self.assert_element(DataCategory.halocheck_dashboard_logo)
        self.click(DataCategory.settings_button)
        self.click(DataCategory.general_button)
        self.assert_elements(DataCategory.datacategory_button, DataCategory.settings_title)
        self.click(DataCategory.datacategory_button)
        self.click(DataCategory.add_category_button)
        self.assert_elements(DataCategory.add_category_notification, DataCategory.confirm_add_data_category, DataCategory.cancel_add_data_category)
        
        fake = Faker()
        self.send_keys(DataCategory.data_category_name_bar,"ZZZ"+fake.first_name())
        self.click(DataCategory.confirm_add_data_category)
        self.sleep(5)
        self.assert_element(DataCategory.data_category_success_notification)
        self.assert_element(DataCategory.close_data_category_success_notification_button)
        #self.sleep(60)
        self.click(DataCategory.close_data_category_success_notification_button)
    
    def test_create_type(self):
        Type.open_homepage(self)
        Type.login(self)

        self.assert_element(Type.halocheck_dashboard_logo)
        self.click(Type.settings_button)
        self.click(Type.general_button)
        self.assert_elements(Type.datacategory_button, Type.settings_title)
        #self.click(Type.datacategory_button)
        self.click(Type.add_type_button)
        #self.assert_elements(Type.add_type_notification, Type.confirm_add_data_category, Type.cancel_add_data_category)
        
        fake = Faker()
        self.send_keys(Type.type_name_bar,"ZZZ"+fake.first_name())
        self.click(Type.confirm_add_data_category)
        self.sleep(5)
        self.assert_element(Type.data_category_success_notification)
        self.assert_element(Type.close_data_category_success_notification_button)
        self.click(Type.close_data_category_success_notification_button)
    
    def test_delete_adverse_media_category(self):
        AdverseMediaCategory.open_homepage(self)
        AdverseMediaCategory.login(self)

        self.assert_element(AdverseMediaCategory.halocheck_dashboard_logo)
        self.click(AdverseMediaCategory.settings_button)
        self.click(AdverseMediaCategory.adverse_media_button)
        self.assert_elements(AdverseMediaCategory.adverse_media_title, AdverseMediaCategory.settings_title)
        self.click(AdverseMediaCategory.last_page)
        self.assert_elements(AdverseMediaCategory.number, AdverseMediaCategory.category)
        self.click(AdverseMediaCategory.last_category_to_be_deleted)
        #self.assert_elements(AdverseMediaCategory.delete_category_notification, AdverseMediaCategory.cancel_delete_adverse_media_category,AdverseMediaCategory.confirm_delete_adverse_media_category)
        self.click(AdverseMediaCategory.confirm_delete_adverse_media_category)
        self.sleep(5)
        self.assert_element(AdverseMediaCategory.delete_adverse_media_category_success_notification)
        self.assert_element(AdverseMediaCategory.close_delete_adverse_media_category_success_notification_button)
        self.click(AdverseMediaCategory.close_delete_adverse_media_category_success_notification_button)
    
    def test_delete_data_category(self):
        DataCategory.open_homepage(self)
        DataCategory.login(self)

        self.assert_element(DataCategory.halocheck_dashboard_logo)
        self.click(DataCategory.settings_button)
        self.click(DataCategory.general_button)
        self.assert_elements(DataCategory.datacategory_button, DataCategory.settings_title)
        self.click(DataCategory.datacategory_button)
        self.sleep(5)
        self.click(DataCategory.last_page_2)
        self.click(DataCategory.delete_category_zz)
        self.sleep(10)

        self.assert_elements(DataCategory.delete_category_notification, DataCategory.confirm_delete_category_button, DataCategory.cancel_delete_category_button)
        self.click(DataCategory.confirm_delete_category_button)
        self.sleep(5)
        self.assert_element(DataCategory.data_category_success_notification)
        self.assert_element(DataCategory.close_data_category_success_notification_button)
        self.click(DataCategory.close_data_category_success_notification_button)

    def test_delete_type(self):
        Type.open_homepage(self)
        Type.login(self)

        self.assert_element(Type.halocheck_dashboard_logo)
        self.click(Type.settings_button)
        self.click(Type.general_button)
        self.assert_elements(Type.datacategory_button, Type.settings_title)
        #self.click(Type.datacategory_button)
        #self.click(Type.last_page_2)
        self.click(Type.delete_type_zz)
        self.sleep(10)

        #self.assert_elements(Type.delete_category_notification, Type.confirm_delete_category_button, Type.cancel_delete_category_button)
        self.click(Type.confirm_delete_category_button)
        self.sleep(5)
        self.assert_element(Type.data_category_success_notification)
        self.assert_element(Type.close_data_category_success_notification_button)
        self.click(Type.close_data_category_success_notification_button)
    
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

    
    def test_transfer_withdraw_credit(self):
        TransferWithdrawCredit2.open_homepage(self)
        TransferWithdrawCredit2.login(self)
        #self.sleep(60)

        self.click(TransferWithdrawCredit2.hide_search_button)
        self.click(TransferWithdrawCredit2.companies_button)
        self.sleep(5)
        self.click(TransferWithdrawCredit2.jessica)
        self.sleep(2)
        self.slow_click(TransferWithdrawCredit2.list_user)
        #self.click(TransferWithdrawCredit2.page3)
        #self.slow_click(TransferWithdrawCredit2.edit_user1)
        self.sleep(10)
        self.click(TransferWithdrawCredit2.transfer_credit)
        self.sleep(5)
        self.send_keys(TransferWithdrawCredit2.amount_credit, "1")
        self.assert_elements(TransferWithdrawCredit2.confirm_button, TransferWithdrawCredit2.cancel_button)
        self.click(TransferWithdrawCredit2.confirm_button)
        self.assert_element(TransferWithdrawCredit2.notification)
        self.click(TransferWithdrawCredit2.notification_close)
        self.sleep(10)
        self.slow_click(TransferWithdrawCredit2.withdraw_credit)
        self.sleep(5)
        self.send_keys(TransferWithdrawCredit2.amount_credit, "1")
        self.assert_elements(TransferWithdrawCredit2.confirm_button, TransferWithdrawCredit2.cancel_button)
        self.click(TransferWithdrawCredit2.confirm_button)
        self.assert_element(TransferWithdrawCredit2.notification)
        #self.click(TransferWithdrawCredit2.notification_close)
        self.sleep(5)
    
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

    def test_reset_password(self):
        resetPassword.open_homepage(self)
        resetPassword.login(self)

        #self.assert_element(resetPassword.halocheck_dashboard_logo)
        self.click(resetPassword.users_button)
        #self.assert_elements(resetPassword.logout_button, resetPassword.users_dashboard_title)
        self.sleep(5)
        self.click(resetPassword.page_2)
        self.sleep(5)
        self.slow_click(resetPassword.edit_user1)
        #self.assert_elements(resetPassword.update_user_title, resetPassword.back_button)
        self.click(resetPassword.reset_password_button)
        self.sleep(3)
        self.assert_elements(resetPassword.reset_password_notification, resetPassword.confirm_reset_password_button)
        self.sleep(2)
        self.click(resetPassword.confirm_reset_password_button)
        self.sleep(5)

    def test_resend_verification(self):
        resendVerification.open_homepage(self)
        resendVerification.login(self)

        #self.assert_element(resendVerification.halocheck_dashboard_logo)
        self.click(resendVerification.users_button)
        #self.assert_elements(resendVerification.logout_button, resendVerification.users_dashboard_title)
        #self.click(resendVerification.second_page)
        self.slow_click(resendVerification.edit_user1)
        #self.slow_click(resendVerification.resend_verification_users_page)
        self.click(resendVerification.resend_verification_edit_users_page)
        self.sleep(5)
        self.assert_elements(resendVerification.resend_account_verification_notification, resendVerification.confirm_resend_account_verification_button)
        self.click(resendVerification.confirm_resend_account_verification_button)
        self.sleep(5)
        self.assert_elements(resendVerification.success_notification, resendVerification.close_alert)

    def test_topup_deduct_credit(self):
        TopupDeductCredit.open_homepage(self)
        TopupDeductCredit.login(self)

        self.sleep(5)
        self.click(TopupDeductCredit.hide_search_button)
        self.slow_click(TopupDeductCredit.companies_button)
        self.sleep(5)
        #self.assert_elements(TopupDeductCredit.companies_title, TopupDeductCredit.logout_button)
        self.click(TopupDeductCredit.edit_company)
        self.click(TopupDeductCredit.topup_button)
        self.send_keys(TopupDeductCredit.amount_credit, "1")
        self.assert_elements(TopupDeductCredit.confirm_button, TopupDeductCredit.cancel_button)
        self.slow_click(TopupDeductCredit.confirm_button)
        #self.assert_element(TopupDeductCredit.notification)
        #self.click(TopupDeductCredit.notification_close)
        #self.sleep(5)
        #self.scroll_to_bottom
        self.sleep(5)
        self.slow_click(TopupDeductCredit.deduct_button)
        self.send_keys(TopupDeductCredit.amount_credit2, "1")
        self.assert_elements(TopupDeductCredit.confirm_button, TopupDeductCredit.cancel_button)
        self.slow_click(TopupDeductCredit.confirm_button)
        self.assert_element(TopupDeductCredit.notification)
        self.click(TopupDeductCredit.notification_close)

    def test_community_watchlist_single_upload(self):
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
        self.send_keys(communityWatchlist_upload.nationality_selection, "Malaysia\n")

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
    
    def test_community_watchlist_management(self):
        communityWatchlist_management.open_homepage(self)
        communityWatchlist_management.login(self)

        self.sleep(5)
        self.slow_click(communityWatchlist_management.cw_sidebutton)
        self.slow_click(communityWatchlist_management.cw_management)
        self.sleep(5)
        
        self.click(communityWatchlist_management.cw_management_filter)
        
        self.sleep(2)
        self.slow_click(communityWatchlist_management.filter_org)
        #self.click_active_element()
        self.send_keys(communityWatchlist_management.filter_org_selection, "Amber Sdn. Bhd\n")
        
        #self.slow_click(communityWatchlist_management.filter_status)
        #self.click(communityWatchlist_management.filter_status_selection)
        self.sleep(10)
        self.click(communityWatchlist_management.cw_filter_apply_filter)
        self.sleep(5)

        self.sleep(2)
        self.slow_click(communityWatchlist_management.cw_case_1)
        self.click(communityWatchlist_management.cw_status)
        self.click_active_element()
        #self.sleep(50)
        self.send_keys(communityWatchlist_management.cw_status_active, "Inactive\n")
        self.click(communityWatchlist_management.cw_case_save_button)
        self.sleep(10)

        self.slow_click(communityWatchlist_management.cw_case_1)
        self.click(communityWatchlist_management.cw_history_tab)
        self.assert_elements(communityWatchlist_management.cw_last_update, communityWatchlist_management.cw_item, communityWatchlist_management.cw_performed_by)
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

    def test_resendverification_tenant(self):
        ResendVerificationTenant.open_homepage(self)
        ResendVerificationTenant.login(self)
        #self.sleep(60)

        self.click(ResendVerificationTenant.companies_button)
        self.sleep(5)
        self.click(ResendVerificationTenant.test_company)
        #self.click(ResendVerificationTenant.users_button)
        self.sleep(2)
        self.slow_click(ResendVerificationTenant.list_user)
        #self.click(ResendVerificationTenant.page3)
        #self.slow_click(ResendVerificationTenant.edit_user1)
        self.sleep(5)
        self.click(ResendVerificationTenant.resend_verification)
        self.click(ResendVerificationTenant.confirm_resend)
        self.assert_element(ResendVerificationTenant.success_notification)
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
        self.click(TransactionHistory.download_history_2)
        self.sleep(10)

class createUsercompany(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    companies_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Companies')]")
    back_button = ("//a[normalize-space()='Back']")
    logout_button = ("//a[@data-rb-event-key='/app/logout']")
    companies_button = ("//a[@data-rb-event-key='/app/companies']")
    create_company_button  = ('body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
    company_name = ("input[name='tenant_name']")
    edit_company = ("(//*[name()='svg'][@role='img'])[21]")
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

        """self.click(createUsercompany.companies_button)
        self.assert_element(createUsercompany.companies_title, createUsercompany.logout_button)
        self.slow_click(createUsercompany.edit_company)
        self.assert_element(createUsercompany.update_company_title, createUsercompany.back_button)
        self.click(createUsercompany.users_button)
        self.click(createUsercompany.create_user_company_button)

        fake = Faker()
        self.send_keys(createUsercompany.user_company_username, fake.first_name()+"@gmail.com")
        self.send_keys(createUsercompany.user_company_firstname, "Z"+fake.first_name())
        self.send_keys(createUsercompany.user_company_lastname, fake.last_name())
        self.send_keys(createUsercompany.user_company_contact_number, "012345678")
        #self.sleep(60)
        self.slow_click(createUsercompany.user_company_role)
        self.slow_click(createUsercompany.user_company_role)
        self.click_active_element()
        self.send_keys(createUsercompany.user_company_role_tenant_executive, "Tenant - Executive\n")

        #self.slow_click(createUsercompany.user_company_status)
        #self.click_active_element()
        #self.send_keys(createUsercompany.user_company_status_selection, "Inactive\n")

        self.click(createUsercompany.save_user_company_button)
        self.assert_element(createUsercompany.account_created_notification)
        self.click(createUsercompany.account_created_notification_close_button)
        
        self.assert_element(createUsercompany.update_company_title)
        self.assert_element(createUsercompany.back_button)"""

class createCompany(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    companies_title = ('body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
    back_button = ('')
    logout_button = ("a[role='button'] span:nth-child(1)")
    companies_button = ("//a[@data-rb-event-key='/app/companies']")
    create_company_button  = ("//a[normalize-space()='Create organisation']")
    company_name = ("input[name='tenant_name']")
    business_registration_number = ("input[name='business_registration_number']")
    country = ("//body/div[@id='root']/div/main/div/div/form/div[6]/div[1]/div[1]/div[1]")
    country_malaysia = ("#react-select-3-input")
    timezone = ("//body[1]/div[1]/div[1]/main[1]/div[1]/div[2]/form[1]/div[6]/div[2]/div[1]/div[1]/div[1]/div[2]")
    country_timezone = ("#react-select-4-input")
    address = ("input[name='address']")
    city = ("input[name='city']")
    postcode = ("input[name='postal_code']")
    state = ("input[name='state']")
    company_type = ("(//div[@class='select__input-container css-19bb58m'])[3]")
    company_type_selection = ("#react-select-5-input")
    payment_type = ("//body[1]/div[1]/div[1]/main[1]/div[1]/div[2]/form[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[2]")
    payment_type_selection = ("#react-select-6-input")
    credit_balance = ('')
    status_type = ("(//div[@class='select__input-container css-19bb58m'])[5]")
    status_type_selection = ("#react-select-7-input")
    create_button = ("button[type='submit']")
    company_created_notification = ("//div[@role='alert']")
    company_created_notification_close = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    companies_dashboard_url = ('https://app-testing.halocheck.com.my//companies')



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
        self.send_keys(createCompany.email_bar, var1)
        # find login bar and key in email

        self.send_keys(createCompany.password_bar, var2)
        self.click(createCompany.login_button)

class deleteAccount(BaseCase):
    homepage_title = ("halocheck")
    halocheck_logo = ("//*[@id='app']/div/div/div[1]/main/div/div/header/div/div/div/div[1]/div/div/div[3]")
    halocheck_dashboard_logo = ("//img[@alt='HaloCheck']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    email_bar = ("input[name='username']")
    email = ("sooyee.ngoi91@gmail.com")
    password_bar = ("input[name='password']")
    password = ("HCdevp@$$")
    login_bar = ("//*[@id='app']/div/div/main/div/div/div/div/div[1]/div[5]/div/button/span")
    users_button = ("//a[@data-rb-event-key='/app/users']")
    users_dashboard_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Users')]")
    back_button = ('')
    logout_button = ("a[role='button'] span:nth-child(1)")
    dashboard_url = ("https://app-testing.halocheck.com.my//users")
    entry_per_page = ("//select[@class='form-select']")
    entry_50 = ("#root > div > main > div.page-content.container-fluid > div.row.d-flex.justify-content-between > div.pagination-entries.col-12.col-sm-2.d-flex.align-items-center.mb-3 > select > option:nth-child(5)")
    second_page = ("#root > div > main > div.page-content.container-fluid > div.row.d-flex.justify-content-between > div.pagination-container.col-12.col-sm-auto.d-flex.justify-content-center.mb-3 > ul > li.page-item.active > a")
    edit_user1 = ("(//*[name()='svg'][@role='img'])[25]")
    users_management_title = ('')
    delete_button = ("//button[normalize-space()='Delete']")
    confirm_delete_account_notification = ("//body/div[@role='dialog']/div/div/div[1]")
    enter_password_confirmation_bar = ('')
    confirm_delete_account = ("//button[normalize-space()='Confirm']")
    account_deleted_notification = ("//span[contains(text(),'Successfully deleted')]")
    page3 = ("(//a[normalize-space()='3'])[1]")

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
        self.send_keys(deleteAccount.email_bar, var1)
        # find login bar and key in email

        self.send_keys(deleteAccount.password_bar, var2)
        self.click(deleteAccount.login_button)
        self.sleep(2)

class AdverseMediaCategory(BaseCase):
    homepage_title = ("halocheck")
    halocheck_logo = ("//*[@id='app']/div/div/div[1]/main/div/div/header/div/div/div/div[1]/div/div/div[3]")
    halocheck_dashboard_logo = ("a[title='HaloCheck'] img[alt='HaloCheck']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    email_bar = ("input[name='username']")
    email = ("sooyee.ngoi91@gmail.com")
    password_bar = ("input[name='password']")
    password = ("HCdevp@$$")
    login_bar = ("//*[@id='app']/div/div/main/div/div/div/div/div[1]/div[5]/div/button/span")
    users_button = ("//a[@data-rb-event-key='/app/users']")
    users_dashboard_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Users')]")
    back_button = ("//a[normalize-space()='Back']")
    logout_button = ("//a[@data-rb-event-key='/app/logout']")
    reset_password_button = ("(//button[normalize-space()='Reset Password'])[1]")
    reset_password_notification = ("//body/div[@role='dialog']/div/div[1]")
    confirm_reset_password_button = ("//button[normalize-space()='Confirm']")
    successfuly_resend_notification = ("//span[contains(text(),'Successfully re-sent verification email to')]")
    close_alert = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    dashboard_url = ("https://app-testing.halocheck.com.my//users")
    edit_user1 = ("(//*[name()='svg'][@role='img'])[14]")
    second_page = ("//a[@aria-label='Page 2']")
    entry_per_page = ("//select[@class='form-select']")
    entry_50 = ("#root > div > main > div.page-content.container-fluid > div.row.d-flex.justify-content-between > div.pagination-entries.col-12.col-sm-2.d-flex.align-items-center.mb-3 > select > option:nth-child(5)")
    resend_verification_users_page = ("(//*[name()='svg'][@role='img'])[16]")
    resend_verification_edit_users_page = ("(//button[normalize-space()='Resend Verification Link'])[1]")
    success_notification = ("div[role='alert']")
    update_user_title = ("//span[normalize-space()='Update User']")
    settings_button = ("//span[normalize-space()='Settings']")
    adverse_media_button = ("//a[@data-rb-event-key='/app/setting/adversemedia']")
    number = ("(//th[normalize-space()='No.'])[1]")
    category = ("(//th[normalize-space()='Category'])[1]")
    last_category_to_be_deleted = ("(//*[name()='svg'][@role='img'])[15]")
    datacategory_button = ("//button[normalize-space()='Data Category']")
    settings_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Settings')]")
    adverse_media_title = ("(//span[contains(text(),'Adverse Media')])[3]")
    add_category_button = ("(//button[normalize-space()='Category'])[1]")
    add_category_notification = ("//body/div[@role='dialog']/div/div[1]")
    delete_category_notification = ("//body/div[@role='dialog']/div/div[1]")
    confirm_add_adverse_media_category = ("//button[normalize-space()='Confirm']")
    cancel_add_adverse_media_category = ("//button[normalize-space()='Cancel']")
    adverse_media_category_name_bar = ("//input[@name='categoryName']")
    confirm_delete_adverse_media_category = ("//button[normalize-space()='Confirm']")
    cancel_delete_adverse_media_category = ("//button[normalize-space()='Cancel']")
    delete_adverse_media_category_success_notification = ("//div[@role='alert']")
    close_delete_adverse_media_category_success_notification_button = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    last_page = ("(//a[normalize-space()='8'])[1]")
    delete_category_zz = ("(//*[name()='svg'][@role='img'])[17]")
    delete_category_notification = ("//body/div[@role='dialog']/div/div[1]")
    confirm_delete_category_button = ("//button[normalize-space()='Confirm']")
    cancel_delete_category_button = ("//button[normalize-space()='Cancel']")
    

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
        self.send_keys(AdverseMediaCategory.email_bar, var1)
        # find login bar and key in email

        self.send_keys(AdverseMediaCategory.password_bar, var2)
        self.click(AdverseMediaCategory.login_button)
        self.sleep(2)

class DataCategory(BaseCase):
    homepage_title = ("halocheck")
    halocheck_logo = ("//*[@id='app']/div/div/div[1]/main/div/div/header/div/div/div/div[1]/div/div/div[3]")
    halocheck_dashboard_logo = ("a[title='HaloCheck'] img[alt='HaloCheck']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    email_bar = ("input[name='username']")
    email = ("sooyee.ngoi91@gmail.com")
    password_bar = ("input[name='password']")
    password = ("HCdevp@$$")
    login_bar = ("//*[@id='app']/div/div/main/div/div/div/div/div[1]/div[5]/div/button/span")
    users_button = ("//a[@data-rb-event-key='/app/users']")
    users_dashboard_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Users')]")
    back_button = ("//a[normalize-space()='Back']")
    logout_button = ("//a[@data-rb-event-key='/app/logout']")
    reset_password_button = ("(//button[normalize-space()='Reset Password'])[1]")
    reset_password_notification = ("//body/div[@role='dialog']/div/div[1]")
    confirm_reset_password_button = ("//button[normalize-space()='Confirm']")
    successfuly_resend_notification = ("//span[contains(text(),'Successfully re-sent verification email to')]")
    close_alert = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    dashboard_url = ("https://app-testing.halocheck.com.my//users")
    edit_user1 = ("(//*[name()='svg'][@role='img'])[14]")
    second_page = ("//a[@aria-label='Page 2']")
    entry_per_page = ("//select[@class='form-select']")
    entry_50 = ("#root > div > main > div.page-content.container-fluid > div.row.d-flex.justify-content-between > div.pagination-entries.col-12.col-sm-2.d-flex.align-items-center.mb-3 > select > option:nth-child(5)")
    resend_verification_users_page = ("(//*[name()='svg'][@role='img'])[16]")
    resend_verification_edit_users_page = ("(//button[normalize-space()='Resend Verification Link'])[1]")
    success_notification = ("div[role='alert']")
    update_user_title = ("//span[normalize-space()='Update User']")
    settings_button = ("//span[normalize-space()='Settings']")
    general_button = ("//a[@data-rb-event-key='/app/setting/general']")
    datacategory_button = ("//button[normalize-space()='Data Category']")
    settings_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Settings')]")
    add_category_button = ("//body//div//div[@role='tabpanel']//div//div//div//button[1]")
    add_category_notification = ("//body/div[@role='dialog']/div/div[1]")
    data_category_name_bar = ("//input[@name='categoryName']")
    confirm_add_data_category = ("//button[normalize-space()='Confirm']")
    cancel_add_data_category = ("//button[normalize-space()='Cancel']")
    data_category_success_notification = ("//div[@role='alert']")
    close_data_category_success_notification_button = ("//button[@class='btn btn-link']//*[name()='svg']")
    last_page = ("(//a[normalize-space()='22'])[1]")
    delete_category_zz = ("(//*[name()='svg'][@role='img'])[13]")
    delete_category_notification = ("//body/div[@role='dialog']/div/div[1]")
    confirm_delete_category_button = ("//button[normalize-space()='Confirm']")
    cancel_delete_category_button = ("//button[normalize-space()='Cancel']")
    last_page_2 = ("//a[@aria-label='Page 2']")

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
        self.send_keys(DataCategory.email_bar, var1)
        # find login bar and key in email

        self.send_keys(DataCategory.password_bar, var2)
        self.click(DataCategory.login_button)
        self.sleep(2)

class Type(BaseCase):
    homepage_title = ("halocheck")
    halocheck_logo = ("//*[@id='app']/div/div/div[1]/main/div/div/header/div/div/div/div[1]/div/div/div[3]")
    halocheck_dashboard_logo = ("a[title='HaloCheck'] img[alt='HaloCheck']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    email_bar = ("input[name='username']")
    email = ("sooyee.ngoi91@gmail.com")
    password_bar = ("input[name='password']")
    password = ("HCdevp@$$")
    login_bar = ("//*[@id='app']/div/div/main/div/div/div/div/div[1]/div[5]/div/button/span")
    users_button = ("//a[@data-rb-event-key='/app/users']")
    users_dashboard_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Users')]")
    back_button = ("//a[normalize-space()='Back']")
    logout_button = ("//a[@data-rb-event-key='/app/logout']")
    reset_password_button = ("(//button[normalize-space()='Reset Password'])[1]")
    reset_password_notification = ("//body/div[@role='dialog']/div/div[1]")
    confirm_reset_password_button = ("//button[normalize-space()='Confirm']")
    successfuly_resend_notification = ("//span[contains(text(),'Successfully re-sent verification email to')]")
    close_alert = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    dashboard_url = ("https://app-testing.halocheck.com.my//users")
    edit_user1 = ("(//*[name()='svg'][@role='img'])[14]")
    second_page = ("//a[@aria-label='Page 2']")
    entry_per_page = ("//select[@class='form-select']")
    entry_50 = ("#root > div > main > div.page-content.container-fluid > div.row.d-flex.justify-content-between > div.pagination-entries.col-12.col-sm-2.d-flex.align-items-center.mb-3 > select > option:nth-child(5)")
    resend_verification_users_page = ("(//*[name()='svg'][@role='img'])[16]")
    resend_verification_edit_users_page = ("(//button[normalize-space()='Resend Verification Link'])[1]")
    success_notification = ("div[role='alert']")
    update_user_title = ("//span[normalize-space()='Update User']")
    settings_button = ("//span[normalize-space()='Settings']")
    general_button = ("//a[@data-rb-event-key='/app/setting/general']")
    datacategory_button = ("//button[normalize-space()='Data Category']")
    settings_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Settings')]")
    add_type_button = (".btn-secondary")
    add_type_notification = ("//body/div[@role='dialog']/div/div[1]")
    type_name_bar = ("(//input[@name='typeName'])[1]")
    confirm_add_data_category = ("//button[normalize-space()='Confirm']")
    cancel_add_data_category = ("//button[normalize-space()='Cancel']")
    data_category_success_notification = ("//div[@role='alert']")
    close_data_category_success_notification_button = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    last_page = ("(//a[normalize-space()='22'])[1]")
    delete_type_zz = ("(//*[name()='svg'][@role='img'])[17]")
    delete_category_notification = ("//body/div[@role='dialog']/div/div[1]")
    confirm_delete_category_button = ("//button[normalize-space()='Confirm']")
    cancel_delete_category_button = ("//button[normalize-space()='Cancel']")
    last_page_2 = ("(//a[normalize-space()='15'])[1]")

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
        self.send_keys(Type.email_bar, var1)
        # find login bar and key in email

        self.send_keys(Type.password_bar, var2)
        self.click(Type.login_button)
        self.sleep(2)

class SingleRiskCheckCW(BaseCase):
    halocheck_logo = ("//a[@title='HaloCheck']//img[@alt='HaloCheck']")
    home_button = ("//a[@data-rb-event-key='/app/home']")
    search_button = ("//a[@data-rb-event-key='/app/search']")
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
    category_1 = ("input[value='1'][name='category']")
    category_2 = ("input[value='2'][name='category']")
    category_3 = ("input[value='4']")
    category_4 = ("input[value='3'][name='category']")
    category_5 = ("input[value='5']")
    community_reference_database = ("")
    single_risk_check_database = ("")
    community_reference_tab = ("")

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
    download_result_1 = ("(//*[name()='svg'][@role='img'])[13]")
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

class DeleteTenantUser(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    companies_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Companies')]")
    back_button = ("//a[normalize-space()='Back']")
    logout_button = ("//a[@data-rb-event-key='/app/logout']")
    companies_button = ("//a[@data-rb-event-key='/app/companies']")
    create_company_button  = ('body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
    company_name = ("input[name='tenant_name']")
    edit_company = ("(//*[name()='svg'][@role='img'])[21]")
    users_button = ("//button[normalize-space()='Users']")
    update_company_title = ("//span[@class='hero-title']")
    edit_user = ("(//*[name()='svg'][@role='img'])[25]")
    delete_user = ("//button[normalize-space()='Delete']")
    delete_user_confirmation = ("//body/div[@role='dialog']/div/div[1]")
    delete_user_confirm_button = ("//button[normalize-space()='Confirm']")
    delete_user_notification = ("//div[@role='alert']")
    delete_user_notification_close_button = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
   


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

class TopupDeductCredit(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    companies_title = ('body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
    back_button = ('')
    logout_button = ("a[role='button'] span:nth-child(1)")
    companies_button = ("//span[normalize-space()='Organisation']")
    create_company_button  = ('body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
    company_name = ("input[name='tenant_name']")
    business_registration_number = ("input[name='business_registration_number']")
    country = ("body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > form:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
    country_malaysia = ("#react-select-2-input")
    timezone = ("body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > form:nth-child(1) > div:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
    country_timezone = ("#react-select-3-input")
    address = ("input[name='address']")
    city = ("input[name='city']")
    postcode = ("input[name='postal_code']")
    state = ("input[name='state']")
    company_type = ("body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > form:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
    company_type_selection = ("#react-select-4-input")
    payment_type = ("body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > form:nth-child(1) > div:nth-child(8) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
    payment_type_selection = ("#react-select-5-input")
    credit_balance = ('')
    status_type = ("body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > form:nth-child(1) > div:nth-child(9) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
    status_type_selection = ("#react-select-6-input")
    create_button = ("button[type='submit']")
    notification = ("//div[@role='alert']")
    notification_close = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    companies_dashboard_url = ('https://app-testing.halocheck.com.my//companies')
    edit_company = ("(//*[name()='svg'][@role='img'])[13]")
    topup_button = ("//button[@class='credit-add btn btn-primary']//*[name()='svg']")
    deduct_button = ("//button[@class='credit-subtract btn btn-primary']//*[name()='svg']")
    amount_credit = ("//input[@placeholder='No. of credits']")
    amount_credit2 = ("(//input[@placeholder='No. of credits'])[1]")
    confirm_button = ("//button[normalize-space()='Confirm']")
    cancel_button = ("//button[normalize-space()='Cancel']")
    topuo_popup = ("//body/div[@role='dialog']/div/div[1]")
    deduct_popup = ("//body/div[@role='dialog']/div/div[1]")
    hide_search_button = ("//span[normalize-space()='Search']")

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
        self.send_keys(TopupDeductCredit.email_bar, var1)
        # find login bar and key in email

        self.send_keys(TopupDeductCredit.password_bar, var2)
        self.click(TopupDeductCredit.login_button)

class TransferWithdrawCredit2(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    companies_title = ('#root > div > aside > div > div.sidebar-menu-body > div > a:nth-child(8) > span')
    back_button = ("//a[normalize-space()='Back']")
    logout_button = ("a[role='button'] span:nth-child(1)")
    companies_button = ("//span[normalize-space()='Organisation']")
    jessica = ("(//*[name()='svg'][@role='img'])[21]")
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
    hide_search_button = ("//span[normalize-space()='Search']")
    
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

class createUser(BaseCase):
    homepage_title = ("halocheck")
    halocheck_logo = ("//*[@id='app']/div/div/div[1]/main/div/div/header/div/div/div/div[1]/div/div/div[3]")
    halocheck_dashboard_logo = ("a[title='HaloCheck'] img[alt='HaloCheck']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
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

class DeleteCompany(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    companies_title = ('body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
    back_button = ('')
    logout_button = ("a[role='button'] span:nth-child(1)")
    companies_button = ("//a[@data-rb-event-key='/app/companies']")
    create_company_button  = ('body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
    company_name = ("input[name='tenant_name']")
    business_registration_number = ("input[name='business_registration_number']")
    country = ("body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > form:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
    country_malaysia = ("#react-select-2-input")
    timezone = ("body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > form:nth-child(1) > div:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
    country_timezone = ("#react-select-3-input")
    address = ("input[name='address']")
    city = ("input[name='city']")
    postcode = ("input[name='postal_code']")
    state = ("input[name='state']")
    company_type = ("body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > form:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
    company_type_selection = ("#react-select-4-input")
    payment_type = ("body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > form:nth-child(1) > div:nth-child(8) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
    payment_type_selection = ("#react-select-5-input")
    credit_balance = ('')
    status_type = ("body > div:nth-child(2) > div:nth-child(1) > main:nth-child(4) > div:nth-child(2) > form:nth-child(1) > div:nth-child(9) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
    status_type_selection = ("#react-select-6-input")
    create_button = ("button[type='submit']")
    company_created_notification = ("//div[@role='alert']")
    company_created_notification_close = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    companies_dashboard_url = ('https://app-testing.halocheck.com.my//companies')
    edit_company = ("(//*[name()='svg'][@role='img'])[11]")
    delete_company = ("//button[normalize-space()='Delete']")
    confirm_delete_company = ("//button[normalize-space()='Confirm']")
    scroll_last_page = ("//a[@aria-label='Page 3']")




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
        self.send_keys(createCompany.email_bar, var1)
        # find login bar and key in email

        self.send_keys(createCompany.password_bar, var2)
        self.click(createCompany.login_button)

class InternalBulkCheck(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
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

class resetPassword(BaseCase):
    homepage_title = ("halocheck")
    halocheck_logo = ("//*[@id='app']/div/div/div[1]/main/div/div/header/div/div/div/div[1]/div/div/div[3]")
    halocheck_dashboard_logo = ("a[title='HaloCheck'] img[alt='HaloCheck']")
    login_button = ("//button[@name='action']")
    email_bar = ("input[name='username']")
    email = ("sooyee.ngoi91@gmail.com")
    password_bar = ("input[name='password']")
    password = ("HCdevp@$$")
    login_bar = ("//*[@id='app']/div/div/main/div/div/div/div/div[1]/div[5]/div/button/span")
    users_button = ("//a[@data-rb-event-key='/app/users']//span[contains(text(),'Users')]")
    users_dashboard_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Users')]")
    page_2 = ("//a[@aria-label='Next page']")
    back_button = ("//a[normalize-space()='Back']")
    logout_button = ("//a[@data-rb-event-key='/app/logout']")
    reset_password_button = ("//button[normalize-space()='Reset Password']")
    reset_password_notification = ("//body/div[@role='dialog']/div/div[1]")
    confirm_reset_password_button = ("//button[normalize-space()='Confirm']")
    successfuly_resend_notification = ("//span[contains(text(),'Successfully re-sent verification email to')]")
    close_alert = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    dashboard_url = ("https://app-testing.halocheck.com.my//users")
    edit_user1 = ("(//*[name()='svg'][@role='img'])[12]")
    second_page = ("//a[@aria-label='Page 2']")
    entry_per_page = ("//select[@class='form-select']")
    entry_50 = ("#root > div > main > div.page-content.container-fluid > div.row.d-flex.justify-content-between > div.pagination-entries.col-12.col-sm-2.d-flex.align-items-center.mb-3 > select > option:nth-child(5)")
    resend_verification_users_page = ("(//*[name()='svg'][@role='img'])[16]")
    resend_verification_edit_users_page = ("(//button[normalize-space()='Resend Verification Link'])[1]")
    success_notification = ("div[role='alert']")
    update_user_title = ("//span[normalize-space()='Update User']")


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
        self.send_keys(InternalBulkCheck.email_bar, var1)
        # find login bar and key in email
        self.send_keys(InternalBulkCheck.password_bar, var2)
        self.click(InternalBulkCheck.login_button)

class resendVerification(BaseCase):
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
    logout_button = ("a[role='button'] span:nth-child(1)")
    resend_verification_button = ("//button[normalize-space()='Resend Verification Link']")
    resend_account_verification_notification = ("//body/div[@role='dialog']/div/div/div[1]")
    confirm_resend_account_verification_button = ("//button[normalize-space()='Confirm']")
    successfuly_resend_notification = ("//span[contains(text(),'Successfully re-sent verification email to')]")
    close_alert = ("(//*[name()='svg'][@data-icon='xmark'])[1]")
    dashboard_url = ("https://app-testing.halocheck.com.my//users")
    edit_user1 = ("//tbody/tr[1]/td[6]/a[1]//*[name()='svg']")
    second_page = ("//a[@aria-label='Page 2']")
    entry_per_page = ("//select[@class='form-select']")
    entry_50 = ("#root > div > main > div.page-content.container-fluid > div.row.d-flex.justify-content-between > div.pagination-entries.col-12.col-sm-2.d-flex.align-items-center.mb-3 > select > option:nth-child(5)")
    resend_verification_users_page = ('//*[@id="root"]/div/main/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[7]/td[5]/span/a/svg')
    resend_verification_edit_users_page = ("(//button[normalize-space()='Resend Verification Link'])[1]")
    success_notification = ("div[role='alert']")

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
        self.send_keys(InternalBulkCheck.email_bar, var1)
        # find login bar and key in email
        self.send_keys(InternalBulkCheck.password_bar, var2)
        self.click(InternalBulkCheck.login_button)

class communityWatchlist_upload(BaseCase):
    homepage_title = ("halocheck")
    halocheck_logo = ("//*[@id='app']/div/div/div[1]/main/div/div/header/div/div/div/div[1]/div/div/div[3]")
    halocheck_dashboard_logo = ("a[title='HaloCheck'] img[alt='HaloCheck']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
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
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    email_bar = ("input[name='username']")
    email = ("sooyee.ngoi91@gmail.com")
    password_bar = ("input[name='password']")
    password = ("HCdevp@$$")
    login_bar = ("//*[@id='app']/div/div/main/div/div/div/div/div[1]/div[5]/div/button/span")
    users_button = ("//a[@data-rb-event-key='/app/users']")
    users_dashboard_title = ("//body//div//div//main//div//div//div//span[contains(text(),'Users')]")
    back_button = ("//a[normalize-space()='Back']")
    cw_sidebutton = ("//span[normalize-space()='Community Reference']")
    cw_management = ("//a[@class='sidebar-menu-nav-link']//span[@class='sidebar-menu-nav-title'][normalize-space()='Management']")
    cw_management_filter =("//button[contains(@class,'btn btn-outline-dark')]")
    filter_org = ("//body/div[contains(@role,'dialog')]/div[contains(@class,'modal-dialog modal-dialog-centered')]/div[contains(@class,'modal-content')]/div[contains(@class,'modal-body')]/div[contains(@class,'accordion')]/div[1]/div[1]")
    filter_org_selection = ("#react-select-3-input")
    filter_status = ("(//div[contains(@class,'accordion-header d-flex justify-content-between')])[3]")
    filter_status_selection = ("//input[@value='1']")
    cw_filter_apply_filter = ("//button[normalize-space()='Apply filter']")
    cw_filter_all_user = ("")
    cw_filter_company = ("")
    cw_filter_all_company = ("")
    cw_case_1 = ("(//*[name()='svg'][@role='img'])[13]")
    cw_case_2 = ("")
    cw_status = ("(//div[@class='select__input-container css-19bb58m'])[1]")
    cw_status_active = ("#react-select-4-input")
    cw_status_inactive = ("")
    cw_status_expiring = ("")
    cw_status_retired = ("")
    cw_status_expired = ("")
    cw_case_save_button = ("//button[@type='submit']")
    cw_history_tab = ("(//button[normalize-space()='History'])[1]")
    cw_last_update = ("(//th[normalize-space()='Last Update'])[1]")
    cw_item = ("(//th[normalize-space()='Item'])[1]")
    cw_performed_by = ("(//th[normalize-space()='Performed By'])[1]")



    
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

class ResendVerificationTenant(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
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
    resend_verification = ("(//*[name()='svg'][@role='img'])[13]")
    confirm_resend = ("//button[normalize-space()='Confirm']")
    success_notification = ("(//div[@role='alert'])[1]")
    test_company = ("(//*[name()='svg'][@role='img'])[21]")

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
        self.send_keys(ResendVerificationTenant.email_bar, var1)
        # find login bar and key in email

        self.send_keys(ResendVerificationTenant.password_bar, var2)
        self.click(ResendVerificationTenant.login_button)

class TransactionHistory(BaseCase):
    email_bar = ("input[name='username']")
    password_bar = ("input[name='password']")
    login_button = ("(//button[@name='action'][normalize-space()='Log In'])[2]")
    transaction_history_sidebar = ("//span[normalize-space()='Transaction History']")
    transaction_history_checks_sidebar =("//span[normalize-space()='Checks']")
    transaction_history_credits_sidebar = ("//span[normalize-space()='Credits']")
    top_date = ("//th[normalize-space()='Date']")
    top_subject = ("//th[normalize-space()='Subject']")
    top_type = ("//th[normalize-space()='Type']")
    top_credit = ("//th[normalize-space()='Credit']")
    top_user = ("//th[normalize-space()='User']")
    top_report = ("//th[normalize-space()='Report']")
    download_checks_1 = ("(//*[name()='svg'][@role='img'])[13]")
    history_tab = ("(//a[normalize-space()='History'])[1]")
    top_period = ("//th[normalize-space()='Period']")
    top_credit_used = ("//th[normalize-space()='Total Credit Used']")
    top_history = ("//th[normalize-space()='History']")
    download_history_1 = ("//tbody/tr[1]/td[3]/a[1]//*[name()='svg']")
    top_category = ("//th[normalize-space()='Category']")
    top_credits = ("//th[normalize-space()='Credits']")
    top_description = ("//th[normalize-space()='Description']")
    top_performed_by = ("//th[normalize-space()='Performed By']")
    download_history_2 = ("//tbody/tr[1]/td[2]/a[1]//*[name()='svg']")
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