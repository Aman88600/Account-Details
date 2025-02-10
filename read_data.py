import json

def get_data():
    file = open('data.json', 'r')
    data = json.load(file)
    file.close()
    return data

if __name__ == '__main__':
    data = get_data()
    print(data)