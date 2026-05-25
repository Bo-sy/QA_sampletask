from main.Pages.BasePage import BasePage
from main.Pages.SearchPage import SearchResultPage


class MainPage(BasePage):

    def __init__(self) -> None:
        self.search_input = self.page.locator("//input[@id='query-builder-test']")
        self.search_button = self.page.locator("//button[contains(@class, 'search')]")
        self.page.goto("https://github.com/")

    def search_by_text(self, text: str) -> 'SearchResultPage':
        self.search_button.click()
        self.search_input.fill(text)
        self.search_input.press("Enter")
        return SearchResultPage(self.page)