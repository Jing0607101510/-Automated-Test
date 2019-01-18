# -*- coding: utf-8 -*-

import threading, time, http.client
HOST = "you.163.com"; #主机地址 例如192.168.1.101
PORT = 443 #端口
URI = "/xhr/search/search.json" #相对地址,加参数防止缓存，否则可能会返回304
TOTAL = 0 #总数
SUCC = 0 #响应成功数
FAIL = 0 #响应失败数
EXCEPT = 0 #响应异常数
MAXTIME=0 #最大响应时间
MINTIME=100 #最小响应时间，初始值为100秒
TOTALTIME = 0 #总的响应时间
GT3=0 #统计3秒内响应的
LT3=0 #统计大于3秒响应的

# 创建一个 threading.Thread 的派生类
class RequestThread(threading.Thread):
    # 构造函数
    def __init__(self, thread_name, post_data):
        threading.Thread.__init__(self)
        self.test_count = 0
        self.post_data = post_data

    # 线程运行的入口函数
    def run(self):
        self.test_performace()


    def test_performace(self):
        global TOTAL
        global SUCC
        global FAIL
        global EXCEPT
        global GT3
        global LT3
        global TOTALTIME
        try:
            st = time.time()
            conn = http.client.HTTPSConnection(HOST, PORT, False)
            conn.request('POST', '/', self.post_data)
            res = conn.getresponse()

            time_span = time.time()-st
            if res.status == 200:
                TOTAL+=1
                SUCC+=1
                TOTALTIME += time_span
            else:
                TOTAL+=1
                FAIL+=1

            self.maxtime(time_span)
            self.mintime(time_span)
            if time_span>3:
                GT3+=1
            else:
                LT3+=1
        except Exception as e:
            print(e)
            TOTAL+=1
            EXCEPT+=1
        conn.close()

    def maxtime(self,ts):
        global MAXTIME
        if ts>MAXTIME:
            MAXTIME=ts
    def mintime(self,ts):
        global MINTIME
        if ts<MINTIME:
            MINTIME=ts

def test(thread_count, post_data):
    global TOTAL
    global SUCC
    global FAIL
    global EXCEPT
    global GT3
    global LT3
    global TOTALTIME
    global MINTIME
    global MAXTIME

    TOTAL = 0
    SUCC = 0
    FAIL = 0
    EXCEPT = 0
    MAXTIME=0
    MINTIME=100
    TOTALTIME = 0
    GT3=0
    LT3=0

    # main 代码开始
    print('===========task start===========')
    # 开始的时间
    start_time = time.time()
    # 并发的线程数
    #thread_count = 10

    i = 0
    TOTAL = 0
    while i < thread_count:
        t = RequestThread("thread" + str(i), post_data)
        t.start()
        i += 1

    t=0
    #并发数所有都完成或大于60秒就结束
    while TOTAL<thread_count and t<60:
        #print "total:%d,succ:%d,fail:%d,except:%d\n"%(TOTAL,SUCC,FAIL,EXCEPT)
        #print HOST,URI
        t+=1
        time.sleep(1)

    print('===========任务 结束===========')
    print("线程数", thread_count)
    print("发送的数据", post_data)
    print("总请求:%d,成功请求:%d,失败请求:%d,异常请求:%d"%(TOTAL,SUCC,FAIL,EXCEPT))
    print('最大响应时间:',MAXTIME)
    print('最小响应时间',MINTIME)
    print('响应时间大于3s的请求数:%d,百分比:%0.2f'%(GT3,float(GT3)/TOTAL))
    print('响应时间小于3d的请求数:%d,百分比:%0.2f'%(LT3,float(LT3)/TOTAL))
    print('平均响应时间: %0.2f'%(TOTALTIME/SUCC))


if __name__ == "__main__":
    post_datas = ['{"keyword":"usb"}']
    test(10, post_datas[0])
    test(20, post_datas[0])
    test(50, post_datas[0])
    test(10, post_datas[0])
    test(20, post_datas[0])
    test(50, post_datas[0])
    test(1000, post_datas[0])