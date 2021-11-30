import requests

payload = {'key1': 'value1', 'key2': 'value2'}

#GET
#r = requests.get('http://httpbin.org/get', params=payload)
r = requests.get('http://httpbin.org/get', params=payload, timeout=1)

#Post
# r = requests.post('http://httpbin.org/post', data=payload)

# PUT
# r = requests.put('http://httpbin.org/put', data=payload)

# DELTE
# r = requests.delete('http://httpbin.org/delete', data=payload)

print(r.status_code)
print(r.text)
print(r.json())