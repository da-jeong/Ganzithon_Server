from django.shortcuts import get_object_or_404, get_list_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests, json

from .models import CityDetail

def city_list(request):
    # CityDetail 모델의 모든 레코드 가져오기
    city_details = CityDetail.objects.all()

    # 템플릿으로 전달할 context 데이터 설정
    context = {'city_details': city_details}

    # render 함수를 사용하여 city_list.html 템플릿을 렌더링하고, context 데이터 전달
    return render(request, 'city_list.html', context)


# API_KEY = settings.API_KEY

# @api_view(['GET'])
# def products(request):
#     url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
#     params = {
#         'auth': API_KEY,
#         'topFinGrpNo': '020000',
#         'pageNo': '1'
#     }
#     response = requests.get(url, params=params)
#     products_data = response.json()['result']['baseList']
    
#     return Response(products_data)

# def VilageFcstInfoService():
#     encodingKey = "{인코딩 key값}"
#     decodingKey = "{디코딩 key값}"

#     # request url 정의
#     url = "https://api.vworld.kr/req/data"
#     request = urllib.request.Request(url)

#     # request 요청
#     response = urllib.request.urlopen(request)

#     # response 결과
#     rescode = response.getcode()

#     if (rescode == 200): # 요청 결과 성공시에만
#         response_body = response.read()
#         res = xml.dom.minidom.parseString(response_body.decode('utf-8'))
#         pretty_res = res.toprettyxml()
#         print(pretty_res)
#     else: # 실패시 -> 에러코드 출력
#         print("Error Code:" + rescode)

# import urllib.parse as par
# import urllib.request as req

# if 
# ``
# url = "https://api.vworld.kr/req/data?service=data&request=GetFeature&data=LT_C_ADSIGG_INFO&key=0744834F-6E5B-3116-BFEE-3A20AD80BB6F&"
# params = {
#             'LAWD_CD': area,
#             'DEAL_YMD': year + month
#          }
# param = par.urlencode(params)
# url = url + param
# data = req.urlopen(url).read()
