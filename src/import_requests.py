import requests
import json
import os

COOKIE_FILE = 'leetcode_cookies.json'

def save_cookies(cookies):
    with open(COOKIE_FILE, 'w') as f:
        json.dump(cookies, f)

def load_cookies():
    if os.path.exists(COOKIE_FILE):
        with open(COOKIE_FILE, 'r') as f:
            return json.load(f)
    return {}

def authenticate():
    session_cookie = input("Enter your LEETCODE_SESSION cookie: ")
    csrf_token = input("Enter your csrftoken cookie: ")

    cookies = {
        'LEETCODE_SESSION': session_cookie,
        'csrftoken': csrf_token
    }
    save_cookies(cookies)

def get_submissions(offset=0, limit=30):
    url = f"https://leetcode.com/api/submissions/?offset={offset}&limit={limit}"
    cookies = load_cookies()
    if not cookies:
        print("No cookies found. Please authenticate.")
        authenticate()
        cookies = load_cookies()
    
    response = requests.get(url, cookies=cookies, headers={'referer': 'https://leetcode.com', 'origin': 'https://leetcode.com'})
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 403:
        print("Session expired. Please authenticate again.")
        authenticate()
        cookies = load_cookies()
        response = requests.get(url, cookies=cookies, headers={'referer': 'https://leetcode.com', 'origin': 'https://leetcode.com'})
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
            return None
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None
