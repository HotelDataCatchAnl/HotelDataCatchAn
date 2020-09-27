import json
import random


with open("./ip_agent.json", "r", encoding='utf-8') as f:
    data = json.load(f)
    # print(data)
    # print(type(data))

def get_random_ip():
    index = random.randint(0, len(data) - 1)
    print(type(data[index]))
    print(data[index])
    return data[index]


if __name__ == '__main__':
    ip_agent = get_random_ip()