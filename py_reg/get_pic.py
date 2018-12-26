# -*- coding:utf-8 -*-
import requests
import os

code_url = 'http://202.193.80.58:81/academic/getCaptcha.do?0.23611265529353553'  # 验证码URL


def getImg(val,localPath):
    if(not os.path.exists(localPath)):
        os.mkdir(localPath)
    for i in range(val,10000) :
        ir=requests.get(code_url)
        str1=localPath+'%d.jpg'%i
        print(str1)
        print(ir.content)
        open(str1 ,'wb').write(ir.content)

if __name__=='__main__':
   getImg(1,'C:/Users/dell/Desktop/Verification-code-identification/pic/')


