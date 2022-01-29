import requests
import utils
from sys import argv

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

res = utils.cur_cut(str(argv[1].upper()),str(response.content))
print(argv)
if res is not None:
  print(float(res))
else:
    print(res)
