import random
from datetime import date, timedelta

data = {
    '广州': 'https://hotel.qunar.com/cn/guangzhou/?fromDate=2020-09-15&toDate=2020-09-16&cityName=%E5%B9%BF%E5%B7%9E',
    '深圳': 'https://hotel.qunar.com/cn/shenzhen/?fromDate=2020-09-15&toDate=2020-09-16&cityName=%E6%B7%B1%E5%9C%B3',
    '珠海': 'https://hotel.qunar.com/cn/zhuhai/?fromDate=2020-09-15&toDate=2020-09-16&cityName=%E7%8F%A0%E6%B5%B7',
    '佛山': 'https://hotel.qunar.com/cn/foshan/?fromDate=2020-09-15&toDate=2020-09-16&cityName=%E4%BD%9B%E5%B1%B1',
    '东莞': 'https://hotel.qunar.com/cn/dongguan/?fromDate=2020-09-15&toDate=2020-09-16&cityName=%E4%B8%9C%E8%8E%9E'
}

def random_city():
    chengshi = ['广州', '深圳', '珠海', '佛山', '东莞']
    return random.choice(chengshi)

def random_date(): #获取随机日期并添加进网址上
    today = date.today()
    a =str(today)
    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    b = str(tomorrow)
    return a, b

def url(city, today, tomorrow):
    if city == '广州':
        url1 = "https://hotel.qunar.com/cn/guangzhou/?fromDate=" + today + "&toDate=" + tomorrow + "&cityName=%E5%B9%BF%E5%B7%9E"
    elif city == '深圳':
        url1 = "https://hotel.qunar.com/cn/shenzhen/?fromDate=" + today + "&toDate=" + tomorrow + "&cityName=%E6%B7%B1%E5%9C%B3"
    elif city == '珠海':
        url1 = "https://hotel.qunar.com/cn/zhuhai/?fromDate=" + today + "&toDate=" + tomorrow + "&cityName=%E7%8F%A0%E6%B5%B7"
    elif city == '佛山':
        url1 = "https://hotel.qunar.com/cn/foshan/?fromDate=" + today + "&toDate=" + tomorrow + "&cityName=%E4%BD%9B%E5%B1%B1"
    else:
        url1 = "https://hotel.qunar.com/cn/dongguan/?fromDate=" + today + "&toDate=" + tomorrow + "&cityName=%E4%B8%9C%E8%8E%9E"
    return url1

def start():
    city = random_city()
    today, tomorrow = random_date()
    city_url = url(city, today, tomorrow)
    return city, city_url

if __name__ == '__main__':
    start()