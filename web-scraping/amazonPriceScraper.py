import bs4
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

res = requests.get(
    'https://www.amazon.com/Automate-Boring-Stuff-Python-2nd-ebook/dp/B07VSXS4NK', headers=headers)

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
soup2 = bs4.BeautifulSoup(soup.prettify(), "html.parser")

elems = soup.select(
    '#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')


print(elems)
print(elems[0].text.strip())
