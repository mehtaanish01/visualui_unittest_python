import unittest
import sys
from selenium import webdriver
import os
import time

username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key


class FirstSampleTest(unittest.TestCase):
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        desired_caps = {
            "build": 'Blog Test',  # Change your build name here
            "name": 'Blog Test',  # Change your test name here
            "browserName": 'Chrome',
            "version": 'latest',
            "platform": 'Windows 10',
            #"fixedIP":"10.130.0.240",
            # "resolution": '1024x768', # change the resolution
            "network": 'true',  # Enable or disable network logs
            "smartUI.project": "Blog-Test1",
            # Build name for smartUI(optional)
            "smartUI.build" : "buildName01",
        }
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@beta-smartui-hub.lambdatest.com/wd/hub".format(
                username, access_key),
            desired_capabilities={"LT:Options": desired_caps})

    # tearDown runs after each test case

    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        urls = ["https://www.coupa.com/blog", "https://www.coupa.com/blog/finance-ap", "https://www.coupa.com/blog/finance-ap/how-virtual-cards-for-b2b-payments-improve-cash-flow-capture-efficiencies-and", "https://www.coupa.com/blog/treasury", "https://www.coupa.com/blog/supply-chain/unrelenting-supply-chain-disruptions-spur-supply-chain-procurement-and-finance", "https://www.coupa.com/blog/supply-chain/5-ways-prepare-for-sovereign-supply-chains", "https://www.coupa.com/blog/technology-innovation", "https://www.coupa.com/blog/procurement/what-contract-lifecycle-management-clm", "https://www.coupa.com/blog/supply-chain/what-sales-and-operations-planning-sop-and-how-it-can-benefit-your-business", "https://www.coupa.com/blog/supply-chain/complete-guide-supply-chain-digital-twins", "https://www.coupa.com/blog/finance-ap/5-payment-pain-points-and-how-solve-them", "https://www.coupa.com/blog/procurement/automate-tasks-reduce-errors-and-accelerate-integrations-coupa-and-datamap",
                "https://www.coupa.com/blog/supply-chain/gartner-names-coupa-challenger-2022-magic-quadranttm-for-supply-chain-planning", "https://www.coupa.com/blog/treasury/7-core-benefits-treasury-management-system-infographic", "https://www.coupa.com/blog/technology-innovation/it-continuity-during-pandemic", "https://www.coupa.com/blog/coupa-news/coupa-and-find-recognized-fast-company-for-world-changing-idea", "https://www.coupa.com/blog/finance-ap/why-virtual-cards-are-better-spend-management-p-cards", "https://www.coupa.com/blog/coupa-news/communityai-unites-power-spend-for-every-coupa-customer", "https://www.coupa.com/blog/procurement/what-contract-lifecycle-management-clm-coupa", "https://www.coupa.com/blog/customer-community/meet-winners-2022-emea-spendsetters-awards-for-smarter-business", "https://www.coupa.com/blog/procurement/cpo-next-ceo", "https://www.coupa.com/blog/finance-ap/empowering-ecosystem-kofax-coupa-and-future-financial-functions"]

        for url in urls:
            driver.get(url)
            time.sleep(6)
            driver.execute_script("smartui.takeScreenshot")


if __name__ == "__main__":
    unittest.main()
