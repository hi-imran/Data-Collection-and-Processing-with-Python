import requests_with_caching
import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params = parameters,permanent_cache_file="itunes_cache.txt")

py_data = json.loads(iTunes_response.text)