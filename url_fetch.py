#/usr/bin/python3
# -*- coding:utf-8 -*-
import requests
import re
import json
from requests_futures.sessions import FuturesSession


joblist_url = "http://search.51job.com/list/190200%252C00,000000,0000,00,9,99,%2B,0,{0}.html?"\
    "lang=c&stype=2&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&"\
    "lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&confirmdate=9&fromType=1&dibiaoid=0"

start_url = joblist_url.format(1)

total_jobs_pattern = "共(?P<total>\d+)条职位"
total_pages_pattern = "共(?P<total>\d+)页，到第"
job_detail_url_pattern = "http://jobs.51job.com/.+?/\d+.html"
cookies = dict(guide='1')

# 抓取总招聘数量信息
r = requests.get(start_url, cookies=cookies,)
r.encoding = 'gb2312'

# 总招聘信息数目
m = re.search(total_jobs_pattern, r.text)
total_job_count = m.group('total')
# 总招聘信息列表数目
m = re.search(total_pages_pattern, r.text)
total_pages = m.group('total')
print("共有{0}条招聘信息,共{1}页.".format(total_job_count, total_pages))

job_detail_url_list = []

session = FuturesSession(max_workers=10)
futures = [session.get(joblist_url.format(i + 1), cookies=cookies)
           for i in range(int(total_pages))]

fetched_pages = 0
fetched_jobs = 0
for future in futures:
    r = future.result()
    urls = re.findall(job_detail_url_pattern, r.text)
    fetched_jobs += len(urls)
    fetched_pages += 1
    print("{0} pages fetched, {1} jobs fetched.".format(
        fetched_pages, fetched_jobs))
    job_detail_url_list.extend(urls)


json.dump(job_detail_url_list, open(
    "job_urls.json", 'w'), indent=2, sort_keys=True, ensure_ascii=False)
