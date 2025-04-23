import requests
import time
from fake_useragent import UserAgent

URL = "https://www.amazon.in/s?k=laptop&page=3&crid=DVXBY0UNVAUE&qid=1744562873&sprefix=lapto%2Caps%2C273&xpid=HjsN6HnD5mleJ&ref=sr_pg_1"

session = requests.Session()

headers = {
    'User-Agent': UserAgent().random,
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    'Referer': 'https://www.amazon.in/',
    'sec-ch-ua-mobile': '?1', 
    'sec-ch-ua-platform': '"Android"',  
    'sec-fetch-dest': 'empty',  
    'sec-fetch-mode': 'no-cors', 
    'sec-fetch-site': 'same-site',  
}

try:
    time.sleep(2)
    r = session.get(URL, headers=headers)
    r.raise_for_status()  
    
    # Try to get the text content with proper encoding
    if r.encoding is None:
        r.encoding = 'utf-8'
    
    with open("file_amazon.html", "w", encoding="utf-8") as f:
        f.write(r.text)
    print("HTML saved successfully!")
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")