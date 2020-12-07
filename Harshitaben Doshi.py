import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = ("/Users/apoorvelous/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)
stars_data = []
new_stars_data = []
def scrape():
    headers = ["Name","Distance","Radius","Mass"]
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs ={"class","List_of_brightest_stars_and_other_record_stars"}):
            li_tags = ul_tag.find_all("li")
            stars_list =[]
            for index,li_tags in enumerate(li_tags):
                if index == 0:
                    stars_list.append(li_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        stars_list.append(li_tags.contents[0])
                    except:
                        stars_list.append("")
            stars_data.append(stars_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        print(f"{i} page done 1")
def scrape_more_data():
    try:
        page = requests.get(Radius)
        soup = BeautifulSoup(page.content, "html.parser")
        stars_list = []
        for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    stars_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    stars_list.append("")
        new_stars_data.append(stars_list)
    except:
        time.sleep(1)
        scrape_more_data(Radius)
scrape()

for index, data in enumerate(stars_data):
    scrape_more_data(data[5])
    print(f"{index+1} page done 2")
final_stars_data = []
for index, data in enumerate(stars_data):
    new_stars_data_element = new_stars_data[index]
    new_stars_data_element = [elem.replace("\n", "") for elem in new_stars_data_element]
    new_stars_data_element = new_stars_data_element[:7]
    final_stars_data.append(data + new_stars_data_element)
df.to_csv('hemaagam.csv')
with open('hemaagam.csv','w') as f:
    csvwriter = csv.writer(f)
    csvwriter = writerow(headers)
    csvwriter = writerows(stars_data)