import re
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from DataClass import DataClass
import folium
import webbrowser

u = urllib.request.urlopen(
    "https://openapi.gg.go.kr/EmgMedInfo?KEY=685efddff2354c78a02c17e9c9453169&Type=xml&pSize=1000")

soup = BeautifulSoup(u, 'html.parser')
print(soup)
base = []
base = [DataClass() for i in range(0, 1000)]

Sum_des = soup.findAll('sum_de')
Distrct_div_nms = soup.findAll('distrct_div_nm')
Medcare_inst_nms = soup.findAll('medcare_inst_nm')
Emgncy_center_telnos = soup.findAll('emgncy_center_telno')
Refine_lotno_addrs = soup.findAll('refine_lotno_addr')
Refine_roadnm_addrs = soup.findAll('refine_roadnm_addr')
Refine_wgs84_logts = soup.findAll('refine_wgs84_logt')
Refine_wgs84_lats = soup.findAll('refine_wgs84_lat')

cnt = 0
for sum_de in Sum_des:
    sum_de = re.sub('<.*?>', '|', sum_de.text)
    base[cnt].in_sum_de(sum_de)
    cnt = cnt + 1
cnt = 0
for distrct_div_nm in Distrct_div_nms:
    distrct_div_nm = re.sub('<.*?>', '|', distrct_div_nm.text)
    base[cnt].in_distrct_div_nm(distrct_div_nm)
    cnt = cnt + 1
cnt = 0
for medcare_inst_nm in Medcare_inst_nms:
    medcare_inst_nm = re.sub('<.*?>', '|', medcare_inst_nm.text)
    base[cnt].in_medcare_inst_nm(medcare_inst_nm)
    cnt = cnt + 1
cnt = 0
for emgncy_center_telno in Emgncy_center_telnos:
    emgncy_center_telno = re.sub('<.*?>', '|', emgncy_center_telno.text)
    base[cnt].in_emgncy_center_telno(emgncy_center_telno)
    cnt = cnt + 1
cnt = 0
for refine_lotno_addr in Refine_lotno_addrs:
    refine_lotno_addr = re.sub('<.*?>', '|', refine_lotno_addr.text)
    base[cnt].in_refine_lotno_addr(refine_lotno_addr)
    cnt = cnt + 1
cnt = 0
for refine_roadnm_addr in Refine_roadnm_addrs:
    refine_roadnm_addr = re.sub('<.*?>', '|', refine_roadnm_addr.text)
    base[cnt].in_refine_roadnm_addr(refine_roadnm_addr)
    cnt = cnt + 1
cnt = 0
for refine_wgs84_logt in Refine_wgs84_logts:
    refine_wgs84_logt = re.sub('<.*?>', '|', refine_wgs84_logt.text)
    base[cnt].in_refine_wgs84_logt(refine_wgs84_logt)
    cnt = cnt + 1
cnt = 0
for refine_wgs84_lat in Refine_wgs84_lats:
    refine_wgs84_lat = re.sub('<.*?>', '|', refine_wgs84_lat.text)
    base[cnt].in_refine_wgs84_lat(refine_wgs84_lat)
    cnt = cnt + 1

map_osm = folium.Map(location=[37.568477, 126.981611], zoom_start=10)
popup = folium.Popup(max_width=650)

for x in range(1000):
    folium.Marker([base[x].out_refine_wgs84_lat(), base[x].out_refine_wgs84_logt()],
                  popup= '<div style="border:0.5px solid silver; white-space:nowrap; width:250px;">' + '<center>'+ base[x].out_sum_de() +
                         '<br><br>' + base[x].out_distrct_div_nm() + '<br><br>' +
                        base[x].out_medcare_inst_nm() + '<br><br>' + base[x].out_emgncy_center_telno() +
                        '<br><br>' + base[x].out_refine_lotno_addr() + '<br><br>' +
                        base[x].out_refine_roadnm_addr() + '</center>'+'</div>').add_to(map_osm)

map_osm.save('.\\경기도 코로나 진료소 현황.html')
webbrowser.open('.\\경기도 코로나 진료소 현황.html')  # web browser에 저장된 지도 띄우기
