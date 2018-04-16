# -*- coding: utf-8 -*-
import scrapy


class VnpssSpider(scrapy.Spider):
    name = 'vnpss'
    allowed_domains = ['bwh1.net']
    start_urls = ['https://bwh1.net/vps-hosting.php']

    def parse(self, response):
        KVM_text = response.xpath("//div[@class='plancon']/div[@class='bronze']/ul[2]/li/text()").extract_first("")
        OVZ_text = response.xpath("//div[@class='plancon']/div[@class='bronze']/ul[1]/li/text()").extract_first("")
        money = response.xpath("//div[@class='plancon']/div[@class='bronze']/ul[1]/li[10]/text()").extract_first("")
        if money:
            if KVM_text != "KVM: no stock":
                print 'KVM，上架'
            if OVZ_text != "OVZ: no stock":
                print "OVZ，上架"
        print "结束"
