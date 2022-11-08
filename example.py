import requests

url = "https://image-captcha-solver-daddy.p.rapidapi.com/solve"

with open('captcha1.jpeg', 'rb') as f:
    payload = f.read()

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "your_RapidApi_Key",
	"X-RapidAPI-Host": "image-captcha-solver-daddy.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
