from seleniumbase import BaseCase


class RecorderTests(BaseCase):
    def test_recording(self):
        self.open("https://app-testing.halocheck.com.my/index.html/#/app/search/singlecheck")
        self.open("https://app-testing.halocheck.com.my/?code=DSYPkE9jCdQK9WJqoKKWX80n1qVVnOlMeOlLgAoHQpr8F&state=S1hLU3NZamhYNHNCSkNvcWVVM25VZDFfaFBIRmppN1daT1lwVUNDcjRVYg==#/app/search/singlecheck")
        self.click("div#root aside div:nth-of-type(2) div:nth-of-type(3) span")
        self.click('a[href="#/app/communitywatchlist/upload"] span')
        self.click('a[href="#/app/communitywatchlist/upload/single"] div')
        self.type('input[name="subject_name"]', "asdasdasdas")
        self.type('input[name="subject_id"]', "12312312321")
        self.click("div#root main div:nth-of-type(2) form div:nth-of-type(3) div div div:nth-of-type(2)")
        self.type("input#react-select-3-input", "malay")
        self.click("div#root main div:nth-of-type(2) form div:nth-of-type(4) div div div:nth-of-type(2)")
        self.click("div#root > div > main > div > div:nth-of-type(2) > div > form > div:nth-of-type(4) > div:nth-of-type(2) > input")
        self.select_option_by_text("div.modal-body div:nth-of-type(2) span span select", "April")
        self.select_option_by_text("div.modal-body div:nth-of-type(2) span span:nth-of-type(3) select", "2019")
        self.click("div.modal-body div:nth-of-type(3) div:nth-of-type(2) button:nth-of-type(5)")
        self.click('button:contains("Confirm")')
        self.click('button:contains("Submit")')
        self.click('button:contains("Cancel")')
