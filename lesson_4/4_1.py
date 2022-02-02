import requests
import utils

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
res = utils.cur_cut(input("Введите валюту:").upper(),str(response.content))

if res is not None:
  print(float(res))
else:
    print(res)
