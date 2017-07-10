##让音乐点缀生活————微信公众号  ‘影音新生活’  有很多好听音乐，为了不用一首首的定来听，这个小小爬虫可以下载下来听循环播放

import requests
import re
import os
import logging;logging.basicConfig(level=logging.DEBUG)
from pyquery import PyQuery as pq


def get_music_url(url):
	response = requests.get(url)
	pattern = re.compile(r'audiourl="(.*?)" music_name="(.*?)"')
	music_url = re.findall(pattern,response.text)

	return music_url


def mkdir(url):
	response = requests.get(url)
	doc = pq(response.text)
	path = doc.find('#activity-name').text().strip()

	isExist = os.path.exists(os.path.join(os.getcwd(),path))
	if not isExist:
		logging.info(u'建了一个名字叫做  '+path+u'  的文件夹！')
		os.mkdir(os.path.join(os.getcwd(),path))
		os.chdir(os.path.join(os.getcwd(),path))
		logging.info(os.getcwd())
		return True
	else:
		logging.info(u'名字叫  '+path+u'  的文件夹已经存在')
		os.chdir(os.path.join(os.getcwd(),path))
		logging.info(os.getcwd())
		return False

def save(music_url):	 
	title = music_url[1]
	url = music_url[0]
	logging.info('开始下载 '+title)
	music = requests.get(url) 
	with open(title + '.m4a', 'ab') as f:
		f.write(music.content)
	logging.info(title+' 下载完毕')

def run(url):
	mkdir(url)
	
	music_url = get_music_url(url)

	logging.info('准备下载  '+str(len(music_url))+'  条歌')

	result = map(save,music_url)

	list(result)


if __name__ == '__main__':
	url = 'http://mp.weixin.qq.com/s/UHac9_peOBUCfEA_C7ABKQ'
	run(url)

	


