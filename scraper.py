from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

url = 'https://etherscan.io/advanced-filter?fadd=0x73ab2bd10ad10f7174a1ad5afae3ce3d991c5047&tadd=0x73ab2bd10ad10f7174a1ad5afae3ce3d991c5047&txntype=2&tkn=0x2260fac5e5542a773aa44fbcfedf7c193bc2c599'
req = Request(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})   # I got this line from another post since "uClient = uReq(URL)" and "page_html = uClient.read()" would not work (I beleive that etherscan is attemption to block webscraping or something?)
response = urlopen(req, timeout=20).read()
response_close = urlopen(req, timeout=20).close()
page_soup = soup(response, "html.parser")
Transfers_info_table_1 = page_soup.find("table", {"class": "table table-hover mb-0"})
print(Transfers_info_table_1)
df=pd.read_html(str(Transfers_info_table_1))[0]
df.to_csv("TransferTable.csv",index=False)

