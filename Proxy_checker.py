import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []

# Assuming you have a proxies.txt file with IP:PORT format
# For demo, we insert a sample format
proxies_list = ["185.199.229.156:7492", "198.23.238.245:1024"] 

for p in proxies_list:
    q.put(p)

def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("https://httpbin.org/ip", 
                               proxies={"http": proxy, "https": proxy}, 
                               timeout=5)
        except:
            continue
        if res.status_code == 200:
            print(f"FOUND VALID PROXY: {proxy}")
            valid_proxies.append(proxy)

# Using 2 threads for fast checking
for _ in range(2):
    t = threading.Thread(target=check_proxies)
    t.start()
