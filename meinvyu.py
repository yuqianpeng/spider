import urllib.request
import urllib.parse
import os
import re

def download_image(image_url):
	dirpath = './qbmeinv'
	# 获取文件名
	filename = os.path.basename(image_url)
	# 拼接文件全路径
	filepath = os.path.join(dirpath, filename)
	# 下载图片
	urllib.request.urlretrieve(image_url, filepath)
	print(filepath + '下载完毕')

def handle_url(url, page):
	url = url + str(page)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
	}
	request = urllib.request.Request(url=url, headers=headers)
	return request

def handle_content(request):
	response = urllib.request.urlopen(request)
	html = response.read().decode('utf-8')
	pattern = re.compile(r'<img class="height_min" title=.*? alt=.*? onerror=.*? src=.*? />')

	src_list = pattern.findall(html)
	ret1 = []
	for i in src_list:
		ret1.append(i.split(' ')[-2])

	for j in ret1:
		image_url = j[5:-1]
		download_image(image_url)

		

def main():
	url = "https://www.dbmeinv.com/?pager_offset="
	start_page = int(input("请输入大于等于1的抓取的起始页码："))
	end_page = int(input("请输入抓取的结束页码："))
	print("开始下载。。。。。。。。。。。")
	for page in range(start_page, end_page + 1):
		request = handle_url(url, page)

		handle_content(request)
	print("全部下载完毕")


if __name__== "__main__":
	main()