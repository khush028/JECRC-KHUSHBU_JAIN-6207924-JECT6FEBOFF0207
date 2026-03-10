# dumps() : Encryption 
# laods () : Decryption

'''
1. JSON,
2. PICKLE ,
'''

import json 
file = open('temp.txt' , 'a+')
data = {
    'fullname' : 'Khushbu Jain', 
    'userid' : 123444,
    'password' : '*****'
}

enc_data = json.dumps(data)
file.write(enc_data)
file.seek(0)
enc_data = file.read()
print(type(enc_data))

ori_data = json.loads(enc_data)
print(ori_data , type(ori_data))
# print(f'Original data : {data}')
# print(f'Type of original data : {type(data)}')
# enc_data = json.dumps(data)
# print(f'Encrypted data : {enc_data}')
# print(f'Type of Encrypted data : {type(enc_data)}')
# dec_data = json.loads(enc_data)
# print(f'Decrypted data : {dec_data}')
# print(f'Type of decrypted data : {type(dec_data)}')
