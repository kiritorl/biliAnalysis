# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyproPipeline:
    def process_item(self, item, spider):
        # print("数据输出到管道: ")
        # print(item['jobName'],
        #       item['companyName'],
        #       item['jobSalary'],
        #       item['jobArea'],
        #       item['jobDate'],
        #       item['jobLink'])
        #
        # # 数据加工处理和统计分析
        # jobCity = item['jobArea']
        # salary = item['jobSalary']
        #
        # if jobCity.find("-") != -1:
        #     jobCity = jobCity.split("-")[0]
        #     pass
        #
        # params = [item['jobName'],
        #         item['companyName'],
        #         item['jobSalary'],
        #         item['jobArea'],
        #         item['jobDate'],
        #         item['jobLink'],
        #         item['jobType'],
        #           jobCity,
        #           jobLowSalary,
        #           jobHighSalary,
        #           jobMeanSalary]
        #
        # jobdao = JobDao()
        # if jobMeanSalary > 0:
        #     result = jobdao.create(params)
        #     if result == 1:
        #         print("写入成功")
        #         pass
        #     pass

        return item
