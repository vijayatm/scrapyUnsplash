# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from unsplash.items import UnsplashItem
from PIL import Image

class UnsplashpicSpider(scrapy.Spider):
	name = 'unsplashPic'
	start_urls =['file:///Users/vijay-7431/IAMV/iamv_pythonScripts/SCRAPY/unsplash_1/unsplash/FolderPages/bikini.htm']
	def parse(self, response):
		baseUrl = 'https://unsplash.com'
		print ("inside first block")
		for bufferLinks in response.xpath('//figure//a[@itemprop="contentUrl"]/@href').extract():
			print (bufferLinks)
			yield Request(bufferLinks, callback=self.parse_links)

	def parse_links(self, response):
		imageLinkList = []
		for imageLink in response.css('img').xpath('@src').getall():
			if imageLink.startswith('https://images.unsplash'):
				imageLinkList.append(imageLink)
		finalUrl = imageLinkList[2][:imageLinkList[2].find("&auto")]
		yield UnsplashItem(image_urls=[finalUrl])		
		print ("\n\n\n")

