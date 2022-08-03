#부산 갈맷길 정보 API 크롤링
from inspect import getgeneratorlocals
import os
from re import L
import sys
import urllib.request
import datetime
import time
import json
from django.http import JsonResponse
import pandas as pd

ServiceKey = 'uG4o2nY2aD7Go6B3N7ROW7I%2FI7Dc0ywfp%2BNPDgpV%2F9DshKHpJI6HxBuBmKUjxWv4kw0771ow8xT5%2BejwgDpRyw%3D%3D'

def getRequestUrl(url):
    #URL 접속 요청 후 응답함수
    #prameter : url -> OpenAPI 전체 URL
    req = urllib.request.Request(url)

    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200: # 200 OK 400대는 (일반적인)오류, 500대 서버오류
            print(f'[{datetime.datetime.now()}] Url Request success')
            return res.read().decode('utf-8')

    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL : {url}')
        return None

def getGalmatgilInfo():
    service_url = 'http://apis.data.go.kr/6260000/fbusangmgcourseinfo/getgmgcourseinfo'
    params = f'?serviceKey={ServiceKey}'
    params += '&numOfRows=10'
    params += '&pageNo=1'
    params += '&resultType=json'
    url = service_url + params

    retData = getRequestUrl(url)

    if retData == None:
        return None
    else:
        return json.loads(retData)

def getGalmatgilService():
    result = []

    jsonData = getGalmatgilInfo()
    # print(jsonData)
    if jsonData['getgmgcourseinfo']['header']['code']:
        if jsonData['getgmgcourseinfo']['item'] =='':
            print('서비스 오류!!!')
        else:
            for item in jsonData['getgmgcourseinfo']['item']:
                seq = item['seq']
                course_nm = item['course_nm']
                gugan_nm = item['gugan_nm']
                gm_range = item['gm_range']
                gm_degree = item['gm_degree']
                start_pls = item['start_pls']
                start_addr = item['start_addr']
                middle_pls = item['middle_pls']
                middle_adr = item['middle_adr']
                end_pls = item['end_pls']
                end_addr = item['end_addr']
                gm_course = item['gm_course']
                gm_text = item['gm_text']

                result.append([seq, course_nm, gugan_nm, gm_range, gm_degree, start_pls, start_addr, middle_pls, middle_adr, end_pls, end_addr, gm_course, gm_text])

    return result           

def main():
    result = []

    print('부산 갈맷길 코스를 조회합니다. ')
    result = getGalmatgilService()

    if len(result) > 0:
        # CSV 파일 저장
        columns = ['seq', 'course_nm', 'gugan_nm', 'gm_range', 'gm_degree', 'start_pls', 'start_addr', 'middle_pls', 'middle_adr', 'end_pls', 'end_addr', 'gm_course', 'gm_text']
        result_df= pd.DataFrame(result,columns=columns)
        result_df.to_csv(f'./부산갈맷길정보.csv',index=False,
                        encoding='utf-8') # 엑셀로 보고 싶다 cp949 csv로 보고 싶다 utf-8
        print('csv파일 저장완료!!')

if __name__=='__main__':
    main()