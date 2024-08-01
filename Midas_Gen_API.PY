import requests
import json
import math
import winreg
#自动获取注册表中的midas_api_key
#打开注册表
reg=winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
#读取注册表中的值
reg_key=winreg.OpenKey(reg,r'Software\MIDAS\midasGen_CH\CONNECTION')
#查询注册表中的值
midas_api_keyvalue=winreg.QueryValueEx(reg_key,'Key')[0]
def midas_api(method, command, body=None):
    base_url = 'https://moa-engineers.midasit.cn:443/gen'
    url = base_url + command
    midas_api_key = midas_api_keyvalue
    headers = {'Content-Type': 'application/json'
       , "MAPI-KEY": midas_api_key,}
    if method == 'POST':
        response = requests.post(url=url, headers=headers, json=body)
    elif method == 'GET':
        response = requests.get(url=url, headers=headers)
    elif method == 'PUT':
        response = requests.put(url=url, headers=headers, json=body)
    elif method == 'DELETE':
        response = requests.delete(url=url, headers=headers)
    print(method,command, response.status_code)
    
    return response.json()