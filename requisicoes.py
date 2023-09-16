import requests

response = requests.get('https://www.walissonsilva.com')

print ('Status code: ', response.status_code)
print ('Headers:')
print (response.headers)

print ('\n content')
print (response.content)

