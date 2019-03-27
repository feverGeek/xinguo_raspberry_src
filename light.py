#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys
import string

# Light class
class Light():
	def __init__(self, pin, times):
		self.times = 0
		self.pin = pin
		self.pins = [5, 6, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
		self.up_time = 0.5
		self.down_time = 0.5
		self.check_pin(pin)
		self.set_times(times)
		self.run(self.times)

	def run(self, times):
		self.setup(self.pin)
		self.set_times(times)
		try:
			self.loop(self.pin, self.times)
		except KeyboardInterrupt:
			self.destroy(self.pin)
	
	def set_times(self, times):
		self.times = times

	def check_pin(self, pin):
		if pin in self.pins:
			print('%d 是有效编号' %pin)
		else:
			print('只能输入以下有效的pin编号')
			for i in self.pins:
				print(i)
			exit()

	def setup(self, pin):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.LOW)

	def loop(self, pin, times):
		for i in range(0, times):
			GPIO.output(pin, GPIO.HIGH)
			print('light up')
			time.sleep(self.up_time)
			GPIO.output(pin, GPIO.LOW)
			print('light down')
			time.sleep(self.down_time)

	def destroy(self, pin):
		GPIO.output(pin, GPIO.LOW)
		GPIO.setup(pin, GPIO.IN)


if __name__ == '__main__':
	print('1')
	light = Light(12, 2)
	print('2')
	light.run(4)
