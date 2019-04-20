#!/usr/bin/env python3

import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PIL import Image
from io import BytesIO
from xvfbwrapper import Xvfb


WEBCAMS = {
	"https://webcam.exdesign.ru/cds-polyustrovo-1": "webcam1.png",
    "https://webcam.exdesign.ru/cds-polyustrovo-2": "webcam2.png"}
VIDEO_CLASSNAME = "container"


def capture_photos():


	options = Options()
	options.headless = True
	driver = webdriver.Chrome(options=options)

	for url, pic in WEBCAMS.items():
		print("%s: capturing..." % url)
		driver.get(url)
		sleep(5)
		element = driver.find_element_by_class_name(VIDEO_CLASSNAME)
		location = element.location
		size = element.size
		png = driver.get_screenshot_as_png()

		im = Image.open(BytesIO(png))

		left = location['x']
		top = location['y']
		right = location['x'] + size['width']
		if url == "https://webcam.exdesign.ru/cds-polyustrovo-1":
			# the site lies about element size (850px)
			bottom = 700
		else:
			bottom = location['y'] + size['height']

		im = im.crop((left, top, right, bottom))
		im.save(pic)
		print("%s: captured as %s" % (url, pic))
	driver.quit()


def main():
	with Xvfb(width=1920, height=1080) as xvfb:
		capture_photos()

if __name__ == "__main__":
	main()
