import re
import time
import random

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from requests.exceptions import RequestException

import warnings

warnings.filterwarnings('ignore')

# 杭州站的基础url
hangzhou_url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=664&workExperience=-1&education=5&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3'
# hangzhou_url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=653&workExperience=-1&education=-1' \
#                '&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3' \
#                '&_v=0.56941966&x-zp-page-request-id=15e5b2a55f484f4da5e0be92d842b06e-1548030421680-768527'

# 请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def get_response(url, headers):
    '''
    获取响应

    参数：
    url     -- 目标站点
    headers -- 请求头信息
    返回：
    若目标站点成功访问，返回其返回的响应信息
    '''
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response
        return None
    except RequestException:
        return None

def parse_data(max_num, step):
    # 初始化一个列表，用于存放各页的信息
    page_info = []

    # 依次解析各页的数据
    for i in range(0, max_num, step):
        url = hangzhou_url.format(i)    # 组装每页的url
        print(url)
        results = get_response(url, headers=headers).json().get(
            'data').get('results')    # 从响应信息中获取需要的字典数据
        print('准备获取第{}页的信息 loading……'.format(
            np.round((i/90)+1)))    # 90代表每页有90条数据

        # print(results)
        # 公司基本信息(包含信息：名称、所在城市、所在县区、办公地点、经纬度、规模、性质)
        company = [res.get('company').get('name') for res in results]    # 公司名称
        city = [res.get('city').get('items')[0].get('name')
                for res in results]    # 公司所在城市
        area = []    # 公司所在县区（许多招聘信息没有提供县区信息）

        for res in results:
            if len(res.get('city').get('items')) == 1:
                area.append(np.nan)
            else:
                area.append(res.get('city').get('items')[1].get('name'))
                businessArea = [res.get('businessArea') for res in results]    # 公司办公地点
                lon = [res.get('geo').get('lon') for res in results]           # 经度
                lat = [res.get('geo').get('lat') for res in results]           # 纬度
        size = [res.get('company').get('size').get('name') for res in results]    # 公司规模
        quality = [res.get('company').get('type').get('name') for res in results]          # 公司性质                   
        # 职位基本信息
        jobName = [res.get('jobName') for res in results]    # 职位名称
        emplType = [res.get('emplType') for res in results]  # 雇佣类型
        salary = [res.get('salary') for res in results]      # 薪水
        welfare = [res.get('welfare') for res in results]    # 福利
        recruitNum = []                                      # 招聘人数（在详情页获取）
        # 职位要求信息
        eduLevel = [res.get('eduLevel').get('name') for res in results]
        workingExp = [res.get('workingExp').get('name') for res in results]
        job_detail = []       # 职位详细描述信息

        detailURL = [res.get('positionURL') for res in results]    # 详情页URL
        # css选择器从详情页获取招聘人数及职位描述详细信息
        for u in detailURL:
            soup = BeautifulSoup(get_response(u, headers=headers).text, 'lxml')
            # 招聘人数
            recruitNum.append(soup.select(
                'body > div.wrap > div.main > div.main1.cl.main1-stat > div > ul > li.clearfix > div.info-three.l > span')[-1].text[1: -1])
            # 职位详情
            detail_info = soup.select(
                'body > div.wrap > div.main > div.pos-info.cl > div.l.pos-info-in > div.responsibility.pos-common > div.pos-ul')
            detail_info = detail_info[0].text.strip()
            pattern = '(\\xa0)| '
            st = re.sub(pattern, '', detail_info)    # 初步清洗文本数据
            job_detail.append(st)

        # 在页面随机停留5至20s
        time.sleep(random.randint(5, 20))

        # 保存每页的内容至page_info中
        page_info.append(pd.DataFrame({
            'company': company, 'city': city, 'area': area, 'businessArea': businessArea,
            'lon': lon, 'lat': lat, 'size': size, 'quality': quality,
            'jobName': jobName, 'emplType': emplType, 'salary': salary, 'recruitNum': recruitNum, 'welfare': welfare,
            'eduLevel': eduLevel, 'workingExp': workingExp, 'jobDetail': job_detail
        }))
        print('第{}页的信息获取完成！'.format(np.round((i/90)+1)))
    # 合并每一页的数据
    total_info = pd.concat(page_info)
    return total_info

def save_to_excel(path, total_info):
    total_info.to_excel(path, index=False)

def main(fileNum):
    max_num = 90 * 12
    step = 90
    path = 'HangzhouJobs_da{}.xlsx'.format(fileNum)
    print(path)
    total_info = parse_data(max_num, step)
    save_to_excel(path, total_info)
    print('爬取完成!')

if __name__ == "__main__":
    main('')