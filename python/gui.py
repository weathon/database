#coding:utf-8
u"""
这是主程序的GUI程序，用于创建一个"浏览器窗口"，建立混合APP
创建时间：2018年12月20日13:39:39
版本：1.0.0(版本控制已经同步至GitHub)
由于众多库的支持兼容性，PY2还是PY3暂未确定
"""
#coding:utf-8
import htmlPy

web_app = htmlPy.WebAppGUI(title=u"文档信息管理系统", maximized=True)
web_app.url = u"http://127.0.0.1:2333/"
web_app.start()

if __name__=="__main__":
	while 1:
		print eval(raw_input(">"))