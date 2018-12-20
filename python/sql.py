#coding:utf-8
u"""
这是主程序的数据库逻辑处理和链接程序
创建时间：2018年12月20日13:39:39
版本：1.0.1(版本控制已经同步至GitHub)
由于众多哭的支持兼容性，PY2还是PY3暂未确定
"""

def checkchar(string):#检测非法字符，防止sql注入
	i=string
	for i in string:
		pass
	return i#返回，若无非法字符或者成功转义，返回字符串，
	
#数据库实现:SQLServer
import pymssql
class main():
	def connect(server,user,password,database):
		# server    数据库服务器名称或IP
		# user      用户名
		# password  密码
		# database  数据库名称
		conn = pymssql.connect(server, user, password, database)
		cursor = conn.cursor()
	
