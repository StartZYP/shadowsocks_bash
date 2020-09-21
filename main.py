import time
import requests
from lxml import etree

def get_session(Cookies):
    Tempdit = {}
    for line in Cookies.split(';'):
        name, value = line.strip().split('=', 1)
        Tempdit[name] = value
    session.cookies = requests.utils.cookiejar_from_dict(Tempdit)


def post_sign():
    params = {
        'mod':'forumdisplay',
        'fid':'15',
        'filter':'author',
        'orderby':'dateline'
    }

    reuslt = session.get('http://www.zuanke8.com/forum.php',params=params)
    html = etree.HTML(reuslt.text)
    test = html.xpath('//*[@id="threadlisttableid"]/tbody/tr/th/a/text()')[0]
    test1 = html.xpath('//*[@id="threadlisttableid"]/tbody/tr/th/a/@href')[0]
    return test,test1
if __name__ == "__main__":
    session = requests.session()
    Cookieslist=[
        'ki1e_2132_saltkey=GZJh9pY8; ki1e_2132_lastvisit=1599443307; _uab_collina=159944692115822258193935; ki1e_2132_client_created=1599446982; ki1e_2132_client_token=88845BD6554E9DFB7004AD1A8C045912; ki1e_2132_auth=ffabEOu0PPoClU0k81M2WnAIW5Z7MOaJzsFGqMd2pp%2BCOf%2BT3kuWb4U1aE%2BTtfzxvktBBUjm04HHUhtMEcIECSjGZfI; ki1e_2132_connect_login=1; ki1e_2132_connect_is_bind=1; ki1e_2132_connect_uin=88845BD6554E9DFB7004AD1A8C045912; ki1e_2132_nofavfid=1; ki1e_2132_atarget=1; ki1e_2132_smile=1D1; Hm_lvt_da6569f688ba2c32429af00afd9eb8a1=1599446921,1599705081; ki1e_2132_home_diymode=1; ki1e_2132_clearUserdata=forum; ki1e_2132_connect_not_sync_t=1; ki1e_2132_lastviewtime=824929%7C1599720872; ki1e_2132_pc_size_c=2ecbfad; timestamp=1600334879000; sign=705FC7A98683AFC35D963904DE966440; ki1e_2132_creditnotice=0D0D0D0D0D0D0D0D0D824929; ki1e_2132_creditbase=0D1315D0D0D0D0D0D0D0; ki1e_2132_creditrule=%E5%8F%91%E8%A1%A8%E5%9B%9E%E5%A4%8D; forum_20=1; ki1e_2132_sendmail=1; ki1e_2132_viewid=tid_7456346; ki1e_2132_ulastactivity=1600412137%7C0; ki1e_2132_noticeTitle=1; ki1e_2132_lastcheckfeed=824929%7C1600412255; ki1e_2132_forum_lastvisit=D_31_1599539807D_19_1600324949D_82_1600408431D_11_1600408448D_25_1600408492D_15_1600412282; Hm_lpvt_da6569f688ba2c32429af00afd9eb8a1=1600412283; ki1e_2132_lastact=1600412283%09connect.php%09check'
    ]
    get_session(Cookieslist[0])
    title,url = post_sign()
    while True:
        time.sleep(3)
        titletmp,urltmp = post_sign()
        if title != titletmp:
            print "Title:"+titletmp
            print "url:"+urltmp
            title = titletmp
            params = {
                'appToken':'AT_xBP33IgAFegqI7kgJxyIAdvsIhOPtUMB',
                'url': urltmp,
                'content': title,
                'topicId':'805',
                'contentType': 1

            }
            requests.get('http://wxpusher.zjiecode.com/api/send/message/',params=params)
    pass
