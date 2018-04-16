# -*- coding: utf-8 -*-
import scrapy
from scrapy.mail import MailSender


class VnpssSpider(scrapy.Spider):
    name = 'vnpss'
    allowed_domains = ['bwh1.net']
    start_urls = ['https://bwh1.net/vps-hosting.php']

    def parse(self, response):
        KVM_text = response.xpath("//div[@class='plancon']/div[@class='bronze']/ul[2]/li/text()").extract_first("")
        OVZ_text = response.xpath("//div[@class='plancon']/div[@class='bronze']/ul[3]/li/text()").extract_first("")
        money = response.xpath("//div[@class='plancon']/div[@class='bronze']/ul[1]/li[10]/text()").extract_first("")
        mailer = MailSender(
            smtphost = "smtp.163.com",
            mailfrom = "wxy148616@163.com",
            smtpuser = "wxy148616@163.com",
            smtppass = "wxy148616",
            smtpport = 25
            )
        if money:
            if KVM_text != "KVM: no stock":
                body = u"KVM，上架，尽快购买！"
                subject = u'KVM上架'
                mailer.send(to = ["1486162155@qq.com", "wxy148616@163.com"], subject = subject.encode("utf-8"),
                            body = body.encode("utf-8"))
            if OVZ_text != "OVZ: no stock":
                body = u"OVZ，上架，尽快购买！"
                subject = u'OVZ上架'
                mailer.send(to = ["1486162155@qq.com", "wxy148616@163.com"], subject = subject.encode("utf-8"),
                            body = body.encode("utf-8"))
        body = u"没有上架商品..."
        subject = u'vpn爬虫'
        mailer.send(to = ["1486162155@qq.com", "wxy148616@163.com"], subject = subject.encode("utf-8"), body = body.encode("utf-8"))
