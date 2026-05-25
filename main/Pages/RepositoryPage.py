from playwright.sync_api import Page

from main.Pages.BasePage import BasePage


class RepositoryPage(BasePage):

    def __init__(self, page: Page) -> None:
        self.page = page

    def get_text_from_readme(self) -> str | None:
        self.page.locator('(//a[@title="README.md"])[2]').click()
        return self.page.locator('//div[@class="markdown-heading"]/h1').text_content()