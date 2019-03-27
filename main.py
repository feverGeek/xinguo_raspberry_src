#-*- coding: utf-8 -*-
#1. 循环接收服务器端的信息,如果是打印信息,则接收图片链接
#2. 下载图片
#3. 将图片存到U盘
#4. 图片移动成功后点亮led
#5. 回到第一步

from light import *
from usbdriver import *
from socket import *
from mydownload import *


def infoTrans():
	#1. 创建套接字
	udpSocket = socket(AF_INET, SOCK_DGRAM)

	#2. 绑定ip 端口
	address = ('127.0.0.1', 6910)
	udpSocket.bind(address)

	#3. 接收信息
	while(True):
		recvData,remoteAddr = udpSocket.recvfrom(1024)
		print(recvData)
		print(remoteAddr)
		
		imgUrl = 'http://' + recvData.decode()
		udpSocket.sendto('0'.encode('utf-8'), remoteAddr)
		print('imgUrl: ' + imgUrl)
	    
		imgPath = download(imgUrl)
		if imgPath:
			print('imgPath: ' + imgPath)
	
		dic = getDiskInfo()
		if writeImgToDisk(imgPath, dic['diskPartMountPoint']):
			print('successful') 
			Light(12, 2)
		else:
			print('failed')		
			Light(12, 4)


if __name__ == '__main__':
	print('->>>>>>Start')
	infoTrans()
