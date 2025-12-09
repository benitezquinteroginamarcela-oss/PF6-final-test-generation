import json
import requests
response = requests.get("https://api-colombia.com/api/v1/TypicalDish")
Typical_disks =response.json()
input("Ingresa un numero, para ver un plato tipico:")
for Typical_disk in Typical_disks:
  print (Typical_disk["name"])
  print (Typical_disk["description"])
  print ("*"*60)
