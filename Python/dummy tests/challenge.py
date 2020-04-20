import requests
url="https://cryptwerk.com"

res=requests.get(url)
#Error catch method
try:
    res.raise_for_status()
except Exception as exc:
        print("There was a problem:%s'%(exc)")

type(res)
res.status_code=requests.codes.ok
#get the length
print(len(res.text))
#print exact line
print(res.text[:2300])