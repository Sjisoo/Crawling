import requests
import json

url = "http://www.melon.com/search/keyword/index.json"
params = {
    'jscallback' : 'jQuery19102372467943089951_1511402165434',
    'query' : '빅뱅',
}
response = requests.get(url, params=params).text
json_string = response.replace(params['jscallback'] + '(','').replace(');','')
result_dict = json.loads(json_string)

print(result_dict)

for song in result_dict['ALBUMCONTENTS']:
    print(song['ALBUMNAME'])