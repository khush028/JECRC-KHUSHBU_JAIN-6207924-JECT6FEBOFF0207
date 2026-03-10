import pickle

file = open('temp.txt', 'wb+')   

data = {
    'fullname': 'Khushbu Jain',
    'userid': 123444,
    'password': '*****'
}

pickle.dumps(data, file)

file.seek(0)

ori_data = pickle.loads(file)

print(ori_data, type(ori_data))

file.close()