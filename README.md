# 51job_crawler

爬取51job某一城市全部招聘信息

1. 修改url_fetch.py中的启动url,选择所需要爬取的城市.

    joblist_url = "http://search.51job.com/list/190200%252C00,000000,0000,00,9,99,%2B,0,{0}.html?"\
        "lang=c&stype=2&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&"\
        "lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&confirmdate=9&fromType=1&dibiaoid=0"


2. 运行url_fetch.py获取招聘信息数目和url,生成job_urls.json.

    python3 url_fetch.py


3. 运行job_details.py,根据job_urls.json中的信息,开始抓取招聘信息详情.

    python3 job_details.py
    
可以根据运行情况修改线程池大小加快抓取速度

    session = FuturesSession(max_workers=5)

