import requests
import json
import pprint
input = raw_input('Enter Mac Address:')
url = 'https://api.macaddress.io/v1?apiKey=at_RzQ1chh7L4iVIDkC62etuhEt9POTD&output=json&search={}'.format(input)
response = requests.get(url)
data  = json.loads(response.content)
print(input)
print
pp = pprint.PrettyPrinter(indent=2)

for key in data.keys():
    print key
    for newkey in data[key].keys():
        if isinstance(data[key][newkey],list):
            
            print '{}'.format(newkey) + ':'+' Array'
            for idx,value in enumerate(data[key][newkey]):
               
               print '  {}'.format(idx)+':'+'{}'.format(value)
        else:
            out = '{}'.format(newkey)+ ':' + '{}'.format(data[key][newkey])
        print out
    print


