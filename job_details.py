#/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import re
import json
from requests_futures.sessions import FuturesSession
from patterns import *

url_list = json.load(open('job_detail_url.json'))
total_urls = len(url_list)
print("{0} urls loaded.".format(total_urls))


def parse_html(text):
    rec = {}
    rec['pub_date'], rec['area'], rec[
        'number'] = re.search(job_detail1_pattern, text).groups()
    rec['exp'], rec['degree'], rec[
        'salary'] = re.search(job_detail2_pattern, text).groups()
    rec['work-loc'] = re.findall(work_location_pattern, text)
    rec['walfare'] = re.findall(walfare_pattern, text)
    rec['catetory'] = re.findall(work_category_pattern, text)
    rec['company_name'] = re.findall(company_name_pattern, text)
    rec['industry'] = re.findall(industry_pattern, text)
    rec['company_type'] = re.findall(company_type_pattern, text)
    rec['company_size'] = re.findall(company_size_pattern, text)
    rec['company_loc'] = re.findall(company_loc_pattern, text)
    return rec

job_data = []
fetched_count = 0
failed_count = 0
session = FuturesSession(max_workers=5)
futures = [session.get(url) for url in url_list]
for future in futures:
    r = future.result()
    try:

        r.encoding = 'gb2312'
        job_data.append(parse_html(r.text))
        fetched_count += 1
        print("{0} jobs fetched {1} jobs failed {2} jobs left.".format(
            fetched_count, failed_count, total_urls - fetched_count - failed_count))
        if fetched_count % 5000 == 0:
            json.dump(job_data, open(
                "job_data.json", 'w', encoding="utf=8"), indent=2, sort_keys=True, ensure_ascii=False)
    except Exception as e:
        failed_count += 1
        print("fetching failed:{0} {1} total fail".format(e, failed_count))
        print(r.url)


json.dump(job_data, open(
    "job_data.json", 'w', encoding="utf=8"), indent=2, sort_keys=True, ensure_ascii=False)
