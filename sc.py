from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import json
options = Options()
options.headless = True
#service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(options=options,executable_path=GeckoDriverManager().install())
#s=Service(executable_path=GeckoDriverManager().install())
#driver = webdriver.Firefox(service=s)

with open("urls.txt","r") as p:
    urls = [i.strip("\n") for i in p.readlines()]
with open('temper.txt','r') as a:
    temp = [i.strip("\n") for i in a.readlines()]

urls = [i for i in urls if i not in temp]
#final = []
for i in urls:
    print(i)
    driver.get(i)
    time.sleep(7)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source,"html.parser")
    name = soup.find("h1",{"property" : "v:name"}).text
    try:
        plugtitle = soup.find("div",{"title" : "Plug Types"}).text
    except:
        plugtitle = ""
    try:
        address = soup.find("a",{"property" : "v:address"}).text
    except:
        address = ""
    try:
        phone = soup.find("a",{"property": "v:tel"}).text
    except:
        phone=""
    final={"name" : name, "type" : plugtitle, "address" : address, "phone" : phone,"url" : i}
    with open("first200.csv","a", encoding='utf-8') as wa:
        wa.write(";".join(final.values())+"\n")
    with open('temper.txt','a') as wp:
        wp.write(i+"\n")
    print({"name" : name, "type" : plugtitle, "address" : address, "phone" : phone,"url" : i})
    #break
#df = pd.DataFrame(final)
#df.to_csv("final.csv",sep=';')
