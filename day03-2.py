# 代理
# http
# import requests
# proxies = {
#     "http":"http://127.0.0.1:1080",
#     "https":"https://127.0.0.1:1080",
# }
# response = requests.get("https://www.taobao.com",proxies=proxies)
# print(response.status_code)

# socks
import requests
proxies = {
    "http":"socks5://127.0.0.1:1080",
    "https":"socks5://127.0.0.1:1080",
}
response = requests.get("https://www.taobao.com",proxies=proxies)
print(response.status_code)