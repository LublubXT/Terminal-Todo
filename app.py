import json

list = {
    'items': [{
            'id': 0,
            'text': 'Todo',
            'complete': False
        },
        {
            'id': 1,
            'text': 'Welcome to your Todo!',
            'complete': False
        },
        {
            'id': 2,
            'text': 'I want to delete this item',
            'complete': True
        },
        {
            'id': 3,
            'text': 'Hello World',
            'complete': False
        },
        {
            'id': 4,
            'text': 'I want to delete this item',
            'complete': False
        }
    ]
}  

for item in list['items']:
    if str(item['complete']) == str(True):
        print("Found Item to Delete")
        print(list['items'].pop(int(item['id'])))


print(json.dumps(list['items'], indent=2))