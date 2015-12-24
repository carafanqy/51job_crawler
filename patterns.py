#/usr/bin/python3
# coding=utf-8

total_jobs_pattern = "共(?P<total>\d+)条职位"
total_pages_pattern = "共(?P<total>\d+)页，到第"
job_detail_url_pattern = "http://jobs.51job.com/.+?/\d+.html"

job_detail1_pattern = "<dt>发布日期：</dt>\s+?<dd class=\"text_dd\">(?P<pub_date>\d{4}\-\d{1,2}\-\d{1,2})&nbsp;</dd>\s+?"\
    "<dt>工作地点：</dt>\s+?<dd class=\"text_dd\">(?P<area>.+)&nbsp;</dd>\s+?<dt>招聘人数：</dt>\s+?<dd class=\"text_dd\">"\
    "(?P<number>.+)&nbsp;</dd>\s+?</dl>"
job_detail2_pattern = "<dt>工作年限：</dt>\s+?<dd class=\"text_dd\">(?P<expirence>.+)&nbsp;</dd>\s+?"\
    "<dt>学历要求：</dt>\s+?<dd class=\"text_dd\">(?P<degree>.+)&nbsp;</dd>\s+?<dt>薪资范围：</dt>\s+?<dd class=\"text_dd\">"\
    "<span class=\"f-col-red\">(?P<salary>.+)</span>&nbsp;</dd>\s+?</dl>"
work_location_pattern = "<dt>上班地址：</dt>\s+?<dd class=\"text_.+?\">(?P<location>.+?)\s+</dd>\s+</dl>"
walfare_pattern = "<span class=\"Welfare_label\">(?P<walfare>.+)</span>"

work_category_pattern = "class=\"f-col-blue\">(?P<category>.+)<"
company_name_pattern = "<div class=\"tBorderTop_box job_page_company\">\s+<h2>(?P<name>.+?)<i"
industry_pattern = "<dt>公司行业：</dt>\s+<dd class=\"text_dd\d+\">(?P<industry>.+)</dd>"
company_type_pattern = "<dt>公司性质：</dt>\s+<dd>(?P<type>.+)</dd>"
company_size_pattern = "<dt>公司规模：</dt>\s+<dd>(?P<size>.+)</dd>"
company_loc_pattern = "<p class=\"job_company_text\">(?P<loc>[^<]+)</p>"
