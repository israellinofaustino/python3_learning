import requests
try:
    website = requests.get('https://google.com')
    print(f"I was able to access Google successfully! => CODE:{website.status_code}") # return a int value
except:
    print(f"Google is currently not accessible!")
