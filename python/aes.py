#coding:utf-8
u"""
这是主程序后端的一个模块，用于处理图片的加密解密以及hash
创建时间：2018年12月20日13:39:39
版本：1.0.2(版本控制已经同步至GitHub)
由于众多库的支持兼容性，PY2还是PY3暂未确定
"""
import hashlib
def encryption(base64,save_path,key):#加密
	pass
	
def decrypt(path,key):#解密
	pass
	
def hash(string):
	md5 = hashlib.md5()
	md5.update(string)
	return md5.hexdigest()
	
if __name__=="__main__":
	while 1:
		print eval(raw_input(">"))
	