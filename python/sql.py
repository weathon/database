#coding:utf-8
u"""
这是主程序的数据库逻辑处理和链接程序
创建时间：2018年12月20日13:39:39(时区：芝加哥)
版本：1.1.0(版本控制已经同步至GitHub)
由于众多库的支持兼容性，PY2还是PY3暂未确定
"""

def checkchar(string):#检测非法字符，防止sql注入，但不完善(由于只是怕用户自己误操作，不考虑攻击)，需谨慎使用，后期可能考虑base64
	i=[]
	wordlist=['"',"'",chr(92),chr(47),"and","or","="," ",")","(",";","*","!","@","#","$","%","^","&"]#危险字符
	for char in wordlist:
		if char in string:
			i.append(char)
		
	return i#返回，空列表表示允许，否则表示拒绝，内容为拒绝的字符

#数据库实现:SQLServer
import pymssql
class main():
	def connect(self,server,user,password,database):
		# server    数据库服务器名称或IP
		# user      用户名
		# password  密码
		# database  数据库名称
		self.conn = pymssql.connect(server, user, password, database)
		self.cursor = conn.cursor()
	

def backup():#备份数据库(不是备份图片)
	pass
	
if __name__=="__main__":
	while 1:
		print eval(raw_input(">"))