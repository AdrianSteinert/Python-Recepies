import json
import requests

def main():
    data = {
        'username': 'james',
        'active': True,
        'subscribers': 10,
        'order_total': 39.99,
        'order_is': ['ACB123', 'QQQ433', 'LOL303'],
    }

    print(data)

    # print objects as json string
    s = json.dumps(data)
    print(s)

    # getting python object from json string
    data2 = json.loads(s)
    assert data2 == data

    # writing data to file
    with open('test_data.json', 'w') as f:
        json.dump(data, f)

    # reading data from file
    with open('test_data.json') as f:
        data3 = json.load(f)
    assert data3 == data


    r = requests.get('https://jsonplaceholder.typicode.com/users')
    print(r.json()) 


if __name__ == '__main__':
    main()