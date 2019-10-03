import requests
r=requests.get("https://financialmodelingprep.com/developer/docs/")
print(r.text)
print(r.status_code)
'''
url="www.something.com"
data={
    "p1":3,
    "a2":4
}

r2=requests.post(url=url,data=data)
print(r2.text)
'''