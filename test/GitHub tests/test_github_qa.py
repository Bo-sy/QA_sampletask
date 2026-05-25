import pytest
from main.Pages.MainPage import MainPage

EXPECTED_TEXT_IN_README = "CopilotKit"


@pytest.fixture
def main_page():
    page = MainPage()
    yield page

def test_check_content_in_readme(main_page: MainPage):
    search_result_page = main_page.search_by_text("copilot")
    repository_page = search_result_page.get_repository_page_by_string("CopilotKit")

    actual_text = repository_page.get_text_from_readme()

    assert actual_text == EXPECTED_TEXT_IN_README, \
        f"Assert that text in Readme.md equal {EXPECTED_TEXT_IN_README}"