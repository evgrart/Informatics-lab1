import requests
import sys

data = {"url": f"https://github.com/{sys.argv[1]}.git", "subject": sys.argv[2], "lab_number": sys.argv[3]}
response = requests.post("http://root-hub.ru:41071/labs", json=data)
response_data = response.json()
text_message = response_data.get("text_message")

print(text_message)
