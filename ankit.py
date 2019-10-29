import requests

headers = {
    'accept': 'application/json',
    'X-API-KEY': 'uo3PinMdsi6dU8dAGhYQRc4DLKm7GviL',
    'X-APP-ID': '03b7c993-cdc8-4b70-86db-51ea94e0cf77',
}

response = requests.get('https://api.capenetworks.com/v1/nodes', headers=headers)
print response