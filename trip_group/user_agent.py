import urllib.request
import lxml.html
import json
import random
import time
import useragenttool


class ip_agent(object):
    def __init__(self):
        self.url = ['https://www.kuaidaili.com/free/inha/1/',
                    'https://www.kuaidaili.com/free/inha/2/',
                    'https://www.kuaidaili.com/free/inha/3/',
                    'https://www.kuaidaili.com/free/inha/4/',
                    'https://www.kuaidaili.com/free/inha/5/']

    # 保存爬取的IP代理地址到json文件中
    def save_ip_agent_json(self):
        f = open("./ip_agent.json", "w", encoding='utf-8')
        result = []
        for i in self.url:
            obj = urllib.request.Request(i, headers=useragenttool.get_headers())
            response = urllib.request.urlopen(obj)
            html = response.read().decode('utf-8')
            # print(html)
            metree = lxml.html.etree
            parser = metree.HTML(html)
            ip_list = parser.xpath("//table[@class='table table-bordered table-striped']/tbody/tr")
            # print(ip_list)

            for item in ip_list:
                dist = {}
                tds = item.xpath("./td/text()")
                aggrement_name = tds[3]
                ip_address = tds[3].lower() + "://" + tds[0] + ":" + tds[1]
                dist[aggrement_name] = ip_address
                result.append(dist)
            time.sleep(3)

            # print(result)
        result_1 = json.dumps(result, indent=2, ensure_ascii=False)
        # print(result_1)
        # print(result)
        # print(type(result))
        # return result
        f.write(result_1)

    '''
        def get_random_ip_agent(self, datas):
        index = random.randint(0, len(datas) - 1)
        print(type(datas[index]))
        print(datas[index])
        return datas[index]
    '''

    def start(self):
        data = self.save_ip_agent_json()
        # ip = self.get_random_ip_agent(data)



def main():
    Ip_agent = ip_agent()
    Ip_agent.start()

if __name__ == '__main__':
    main()