import requests
import json 
from collections import Counter, defaultdict, OrderedDict
res = requests.get('https://www.tokocrypto.com/open/v1/common/symbols')
response = json.loads(res.text)
symbols = response['data']['list']


couple_count = defaultdict(int)
couple_assets = defaultdict(list)

for item in symbols:
    couple_count[item['quoteAsset']] += 1
    couple_assets[item['quoteAsset']].append(f"{item['baseAsset']}/{item['quoteAsset']}")

fa = sorted(couple_count.items(), key=lambda k_v: k_v[1], reverse=True)[:3:]


for quote, count in fa:
    print(f"quoteAsset: {quote}, count: {count} \n list: {couple_assets.get(quote)} ")
