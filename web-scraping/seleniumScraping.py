from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector(
    '.main > ul:nth-child(16) > li:nth-child(1) > a:nth-child(1)')

elem.click()

paragraph = browser.find_element_by_css_selector(
    '#calibre_link-1610 > p:nth-child(5)')

print(paragraph.text)
