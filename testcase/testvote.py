# -*- coding:utf-8 -*-
import xlrd
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath



testdata=xlrd.open_workbook(GetTestDataPath())



testurl="http://127.0.0.1:8000"
def post_vote():
    try:
        table = testdata.sheets()[1]
        for i in range(3,5):
            choice=table.cell(i,0).value
            status=table.cell(i,1).value
            qiwang = table.cell(i, 2).value
            hdata={
                'choice':int(choice)
            }
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid="1-1"
            testname="testvote"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestPostRequest(testurl+'/polls/1/vote/',hdata,header,testcaseid,testname,testhope,fanhuitesthpe)
    except Exception as e:
        print(e)
# post_vote()

def get_polls():
    try:
        table = testdata.sheets()[1]
        for i in range(13,14):
            status = table.cell(i, 0).value
            qiwang = table.cell(i, 1).value
            hdata=""
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid="1-1"
            testname="testpolls"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest(testurl+'/polls/1/',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,"status")
    except Exception as e:
        print(e)

# get_polls()

def get_demo():
    try:
        hdata = {'key': '00d91e8e0cca2b76f515926a36db68f5','phone': '13594347817','passwd': '123654'}
        header = {
            "content-type": "application/json;charset=utf-8"
        }
        testcaseid="1-1"
        testname="testdemo"+testcaseid
        testhope='202'
        fanhuitesthpe="用户已注册"
        r=TestGetRequest("https://www.apiopen.top/createUser",hdata,header,testcaseid,testname,testhope,fanhuitesthpe,'code')
    except Exception as e:
        print(e)

# get_demo()

def get_login():
    try:
        table = testdata.sheets()[2]
        for i in range(3,5):
            key = table.cell(i, 0).value
            print(key)
            phone = table.cell(i, 1).value
            phone=str(int(phone))
            pwd = table.cell(i, 2).value
            pwd = str(int(pwd ))
            status = table.cell(i, 3).value
            qiwang = table.cell(i, 4).value
            hdata = {'key': key,'phone':phone ,'passwd': pwd}
            # hdata = {
            #     "key": "00d91e8e0cca2b76f515926a36db68f5",
            #     "phone'": "13594347817",
            #     "passwd": "123654"
            # }
            header = {
                "content-type": "application/json;charset=utf-8"
            }
            testcaseid="1-2"
            testname="testdemo"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest("https://www.apiopen.top/login",hdata,header,testcaseid,testname,testhope,fanhuitesthpe,'code')
    except Exception as e:
        print(e)

# get_login()