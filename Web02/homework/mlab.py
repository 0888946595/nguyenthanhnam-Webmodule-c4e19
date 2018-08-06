import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds135966.mlab.com:35966/warmwinter

host = "ds135966.mlab.com"
port = 35966
db_name = "warmwinter"
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