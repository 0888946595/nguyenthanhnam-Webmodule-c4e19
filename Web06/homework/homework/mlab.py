import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds245277.mlab.com:45277/muadongkhonglanh

host = "ds245277.mlab.com"
port = 45277
db_name = "muadongkhonglanh"
user_name = "admin"
password = "thanhnam123"



def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())