from bs4 import BeautifulSoup
from openpyxl import load_workbook
from selenium import webdriver
def name2key(name):
    ind = name.find(" ")
    while ind!=-1:
        name = name[:ind]+"+"+name[ind+1:]
        ind = name.find(" ")
    return name

wb = load_workbook("Football Draft 2019.xlsx")
sheet = wb["Update"]

list = []
for i in range(460):
    name = sheet["C"+str(i+2)].value
    list.append(name)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
chrome = webdriver.Chrome(options=options,
                          executable_path="C:/Users/darre/OneDrive/桌面/Darrell/Python/chromedriver")
def crawl(url):
    chrome.set_page_load_timeout(10)
    chrome.get(url)
    soup = BeautifulSoup(chrome.page_source, 'html5lib')
    try:
        player = soup.find('a','spielprofil_tooltip tooltipstered').text
        return player
    except:
        return None

for elem in list:
    searchkey = name2key(elem)
    val = "Diff"
    url="https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query=%s&x=0&y=0"%searchkey
    if elem == crawl(url):
        pass
    else:
        print(elem,"/",crawl(url))