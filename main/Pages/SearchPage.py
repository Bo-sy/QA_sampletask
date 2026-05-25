from playwright.sync_api import Page

from main.Pages.BasePage import BasePage
from main.Pages.RepositoryPage import RepositoryPage


class SearchResultPage(BasePage):

    def __init__(self, page: Page) -> None:
        self.page = page

    def get_repository_page_by_string(self, search_text: str) -> 'RepositoryPage':
        locator_xpath = f"//span[contains(text(),'{search_text}')]"
        self.page.locator(locator_xpath).click()

        return RepositoryPage(self.page)