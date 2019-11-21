import requests
import base64

f = open("d.png", "br")
img = f.read()
img = base64.b64encode(img)
d = {}
d["img"] = img

#r = requests.post("https://q-draw.herokuapp.com/", data=d)
r = requests.post("http://localhost:5000/", data=d)
print(r.status_code)
print(r.text)
