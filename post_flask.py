import requests
import base64

f = open("cat.png", "br")
img = f.read()
img = base64.b64encode(img)
d = {}
d["img"] = img

r = requests.post("http://localhost:5000/", data=d)
print(r.status_code)
print(r.text)