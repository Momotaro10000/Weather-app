import requests

# url = 'http://wttr.in/san%20francisco?nTqu&lang=en'
locations = ['London', 'svo', 'Череповец']
url_template = 'http://wttr.in/{}?n?mTqu&lang=ru'
for location in locations:
    url = url_template.format(location)
    response = requests.get(url)
    print(response.text)