# To sent request form a test py file to a django project

import requests,json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'


# def get_resource(id=None):
#     data = {}
#     if id is not None:
#         data = {
#             'id':id
#             }
#     res = requests.get(BASE_URL + END_POINT , data = json.dumps(data))
#     print(res.status_code)
#     print(res.json())
# get_resource(2)

# def create_data():
#     new_movie = {
#         'name':'kannappa',
#         'hero':'snow',
#         'rating':10
#     }

#     res = requests.post(BASE_URL+END_POINT, data = json.dumps(new_movie))
#     print(res.status_code)
#     print(res.json())


# create_data()


# def delete_data(id):
#     dic = {
#         'id': id
#     }
#     res = requests.delete(BASE_URL+END_POINT,data= json.dumps(dic))
#     print(res.status_code)
#     print(res.json())

# delete_data(4)

def update_data(id):
    new_dir = {
        'id':id,
        
        'rating':10,
    }
    res = requests.put(BASE_URL + END_POINT, data=json.dumps(new_dir))
    print(res.status_code)
    print(res.json())

update_data(3)
