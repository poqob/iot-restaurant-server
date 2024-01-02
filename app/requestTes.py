import requests

url = "http://192.168.73.100:5951/color_change"
data = {"color": '{"status": 1, "red": 255, "green": 0, "blue": 0}'}

response = requests.post(url, data=data)
print(response.text)

url1 = "http://192.168.73.100:5951/call_waiter"
data_waiter = {"desk_id": "1234567890"}
response = requests.post(url1, data=data_waiter)
print(response.text)


url2 = "http://192.168.73.100:5951/attic"
attic = {"attic": "1"}
response = requests.post(url2, data=attic)
print(response.text)

url3 = "http://192.168.73.100:5951/log"
response = requests.get(url3)
print(response.text)
