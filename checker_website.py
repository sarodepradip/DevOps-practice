import requests
url = "https://google.com"


response = requests.get(url)

if response.status_code == 200:
    print("website is UP")
else:
    print("website is DOWN")
    
    
    
    