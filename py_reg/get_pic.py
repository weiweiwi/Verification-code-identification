# -*- coding:utf-8 -*-
import requests
import os

code_url = 'https://cd.abiz.com/validcode'  # 验证码URL



def getImg(val,localPath):
    if(not os.path.exists(localPath)):
        os.mkdir(localPath)

    for i in range(val,10000) :
        ir=requests.get(code_url+'?t='+str(i))
        str1=localPath+'%d.jpg'%i
        print(str1)
        open(str1 ,'wb').write(ir.content)

if __name__=='__main__':

    getImg(1000,'e:/pic/')


