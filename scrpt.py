#import
import requests
import schedule
import time
import logging

#logging format
logging.basicConfig(
    level=logging.INFO,
    format="{asctime} - {levelname} - {message}",
    filename="scrpt.log",
    encoding="utf-8",
    filemode="w",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

# request
def request(web_address):
#check if website is up
    try:
        res = requests.get(web_address, timeout=7)  # Wait max 7 seconds
        print(f"[OK] {web_address} is UP — Status: {res.status_code}")
        logging.info(f"[OK] {web_address} is UP — Status: {res.status_code}")
        # print(f"[OK] {web_address} is UP — Status: {res.status_code}")
    except requests.exceptions.Timeout:
         logging.error(f" {web_address} timed out — didn't respond in 7 seconds")
        # print(f" {web_address} timed out — didn't respond in 5 seconds")
    except requests.exceptions.RequestException as e:
        logging.warning(f" {web_address} timed out — didn't respond in 7 seconds")
        # print(f" {web_address} is DOWN — Error: {e}")

#auto clear scrpt.log
def auto_clear_log():
    try:
        open("scrpt.log", "w").close()
        # print("[OK] [Auto] Log cleared at", time.strftime("%Y-%m-%d %H:%M:%S"))
        logging.info("[Auto] Log cleared.")
    except Exception as e:
        # print(f"Failed to auto-clear log: {e}")
        logging.error(f" Auto-clear failed: {e}")



#read websites from file
def readfile():
    with open('web_address.txt', 'r') as f:
            web_address_list = [item for line in f.read().splitlines() for item in line.split(' ') if item != '']
            for each_website in web_address_list:
                request(each_website)
              
#schedule to run read txt and clear log
schedule.every(5).minutes.do(readfile)
schedule.every(1).hours.do(auto_clear_log)

while True:
    schedule.run_pending()
    time.sleep(1)

#I plan to work on sending email alongside to logging