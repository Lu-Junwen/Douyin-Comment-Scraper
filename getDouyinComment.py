import requests
import json
import time

def transTime(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

#懒得看csv操作，用了笨方法
def saveComments(comments, resultFile):
    if not comments or len(comments)==0:
        return
    with open(resultFile,'a') as fp:
        for item in comments:
            fp.write(str(item['create_time']))
            fp.write(',')
            if 'ip_label' in item:
                fp.write(item['ip_label'])
            else:
                fp.write('未知')
            fp.write(',"')
            fp.write(item['text'].replace('\n',' ').replace('"','""'))
            fp.write('","')
            fp.write(item['user']['nickname'].replace('"','""'))
            fp.write('","')
            fp.write(item['user']['signature'].replace('\n',' ').replace('"','""').strip())
            fp.write('"\r\n')

urlComment="https://www.douyin.com/aweme/v1/web/comment/list/"

urlList="https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_general&sort_type=0&publish_time=0&keyword=AI%E6%BC%AB%E7%94%BB%E7%85%A7%E7%89%87%E7%94%9F%E6%88%90&search_source=search_history&query_correct_type=1&is_filter_search=0&from_group_id=&offset=0&count=15&pc_client_type=1&version_code=190600&version_name=19.6.0&cookie_enabled=true&screen_width=1512&screen_height=982&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7336886543707293211&msToken=DwJcw3KziIJQ3wHZaHjcvxnF7jNSdWV5ZF8A1g702o9g1wV069qHKJbL96oRcqbBHcjg3MSgfj1P6iIcuiA83YCJY6anEE8muS171d83-5D1hF8Y84M9Ta_zyeaP6g==&X-Bogus=DFSzswVYVj0ANc2EtbvppDLNKBTy"

resultFile="CommentData"

statisticalDataFile="statisticalDataFile"

headerList = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie':'',#Fill in your Cookie
    'Referer':'https://www.douyin.com/search/%E4%B8%8A%E6%B5%B7%E8%BF%AA%E5%A3%AB%E5%B0%BC?aid=f64e041e-de27-4b15-ac02-32371d2f73a5&publish_time=0&sort_type=0&source=search_sug&type=general',
    'Sec-Ch-Ua':'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"macOS"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

paramList = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'search_channel': 'aweme_general',
    'sort_type': '0',
    'publish_time': '0',
    'keyword': '',
    'search_source': 'search_sug',
    'query_correct_type': '1',
    'is_filter_search': '0',
    'from_group_id': '',
    'offset': '',
    'count': '15',
    'pc_client_type': '1',
    'version_code': '190600',
    'version_name': '19.6.0',
    'cookie_enabled': 'true',
    'screen_width': '1512',
    'screen_height': '982',
    'browser_language': 'zh-CN',
    'browser_platform': 'MacIntel',
    'browser_name': 'Chrome',
    'browser_version': '122.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '122.0.0.0',
    'os_name': 'Mac OS',
    'os_version': '10.15.7',
    'cpu_core_num': '10',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '50',
    'webid': '7336886543707293211',
    'msToken': 'PYgcBguavepAybnCAQSxcwpOeh-L-tVjWDjIIQdgJWgjdI6HUwrQ4m9ALpKSZSpMqpmGCElLp75nPauMb8XEkcKrrcQgcMlY9KbQCLtXRARfRDnlIL07Ij7HT_XQnA==',
    'X-Bogus': 'DFSzswVOU5sANGyItbvgoDLNKBOl',
}

headerComment = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,es-MX;q=0.6,es;q=0.5',
    'cookie': '',#Fill in your Cookie
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAlfFujj6wKxN1TqrqqJu4XBaZqek6XwvvA_afAojNvWr1E4ZO_nadPC1Ku7XMpzfj?modal_id=7316808340519030055',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

paramComment = {
        'device_platform': 'webapp', 
        'aid': '6383',
        'channel': 'channel_pc_web',
        'aweme_id': '',
        'cursor': '0',
        'count': '20',
        'item_type': '0',
        'insert_ids': '',
        'whale_cut_token': '',
        'cut_version': '1',
        'rcFT': '',
        'pc_client_type': '1',
        'version_code': '170400',
        'version_name': '17.4.0',
        'cookie_enabled': 'true',
        'screen_width': '1512',
        'screen_height': '982',
        'browser_language': 'zh-CN',
        'browser_platform': 'MacIntel',
        'browser_name': 'Chrome',
        'browser_version': '122.0.0.0',
        'browser_online': 'true',
        'engine_name': 'Blink',
        'engine_version': '122.0.0.0',
        'os_name': 'Mac OS',
        'os_version': '10.15.7',
        'cpu_core_num': '10',
        'device_memory': '8',
        'platform': 'PC',
        'downlink': '0.65',
        'effective_type': '4g',
        'round_trip_time': '150',
        'webid': '7336886543707293211',
        'msToken': 'ynBEzZt8-ldeY6wwpzl405oYAmP1FKuxiAaZnMedfqbO1sPbxhL_CXd-EEQwiN1sCYwsUUkDV6Lu5Ml65uDGyFnkHlNgaXvl4CvGkvGaBbaL10xC4BiuoF5v0-1U',
        'X-Bogus': 'DFSzswVu2jhANjA3toyEsDLNKBPI'
    }

idList=set()


def getComment(id,endFile):
    paramComment['aweme_id']=id
    while True:
        r=requests.get(url=urlComment,params=paramComment,headers=headerComment)
        
        if not r.ok:
            print(r)
            print("Bad!")
            exit()
        
        comments=r.json().get('comments', None)
        saveComments(comments,endFile)
        if 'has_more' not in r.json():
            break
        if not r.json()['has_more']:
            break
        paramComment['cursor']=str(int(paramComment['cursor'])+int(paramComment['count']))
        
def getList(s,list,num):
    paramList['keyword']=s
    paramList['offset']='0'
    while len(list)<num:
        r=requests.get(url=urlList,headers=headerList)

        if not r.ok:
            print(r)
            print("Can't open the link!")
            exit()
        
        searchResult=r.json()['data']
        
        for item in searchResult:
            if 'aweme_info' not in item:
                continue
            list.add(item['aweme_info']['aweme_id'])
        
        if not r.json()['has_more']:
            break
        
        paramList['offset']=str(int(paramList['count'])+int(paramList['offset']))
        
getList('',idList,15) #Fill in keyword in the first parameter.
with open("idList.txt",'w') as fp:
    for id in idList:
        fp.write(str(id))
        fp.write('\n')
        getComment(id,resultFile)