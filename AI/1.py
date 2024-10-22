import requests, json 


url = "http://127.0.0.1:5000/convert"
data = {
    "num1" : "456"
}
response = requests.post(url=url,json = data)
result = response.json()
print(result["result"])