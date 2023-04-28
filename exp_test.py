import pytest
from playwright.sync_api import Page, expect



def test_youtube_search_using_keyword_and_check_if_results_match_with_search_keyword_and_print_1st_10_videos(page: Page):
    page.goto("https://www.youtube.com")
    search_keyword= 'Coding'



    # create a locator
    get_started = page.get_by_placeholder("Search")
    get_started.click()
    get_started.fill(search_keyword)
    get_started.press("Enter")
    page.wait_for_timeout(8000)
    print(page.url)

    found_elements = page.locator('a#video-title')
    print(found_elements.count())
    for i in range(10):
        print(found_elements.nth(i).get_attribute('href'))
        print(found_elements.nth(i).all_text_contents())
        if found_elements.nth(i).get_attribute('title').lower().__contains__(search_keyword.lower()):
            print(f"{i+1} is match")
        else:
            print(f"{i+1} is not match")
















