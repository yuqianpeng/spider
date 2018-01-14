
from selenium import webdriver
import time
import json
from lxml import etree

def handle_data(html):
	html1 = etree.HTML(html)
	li_list = html1.xpath('//div[@class="content"]/ul/li') 
	items = []
	for i in range(len(li_list)):
		item = {}
		image_url = li_list[i].xpath('.//div[@class="header "]/a/img/@data-src')
		# print(len(image_url))
		if len(image_url) == 0:
			image_url = ''
		else:
			image_url = image_url[0]
		name = li_list[i].xpath('.//div[contains(@class,"header")]/a/div/span[@class="name"]/text()')[0]
		time = li_list[i].xpath('.//div[contains(@class,"header")]/a/div/span[@class="time"]/text()')[0]

		if i <= 20:
			content = li_list[i].xpath('.//div[contains(@class,"content-wrapper")]/a/div/h1/p/text()')
			print(len(content))
		else:
			content = li_list[i].xpath('.//div[contains(@class,"content-wrapper")]/a/div/text()')
			print(len(content))
		item['image_url'] = image_url
		item['name'] = name
		item['time'] = time
		item['content'] = content
		items.append(item)
	string = json.dumps(items, ensure_ascii=False)
	with open('neihan.json', 'w', encoding='utf-8') as fp:
		fp.write(string)	

def main():
	path = r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe'
	driver = webdriver.PhantomJS(path)
	url = 'http://neihanshequ.com/'
	driver.get(url)
	time.sleep(2)
	end = int(input('请输入加载几页：'))
	for x in range(1, end):
		load_button = driver.find_element_by_id('loadMore')
		load_button.click()
		time.sleep(2)
	html = driver.page_source
	print(type(html))
	handle_data(html)


if __name__ == '__main__':
	main()