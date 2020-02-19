# -*- coding: utf-8 -*-
import scrapy
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from imagedownload.items import ImagedownloadItem


class ImagedownspSpider(scrapy.Spider):
    name = 'imagedownsp'
    # allowed_domains = ['imagedown']
    # start_urls = [
    #     'http://books.toscrape.com/catalogue/category/books/romance_8/page-1.html',
    #     'http://books.toscrape.com/catalogue/category/books/romance_8/page-2.html'
    # ]

    price_array = []
    count = 0

    custom_settings = {
        "ITEM_PIPELINES": {
            'imagedownload.pipelines.ImagedownloadPipeline': 300,
            # 'scrapy.pipelines.images.ImagesPipeline': 1,
        },
        "FILES_STORE": 'book_cover_images',
        "IMAGES_STORE": 'book_cover_images'
    }


    def __init__(self):
        # chrome_driver = "imagedownload/chromedriver/chromedriver.exe"
        firefox_driver = "imagedownload/chromedriver/geckodriver.exe"

        self.driver = webdriver.Firefox(executable_path = firefox_driver)

        chrome_driver = "imagedownload/chromedriver/chromedriver.exe"
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary
        # self.driver = webdriver.Chrome(chrome_driver, chrome_options = options)
        self.driver.set_window_size(1366, 768)

        self.start_urls = ['https://www.feefo.com/business/gb_en/resources/blog']

    def parse(self, response):

        #https://microcel.com/brands/adonit

        self.driver.get(response.url)
        sleep(1)

        self.driver.find_element_by_xpath("//a[contains(@class, 'cc-btn cc-dismiss')]").click()

        # self.driver.find_element_by_id("customer_email").send_keys("jason@allbatteryexperts.com")
        # sleep(1)
        # self.driver.find_element_by_id("customer_password").send_keys("Apple4421")
        # sleep(1)
        # self.driver.find_element_by_class_name("action_button").click()

        # sleep(1)
        # self.driver.get('https://www.cellhelmetwholesale.com/pages/upc-barcode-sku-list')


        print("-------------------------------start------------------------\n")

        next_page = 1
        count = 0
        all_links = []
        img_links = []
        all_titles = []
        all_contents = []
        all_meta = []
        all_date = []


        while(next_page != 0):
            sleep(1)
            try:
                # if self.driver.find_element_by_xpath("//div/a[contains(@class, 'btn btn-secondary')]"):
                self.driver.find_element_by_xpath("//div/a[contains(@class, 'btn btn-secondary')]").click()
                sleep(3)
                # next_page = 0
                    # next_page+=1
            except:
                next_page = 0
                print("END")
        
        alist = self.driver.find_elements_by_xpath("//div[contains(@class, 'article__body')]")
        for ali in alist:
            surl = ali.find_element_by_xpath("./a[contains(@class, 'article__link')]").get_attribute("href")
            all_links.append(surl)
            iurl = ali.find_element_by_xpath("./a[contains(@class, 'article__link')]/picture/img[contains(@class, 'article__img')]").get_attribute("src")
            img_links.append(iurl)
            cdate = ali.find_element_by_xpath("./a[contains(@class, 'article__link')]/div[contains(@class, 'article__content')]/p[contains(@class, 'article__meta mb-0')]").text
            all_date.append(cdate)
            # all_links.append(str(ali.get_attribute("href")))

        for ele in all_links:
            self.driver.get(ele)
            sleep(1)
            at = self.driver.find_element_by_xpath("//h1[contains(@class, 'display-4')]").text
            act = self.driver.find_element_by_xpath("//section[contains(@class, 'article__entry__content')]").get_attribute("outerHTML")
            am = self.driver.find_element_by_xpath("//meta[contains(@property, 'og:description')]").get_attribute("content")

            all_titles.append(at)
            all_contents.append(act)
            all_meta.append(am)

        for aft in all_links:
            yield ImagedownloadItem(Url=aft, Date=all_date[count], Title=all_titles[count], Content=all_contents[count], Meta=all_meta[count], ImgUrl=img_links[count])
            count+=1


        # while(next_page !=0):
        #     detail_array = []
        #     tlis = []
        #     imglist = []

        #     Title = ''
        #     SKU = ''
        #     Barcode = ''
        #     MSRP = ''

        #     count = 1

        #     detail_array = self.driver.find_elements_by_xpath("//div/table/tbody/tr")

        #     for item in detail_array:
        #         Title = item.find_element_by_xpath("//tr[" + str(count) + "]//td[1]").text
        #         SKU = item.find_element_by_xpath("//tr[" + str(count) + "]//td[2]").text
        #         Barcode = item.find_element_by_xpath("//tr[" + str(count) + "]//td[3]").text + '@@@'
        #         # MSRP = item.find_element_by_xpath("//tr[" + str(count) + "]//td[4]").text

        #         print('\n' + Title + '   ' + SKU + '   ' + Barcode + '   ' + MSRP + '\n')
        #         count+=1

        #         yield ImagedownloadItem(Title=Title, SKU=SKU, Barcode=Barcode, MSRP=MSRP)


        #     try:
        #         if self.driver.find_element_by_xpath("//p/a[" + str(next_page) + "]"):
        #             self.driver.find_element_by_xpath("//p/a[" + str(next_page) + "]").click()
        #             next_page+=1
        #     except:
        #         next_page = 0

        # for li in all_links:
        #     # sleep(0.5)
        #     yield scrapy.Request(li, callback=self.parse_book)


        # self.driver.close()


    # def parse_book(self, response):

    #     self.driver.get(response.url)

    #     # sleep(1)

    #     tem_msrp = ''


    #     imglist = self.driver.find_elements_by_xpath("//li/img")
    #     d_imglist = []
    #     for imgli in imglist:
    #         d_imglist.append(str(imgli.get_attribute("src")))

        
    #     try:
    #         Title = self.driver.find_element_by_xpath("//h1").text.strip()
    #         pass
    #     except Exception as e:
    #         Title = ''
    #         pass

    #     try:
    #         SKU = ''
    #         pass
    #     except Exception as e:
    #         SKU = ''
    #         pass

    #     try:
    #         Barcode = ''
    #         pass
    #     except Exception as e:
    #         Barcode = ''
    #         pass
        
    #     try:
    #         MSRP = tem_msrp
    #         pass
    #     except Exception as e:
    #         MSRP = ''
    #         pass
        

    #     yield ImagedownloadItem(Title=Title, SKU=SKU, Barcode=Barcode, MSRP=MSRP)
        
        
    #     pass
