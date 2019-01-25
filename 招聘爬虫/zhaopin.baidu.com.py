"""
1. 学习目标
    1.1  
"""
import requests
import json
import urllib
from multiprocessing import Process, Queue, Pool, Manager


def main():
    # 统计java
    args = [
        {'query': 'java', 'city': urllib.parse.quote("成都"), 'city_zm': 'cd'},
        {'query': 'java', 'city': urllib.parse.quote("重庆"), 'city_zm': 'cq'},
        {'query': 'java', 'city': urllib.parse.quote("武汉"), 'city_zm': 'wh'},
        {'query': 'java', 'city': urllib.parse.quote("北京"), 'city_zm': 'bj'},
        {'query': 'java', 'city': urllib.parse.quote("上海"), 'city_zm': 'sh'},
        {'query': 'java', 'city': urllib.parse.quote("广州"), 'city_zm': 'gz'},
        {'query': 'java', 'city': urllib.parse.quote("深圳"), 'city_zm': 'sz'}
    ]

    m = Manager()
    java_result = m.dict()
    java_result["xueke"] = "java"
    p = Pool()
    for arg in args:
        params = {'query': arg['query'], 'city': arg['city'], 'date': '20181017_20181024', 'city_zm': arg['city_zm']}
        p.apply_async(getdispNum, args=(params, java_result))
    p.close()
    p.join()

    print(java_result)

    # # 统计php
    # args = [
    #     {'query': 'php', 'city': urllib.parse.quote("成都"), 'city_zm': 'cd'},
    #     {'query': 'php', 'city': urllib.parse.quote("重庆"), 'city_zm': 'cq'},
    #     {'query': 'php', 'city': urllib.parse.quote("武汉"), 'city_zm': 'wh'},
    #     {'query': 'php', 'city': urllib.parse.quote("北京"), 'city_zm': 'bj'},
    #     {'query': 'php', 'city': urllib.parse.quote("上海"), 'city_zm': 'sh'},
    #     {'query': 'php', 'city': urllib.parse.quote("广州"), 'city_zm': 'gz'},
    #     {'query': 'php', 'city': urllib.parse.quote("深圳"), 'city_zm': 'sz'}
    # ]
    #
    # php_result = m.dict()
    # php_result["xueke"] = "PHP"
    # p = Pool()
    # for arg in args:
    #     params = {'query': arg['query'], 'city': arg['city'], 'date': '20181013_20181020', 'city_zm': arg['city_zm']}
    #     p.apply_async(getdispNum, args=(params, php_result))
    # p.close()
    # p.join()
    #
    # # 统计ui
    # args = [
    #     {'query': 'UI', 'city': urllib.parse.quote("成都"), 'city_zm': 'cd'},
    #     {'query': 'UI', 'city': urllib.parse.quote("重庆"), 'city_zm': 'cq'},
    #     {'query': 'UI', 'city': urllib.parse.quote("武汉"), 'city_zm': 'wh'},
    #     {'query': 'UI', 'city': urllib.parse.quote("北京"), 'city_zm': 'bj'},
    #     {'query': 'UI', 'city': urllib.parse.quote("上海"), 'city_zm': 'sh'},
    #     {'query': 'UI', 'city': urllib.parse.quote("广州"), 'city_zm': 'gz'},
    #     {'query': 'UI', 'city': urllib.parse.quote("深圳"), 'city_zm': 'sz'}
    # ]
    #
    # ui_result = m.dict()
    # ui_result["xueke"] = "ui"
    # p = Pool()
    # for arg in args:
    #     params = {'query': arg['query'], 'city': arg['city'], 'date': '20181013_20181020', 'city_zm': arg['city_zm']}
    #     p.apply_async(getdispNum, args=(params, ui_result))
    # p.close()
    # p.join()
    #
    #
    #
    # args = [
    #     {'query': urllib.parse.quote("平面"), 'city': urllib.parse.quote("成都"), 'city_zm': 'cd'},
    #     {'query': urllib.parse.quote("平面"), 'city': urllib.parse.quote("重庆"), 'city_zm': 'cq'},
    #     {'query': urllib.parse.quote("平面"), 'city': urllib.parse.quote("武汉"), 'city_zm': 'wh'},
    #     {'query': urllib.parse.quote("平面"), 'city': urllib.parse.quote("北京"), 'city_zm': 'bj'},
    #     {'query': urllib.parse.quote("平面"), 'city': urllib.parse.quote("上海"), 'city_zm': 'sh'},
    #     {'query': urllib.parse.quote("平面"), 'city': urllib.parse.quote("广州"), 'city_zm': 'gz'},
    #     {'query': urllib.parse.quote("平面"), 'city': urllib.parse.quote("深圳"), 'city_zm': 'sz'}
    # ]
    #
    # pingmian_result = m.dict()
    # pingmian_result["xueke"] = "ui"
    # p = Pool()
    # for arg in args:
    #     params = {'query': arg['query'], 'city': arg['city'], 'date': '20181013_20181020', 'city_zm': arg['city_zm']}
    #     p.apply_async(getdispNum, args=(params, pingmian_result))
    # p.close()
    # p.join()
    #
    # ui_result['cd'] = int(ui_result['cd']) + int(pingmian_result['cd'])
    # ui_result['cq'] = int(ui_result['cq']) + int(pingmian_result['cq'])
    # ui_result['wh'] = int(ui_result['wh']) + int(pingmian_result['wh'])
    # ui_result['bj'] = int(ui_result['bj']) + int(pingmian_result['bj'])
    # ui_result['sh'] = int(ui_result['sh']) + int(pingmian_result['sh'])
    # ui_result['gz'] = int(ui_result['gz']) + int(pingmian_result['gz'])
    # ui_result['sz'] = int(ui_result['sz']) + int(pingmian_result['sz'])
    #
    #
    #
    #
    # # 统计前端
    # args = [
    #     {'query': urllib.parse.quote('前端'), 'city': urllib.parse.quote("成都"), 'city_zm': 'cd'},
    #     {'query': urllib.parse.quote('前端'), 'city': urllib.parse.quote("重庆"), 'city_zm': 'cq'},
    #     {'query': urllib.parse.quote('前端'), 'city': urllib.parse.quote("武汉"), 'city_zm': 'wh'},
    #     {'query': urllib.parse.quote('前端'), 'city': urllib.parse.quote("北京"), 'city_zm': 'bj'},
    #     {'query': urllib.parse.quote('前端'), 'city': urllib.parse.quote("上海"), 'city_zm': 'sh'},
    #     {'query': urllib.parse.quote('前端'), 'city': urllib.parse.quote("广州"), 'city_zm': 'gz'},
    #     {'query': urllib.parse.quote('前端'), 'city': urllib.parse.quote("深圳"), 'city_zm': 'sz'}
    # ]
    #
    # qianduan_result = m.dict()
    # qianduan_result['xueke'] = "前端"
    # p = Pool()
    # for arg in args:
    #     params = {'query': arg['query'], 'city': arg['city'], 'date': '20181013_20181020', 'city_zm': arg['city_zm']}
    #     p.apply_async(getdispNum, args=(params, qianduan_result))
    # p.close()
    # p.join()
    #
    # # 统计H5
    # args = [
    #     {'query': "H5", 'city': urllib.parse.quote("成都"), 'city_zm': 'cd'},
    #     {'query': "H5", 'city': urllib.parse.quote("重庆"), 'city_zm': 'cq'},
    #     {'query': "H5", 'city': urllib.parse.quote("武汉"), 'city_zm': 'wh'},
    #     {'query': "H5", 'city': urllib.parse.quote("北京"), 'city_zm': 'bj'},
    #     {'query': "H5", 'city': urllib.parse.quote("上海"), 'city_zm': 'sh'},
    #     {'query': "H5", 'city': urllib.parse.quote("广州"), 'city_zm': 'gz'},
    #     {'query': "H5", 'city': urllib.parse.quote("深圳"), 'city_zm': 'sz'}
    # ]
    #
    # h5_result = m.dict()
    # h5_result['xueke'] = "前端"
    # p = Pool()
    # for arg in args:
    #     params = {'query': arg['query'], 'city': arg['city'], 'date': '20181013_20181020', 'city_zm': arg['city_zm']}
    #     p.apply_async(getdispNum, args=(params, h5_result))
    # p.close()
    # p.join()
    #
    # qianduan_result['cd'] = int(qianduan_result['cd']) + int(h5_result['cd'])
    # qianduan_result['cq'] = int(qianduan_result['cq']) + int(h5_result['cq'])
    # qianduan_result['wh'] = int(qianduan_result['wh']) + int(h5_result['wh'])
    # qianduan_result['bj'] = int(qianduan_result['bj']) + int(h5_result['bj'])
    # qianduan_result['sh'] = int(qianduan_result['sh']) + int(h5_result['sh'])
    # qianduan_result['gz'] = int(qianduan_result['gz']) + int(h5_result['gz'])
    # qianduan_result['sz'] = int(qianduan_result['sz']) + int(h5_result['sz'])
    #
    #
    #
    #
    # # 统计Python
    # args = [
    #     {'query': "Python", 'city': urllib.parse.quote("成都"), 'city_zm': 'cd'},
    #     {'query': "Python", 'city': urllib.parse.quote("重庆"), 'city_zm': 'cq'},
    #     {'query': "Python", 'city': urllib.parse.quote("武汉"), 'city_zm': 'wh'},
    #     {'query': "Python", 'city': urllib.parse.quote("北京"), 'city_zm': 'bj'},
    #     {'query': "Python", 'city': urllib.parse.quote("上海"), 'city_zm': 'sh'},
    #     {'query': "Python", 'city': urllib.parse.quote("广州"), 'city_zm': 'gz'},
    #     {'query': "Python", 'city': urllib.parse.quote("深圳"), 'city_zm': 'sz'}
    # ]
    #
    # python_result = m.dict()
    # python_result["xueke"] = "python"
    # p = Pool()
    # for arg in args:
    #     params = {'query': arg['query'], 'city': arg['city'], 'date': '20181013_20181020', 'city_zm': arg['city_zm']}
    #     p.apply_async(getdispNum, args=(params, python_result))
    # p.close()
    # p.join()
    #
    # # 统计软件测试
    # args = [
    #     {'query': urllib.parse.quote("软件测试"), 'city': urllib.parse.quote("成都"), 'city_zm': 'cd'},
    #     {'query': urllib.parse.quote("软件测试"), 'city': urllib.parse.quote("重庆"), 'city_zm': 'cq'},
    #     {'query': urllib.parse.quote("软件测试"), 'city': urllib.parse.quote("武汉"), 'city_zm': 'wh'},
    #     {'query': urllib.parse.quote("软件测试"), 'city': urllib.parse.quote("北京"), 'city_zm': 'bj'},
    #     {'query': urllib.parse.quote("软件测试"), 'city': urllib.parse.quote("上海"), 'city_zm': 'sh'},
    #     {'query': urllib.parse.quote("软件测试"), 'city': urllib.parse.quote("广州"), 'city_zm': 'gz'},
    #     {'query': urllib.parse.quote("软件测试"), 'city': urllib.parse.quote("深圳"), 'city_zm': 'sz'}
    # ]
    #
    # qa_result = m.dict()
    # qa_result["xueke"] = "软件测试"
    # p = Pool()
    # for arg in args:
    #     params = {'query': arg['query'], 'city': arg['city'], 'date': '20181013_20181020', 'city_zm': arg['city_zm']}
    #     p.apply_async(getdispNum, args=(params, qa_result))
    # p.close()
    # p.join()
    #
    #
    #
    # result = [java_result,php_result,ui_result,qianduan_result,python_result,qa_result]
    # for r in result:
    #     print(r)


def getdispNum(args, java_result):
    url = 'http://zhaopin.baidu.com/api/qzasync?query={args[query]}&city={args[city]}&is_adq=1&pcmod=1&date={args[date]}'.format(
        args=args)
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    response = requests.get(url,headers=headers)
    data = json.loads(response.content.decode("utf-8"))
    java_result[args['city_zm']] = data['data']['dispNum']
    print(data['data']['dispNum'])


if __name__ == "__main__":
    main()
