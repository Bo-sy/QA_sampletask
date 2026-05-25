from playwright.sync_api import sync_playwright, Playwright, Browser, Page

class BasePage:
    playwright: Playwright
    browser: Browser
    page: Page

_playwright_context_manager = sync_playwright()
BasePage.playwright = _playwright_context_manager.start()

BasePage.browser = BasePage.playwright.chromium.launch(
    headless=False,
    slow_mo=50
)
BasePage.page = BasePage.browser.new_page()