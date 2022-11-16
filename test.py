import requests
import json
from bs4 import BeautifulSoup

https = '178.32.116.64:3128'
proxies = {
    'http': https,
    'https': https,
}
headers = {
    "User-Agent": "Opera/9.80 (X11; Linux x86_64; U; de) Presto/2.2.15 Version/10.00"}
try:
    out = requests.get('https://ipinfo.io/', proxies=proxies, timeout=3,)
    result = json.dumps(out.json(), indent=3)
    print(result)
    page = requests.get("https://www.1tamilmv.cfd",
                        proxies=proxies, timeout=3,)
    bs = BeautifulSoup(page.content, 'html.parser')
    f = open("demofile3.html", "w")
    f.write(bs.prettify())
    f.close()
except Exception as err:
    print(err)
