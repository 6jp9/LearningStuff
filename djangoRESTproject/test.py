# To sent request form a test py file to a django project
import io
import requests,json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'
def get_data(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    res = requests.get(BASE_URL+END_POINT , json.dumps(data))
    print(res.status_code)
    print(res.json())
get_data(2)
