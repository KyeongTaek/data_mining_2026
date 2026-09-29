# Python3 Sample Code

import urllib.request

import os
from dotenv import load_dotenv

load_dotenv()

service_url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

parameters = "?_type=json&serviceKey=" + os.getenv('SERVICE_KEY') + "&YM=201201&NAT_CD=112&ED_CD=E"
alt_parameters = "?_type=json&serviceKey=" + os.getenv('ALT_SERVICE_KEY') + "&YM=201201&NAT_CD=112&ED_CD=E"

#url = service_url + parameters
url = service_url + alt_parameters

#params = {'serviceKey': os.getenv('SERVICE_KEY'), 'YM': '201201', 'NAT_CD': '112', 'ED_CD': 'E'}
#alt_params = {'serviceKey': os.getenv('ALT_SERVICE_KEY'), 'YM': '201201', 'NAT_CD': '112', 'ED_CD': 'E'}

retData = None

req = urllib.request.Request(url)
try:
    resp = urllib.request.urlopen(req)
    if resp.getcode() == 200:
        print("Url Request Success")
        retData = resp.read().decode('utf-8')
    else:
        print("Request Not Successful(%d)" % resp.getcode())
        exit
except Exception as e:
    print(e)
    exit

print(retData)
