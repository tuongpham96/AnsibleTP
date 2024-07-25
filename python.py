#Test
import requests
import json
import urllib3
urllib3.disable_warnings()

url = "https://10.99.255.163/restapi/v10.2/Policies/SecurityRules?location=vsys&vsys=vsys1&name=TuongPham"

payload = json.dumps({
  "entry": {
    "@name": "TuongPham",
    "to": {
      "member": [
        "any"
      ]
    },
    "from": {
      "member": [
        "any"
      ]
    },
    "source": {
      "member": [
        "any"
      ]
    },
    "destination": {
      "member": [
        "any"
      ]
    },
    "source-user": {
      "member": [
        "any"
      ]
    },
    "category": {
      "member": [
        "any"
      ]
    },
    "application": {
      "member": [
        "any"
      ]
    },
    "service": {
      "member": [
        "any"
      ]
    },
    "action": "drop"
  }
})
headers = {
  'X-PAN-KEY': 'LUFRPT1OWGVVWENmWGNTN3ZvRUFHcXJzMFhQRHY4QUE9MkEzM3lDRzVYWkFmSW5Jd0JIdzFuVEFiWU02T1ErQXJjRFAvSnZoM29WQ0VZL3hCaGMya3NZWk41Umg5djFveQ==',
  'Content-Type': 'application/json',
  'Cookie': 'PHPSESSID=7kjjtn6qfv77pb0eesbp4g3gnt'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print("TrungTa")
