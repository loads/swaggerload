import requests
from pprint import pprint
from ops import operation


@operation
def getDownloads(verb, endpoint, **options):
    data = {"body": "mozstd-track-digest256;a:1"}
    res = requests.post(endpoint, data)
    try:
        body = res.json()
    except ValueError:
        pprint(res.content)

    assert res.status_code == 200
