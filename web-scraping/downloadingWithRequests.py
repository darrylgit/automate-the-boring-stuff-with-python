import requests
import os

os.chdir('/home/daniel/Coding/automate-the-boring-stuff/web-scraping')

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
# print(res.status_code)

res.raise_for_status()

outputFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(10000):
    outputFile.write(chunk)

outputFile.close()
