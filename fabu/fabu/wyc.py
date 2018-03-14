import requests
import re
se = requests.session()

def wyc(content):

    headers = {

        'cookie':'JSESSIONID=24EBD9702FD8D87EBE34A25E0A88020A; UM_distinctid=1620afb3a2c191-0374dfd03c4819-3b60450b-1fa400-1620afb3a2d3dc; CNZZDATA2027872=cnzz_eid%3D860635322-1520600759-%26ntime%3D1520600759; naipanA_feixiang1799@163.com=naipanB_a83822851',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Referer':'http://www.naipan.com/',
        'Origin':'http://www.naipan.com',
        'Content-Type':'application/x-www-form-urlencoded',



    }

    se.headers.clear()
    se.headers.update(headers)

    postdate = {

        'replaceNum':'0',
        'userReplaceNum':'0',
        'webContent':content,
        'amode':'0',
        'linkWeiWord':'',
        'linkWeiUrl':'http://',
        'weiKu':'0',
        'weiMode':'0',

    }

    posturl = 'http://www.naipan.com/index.html'
    pdata = se.post(posturl,data=postdate).text

    wyc1 = 'min-width:1180px" wrap="physical">'
    wyc2 = '</textarea>'
    yc = re.compile(wyc1+'(.*?)'+wyc2,re.S)
    findyc = re.findall(yc,pdata)[0]
    print(findyc)
    return findyc
