from seleniumbase import BaseCase


class RecorderTests(BaseCase):
    def test_recording(self):
        self.open("https://app-testing.halocheck.com.my/index.html#/app/search/singlecheck")
        self.open("https://app-testing.halocheck.com.my/?code=-k-blt3ds10_t5-uGmoYfFAE0kFnWq1LsiLe_7hYrJLRz&state=M00uZ0tINHpqdjR1NDdNMFBtZnZqUEJreHc5QjhXcFQ2dFQ5ZmxObzRZRg==#/app/search/singlecheck")
        self.click('a[href="#/app/promotions"] span')
        self.click('a[href="#/app/promotions/add"]')
        self.select_option_by_text("div.modal-body div div:nth-of-type(2) span span select", "February")
        self.select_option_by_text("div.modal-body div div:nth-of-type(2) span span:nth-of-type(3) select", "2025")
        self.click("div.modal-body div div:nth-of-type(3) div:nth-of-type(2) button:nth-of-type(7)")
        self.click("div.modal-body div div:nth-of-type(3) div:nth-of-type(2) button:nth-of-type(34)")
        self.click('button:contains("Confirm")')
        self.type('input[name="quantity"]', "1")
        self.type('input[name="redemption"]', "1")
        self.type('textarea[name="remarks"]', "1")
