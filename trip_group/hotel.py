from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import lxml.html
import get_city

path = r"./chromedriver.exe"
driver = webdriver.Chrome(path)
city, url = get_city.start()
driver.get(url)
time.sleep(1)

metree = lxml.html.etree
parser = metree.HTML(driver.page_source)

result = []
head = ["城市", "酒店名", "价格", "评分", "地址", "网址"]
items = parser.xpath('//div[@class="inner clearfix"]')
for i in range(4):
    for item in items:
        hotel = item.xpath(".//div[@class='cont']/p[@class='name']/a/text()")[0]
        price = item.xpath('.//div[@class="operate fl_right"]/p[@class="price_new"]/a/text()')[0]
        grade = item.xpath(".//div[@class='cont']/p[@class='comm']/span[@class='num']/text()")[0]
        address = item.xpath(".//div[@class='cont']/p[@class='adress']/text()")[0]
        hotel_url = "https://hotel.qunar.com" + item.xpath(".//div[@class='cont']/p[@class='name']/a/@href")[0]
        data = [city, hotel, price, grade, address, hotel_url]
        result.append(data)
    print(str(i+2))
    time.sleep(5)
    driver.find_element_by_xpath("//a[@class='item cur']/following-sibling::a[1]").click()
result.insert(0, head)
print(result)
print(len(result))
