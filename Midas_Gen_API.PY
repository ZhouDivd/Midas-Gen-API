import requests
import json
import math
import winreg
import sys
"""自动获取注册表中的midas_api_key和URL, 当自动获取失败时,在GH电池内输入key和url运行电池则在当前文件夹生成一个txt文件,
内含key和url供使用,相当于手动获取"""
def getapikey():
    try:
        reg=winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
        #读取注册表中的值
        reg_key=winreg.OpenKey(reg,r'Software\MIDAS\midasGen_CH\CONNECTION')
        #查询注册表中的值
        midas_api_keyvalue=winreg.QueryValueEx(reg_key,'Key')[0]
        #apiurl="https://"+winreg.QueryValueEx(reg_key,'URI')[0]+":443/gen"
        #关闭注册表
        winreg.CloseKey(reg_key)
        winreg.CloseKey(reg)
    except:
            with open(r"C:\GH_CPython\key.txt",'r') as file:
                midas_api_keyvalue=file.readline()
                
    return midas_api_keyvalue
def getapiurl():
    try:
        reg=winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
        #读取注册表中的值
        reg_key=winreg.OpenKey(reg,r'Software\MIDAS\midasGen_CH\CONNECTION')
        #查询注册表中的值
        apiurl="https://"+winreg.QueryValueEx(reg_key,'URI')[0]+":443/gen"
        #关闭注册表
        winreg.CloseKey(reg_key)
        winreg.CloseKey(reg)
    except:
            with open(r"C:\GH_CPython\url.txt",'r') as file:
                apiurl=file.readline()
                
    return apiurl

def midas_api(method, command, body=None):
    base_url =  getapiurl()
    url = base_url + command
    midas_api_key = getapikey()
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
