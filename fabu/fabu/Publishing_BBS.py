import  requests
import re
se = requests.session()
from .wyc import wyc




def Publishing(title,content):
    get_url = 'http://www.75hb.com/bbs/forum.php?mod=post&action=newthread&fid=52'

    headers = {

        'cookie': '_uab_collina=152055279119608995114701; province=6; city=76; district=0; street=1; street_area=1; session_id_ip=222.209.249.172_00e3590d01df4b7e5a877a2642efa676; __jsluid=d91e0c874f50e352637feb170a5906ad; bdshare_firstime=1520081890016; Z41o_2132_saltkey=ldLeap5o; Z41o_2132_lastvisit=1520549183; Z41o_2132_nofavfid=1; ECS[history]=29248%2C33570%2C32991%2C33139%2C17764; ECS[list_history]=29248%2C33570%2C32991%2C33139%2C17764; ECS[visit_times]=6; Hm_lvt_d37804ec3d9bfa562610cdb6525fadd5=1520301475,1520554570,1520578696,1520907896; Z41o_2132_pc_size_c=0; Z41o_2132_atarget=1; Z41o_2132_st_t=0%7C1521010448%7C218e12c1aef258a9f4a863f54265c728; Z41o_2132_forum_lastvisit=D_49_1521010352D_48_1521010448; Z41o_2132_visitedfid=48D49D42D2; Z41o_2132_viewid=tid_5285; _umdata=85957DF9A4B3B3E8DBA9C4A6E17667D825936BAEF541F67C7B990512A4D628D2C6AE598D998DA8D2CD43AD3E795C914C549833D2A57F6B94B3A2B3AD6BE8B6B8; Z41o_2132_ulastactivity=c01eqXIB74dGby9YUKQ6fhPa%2FnbUCVIR3dH056g9KdAyz84GeH0i; Z41o_2132_auth=2687AruCv2F2uoQub5SVQygFJRhp7G0syHaJgWG2m9DPy6xBV2wXrGGXK8oBNL6H1x5a44QiTg0P%2B7xg5TFV; Z41o_2132_st_p=1%7C1521010539%7C5aeb1292b3db5073da161dcd00345a95; Z41o_2132_addoncheck_plugin=1; Z41o_2132_sid=fP2etZ; Z41o_2132_lip=222.209.250.115%2C1521010538; Z41o_2132_onlineusernum=8; Z41o_2132_checkpm=1; Z41o_2132_sendmail=1; Z41o_2132_lastcheckfeed=1%7C1521015351; Z41o_2132_checkfollow=1; Z41o_2132_lastact=1521015351%09misc.php%09patch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Host': 'www.75hb.com',

    }

    se.headers.clear()
    se.headers.update(headers)
    str = se.get(get_url).text

    hash1 = 'id="formhash" value="'
    hash2 = '" />'
    time1 = 'id="posttime" value="'
    time2 = '" />'

    hs = re.compile(hash1+"(.*?)"+hash2,re.S)
    ti = re.compile(time1+"(.*?)"+time2,re.S)



    fromhash = re.findall(hs,str)[0]
    posttime = re.findall(ti,str)[0]

    print(fromhash,posttime)


    wy_content = wyc(content)




    data = {
        'formhash':fromhash,
        'posttime':posttime,
        'wysiwyg':'1',
        'subject':title,
        'message':wy_content,
        'replycredit_extcredits':'0',
        'replycredit_times':'1',
        'replycredit_membertimes':'1',
        'replycredit_random':'100',
        'readperm':'',
        'price':'',
        'tags':'',
        'rushreplyfrom':'',
        'rushreplyto':'',
        'rewardfloor':'',
        'replylimit':'',
        'stopfloor':'',
        'creditlimit':'',
        'allownoticeauthor':'1',
        'usesig':'1',
        'htmlon':'1',
        'save':'',
        'mygroupid':'',
        'uploadalbum':'1',
        'newalbum':'请输入相册名称',

    }

    se.headers.clear()
    se.headers.update(headers)
    post_url = "http://www.75hb.com/bbs/forum.php?mod=post&action=newthread&fid=52&extra=&topicsubmit=yes"
    string = se.post(post_url,data=data).text

    if title in string:
        link1 = '<link href="'
        link2 = '" rel="canonical"'
        lk = re.compile(link1+"(.*?)"+link2,re.S)
    try:
        link = re.findall(lk,string)[0]
        print("当前link的值为:"+link)
    except IndexError:
        print('当前帖子已发布,正在切换下一个帖子')

    else:
        bd_url = '	http://data.zz.baidu.com/urls?site=www.75hb.com&token=EDUEd4qfULX3yGnV'
        headers = {

            'User-Agent': 'curl/7.12.1',
            'Host': 'data.zz.baidu.com',
            'Content-Type': 'text/plain',
            'Content-Length': '83',

        }
        se.headers.clear()
        se.headers.update(headers)
        bd_str = se.post(bd_url, data=link).text
        print('发布成功')
        return '发布成功'

