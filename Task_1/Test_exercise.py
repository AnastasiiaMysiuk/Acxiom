import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TitleFetch(unittest.TestCase):

    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_1(self):
        self.driver.get("https://news.ycombinator.com/")
        searchItems = self.driver.find_elements(By.XPATH, "//span[@class='titleline']/a")
        for i in searchItems:
            print(i.text)

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main':
    unittest.main()