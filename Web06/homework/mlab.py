import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds115472.mlab.com:15472/cms-c4e19-app

host = "ds115472.mlab.com"
port = 15472
db_name = "cms-c4e19-app"
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