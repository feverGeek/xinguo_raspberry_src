#-*- coding: utf-8 -*-
import psutil
import sys
import os 
# u盘挂载后的所在位置
usbDiskPath = '/media/pi/B6AF-3198'

# u盘内的一个特定位置，图片要被移到这里
#./KadexMicro/Image/B/
specifyFile = 'KadexMicro'

def getDiskInfo():

	diskPartNum = 0
	diskPartDevice = []
	diskPartMountPoint = []
	for part in psutil.disk_partitions():
		diskPartNum += 1
		diskPartDevice.append(part[0])
		diskPartMountPoint.append(part[1])

	return {'diskPartNum' : diskPartNum,
			'diskPartDevice' : diskPartDevice,
			'diskPartMountPoint' : diskPartMountPoint}
		
		

def writeImgToDisk(path, mountPoint):
	# 1 获取所有移动硬盘的挂载点 
	mobileDiskMountPoint = []
	targetDiskMountPoint = None 
	for point in mountPoint:
		if 'media' in point:
			mobileDiskMountPoint.append(point)
	# 2 检测特定u盘是否被挂载
	for point in mobileDiskMountPoint:
		if specifyFile not in os.listdir(point):
			continue
		targetDiskMountPoint = point
	
	if targetDiskMountPoint:
		#4. U盘挂载成功后将文件写到U盘中去
		os.system('sudo cp {} {}'.format(path, targetDiskMountPoint+'/KadexMicro/Image/B/'))
		os.system('sudo umount {}'.format(targetDiskMountPoint))
		return True
	else:
		return False


if __name__ == '__main__':
	path = '/home/pi/Desktop/test'
	dic = getDiskInfo()
	print(dic)
	if writeImgToDisk(path, dic['diskPartMountPoint']):
		print('successful')
	else:
		print('failed')
