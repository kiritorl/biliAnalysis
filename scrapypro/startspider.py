from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'spiderdata',
         '-a', 'base_url=https://search.bilibili.com/all?keyword=%E5%8E%9F%E7%A5%9E&from_source=webtop_search&spm_id_from=333.851&page={0}',
         '-a', 'keyWord=原神'
    ])
