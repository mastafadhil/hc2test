from seleniumbase import BaseCase


class RecorderTests(BaseCase):
    def test_recording(self):
        self.open("https://app-testing.halocheck.com.my")
        self.open_if_not_url("https://app-testing.halocheck.com.my/#/app/search/singlecheck")
        self.open("https://app-testing.halocheck.com.my/?code=cb9QfdvoTl4-ByTNRKjeNj2J4RX2aRxawAxsyPNlNjPhZ&state=U1dFOUJTY0JsVW5zOVFmT1JocF9mdE00OVZUd0RmelQtMkxKVU51RGpafg==#/app/search/singlecheck")
        self.click("div#root > div > aside > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div > span")
        self.click('a[href="#/app/transactionhistory/credits"] span')
        self.click("a#react-aria8323854736-:r1:-tab-history")
        self.click('a[href="/"] svg path')
