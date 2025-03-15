
import streamlit as st
import requests
import xml.etree.ElementTree as ET

# API 기본 정보
BASE_URL = "http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute"
SERVICE_KEY = st.secrets["API_KEY"]  # Streamlit Cloud 배포 시 secrets.toml 사용

# 조회할 버스 노선 정보 (노선 ID, 정류소 ID)
# 상도전통시장 650, 641
bus_routes_1 = [
    {"busRouteId": "100100097", "stId": "119000070", "ord": "55", "name": "650번"},
    {"busRouteId": "100100094", "stId": "119000070", "ord": "77", "name": "641번"},
]
# 래미안중문 5511
bus_routes_2 = [
    {"busRouteId": "100100250", "stId": "119000317", "ord": "33", "name": "5511번"}
]
# 금양빌딩 5511
bus_routes_3 = [
    {"busRouteId": "100100250", "stId": "119000316", "ord": "45", "name": "5511번"}
]
# Streamlit UI
#st.title("🚍 버스 도착 정보")
st.subheader("🚍 버스 도착 정보")

#st.write("서울시 공공데이터 API를 활용한 버스 도착 시간 조회")

# 버튼 추가
if st.button("도착 정보 조회(상도전통시장 650,641) 🚀"):
    bus_info_list = []

    for route in bus_routes_1:
        params = {
            "serviceKey": SERVICE_KEY,
            "stId": route["stId"],
            "busRouteId": route["busRouteId"],
            "ord": route["ord"],
        }
        response = requests.get(BASE_URL, params=params)

        # XML 데이터 파싱
        root = ET.fromstring(response.content)
        arrmsg1 = root.find(".//arrmsg1").text  # 첫 번째 도착 정보
        arrmsg2 = root.find(".//arrmsg2").text  # 두 번째 도착 정보

        bus_info_list.append({
            "노선": route["name"],
            "첫 번째 도착": arrmsg1,
            "두 번째 도착": arrmsg2,
        })

    # DataFrame 형태로 출력
    st.table(bus_info_list)

# 버튼 추가
if st.button("도착 정보 조회(래미안중문(중대방향) 5511) 🚀"):
    bus_info_list = []

    for route in bus_routes_2:
        params = {
            "serviceKey": SERVICE_KEY,
            "stId": route["stId"],
            "busRouteId": route["busRouteId"],
            "ord": route["ord"],
        }
        response = requests.get(BASE_URL, params=params)

        # XML 데이터 파싱
        root = ET.fromstring(response.content)
        arrmsg1 = root.find(".//arrmsg1").text  # 첫 번째 도착 정보
        arrmsg2 = root.find(".//arrmsg2").text  # 두 번째 도착 정보

        bus_info_list.append({
            "노선": route["name"],
            "첫 번째 도착": arrmsg1,
            "두 번째 도착": arrmsg2,
        })

    # DataFrame 형태로 출력
    st.table(bus_info_list)

# 버튼 추가
if st.button("도착 정보 조회(금양빌딩(숭실대방향) 5511) 🚀"):
    bus_info_list = []

    for route in bus_routes_3:
        params = {
            "serviceKey": SERVICE_KEY,
            "stId": route["stId"],
            "busRouteId": route["busRouteId"],
            "ord": route["ord"],
        }
        response = requests.get(BASE_URL, params=params)

        # XML 데이터 파싱
        root = ET.fromstring(response.content)
        arrmsg1 = root.find(".//arrmsg1").text  # 첫 번째 도착 정보
        arrmsg2 = root.find(".//arrmsg2").text  # 두 번째 도착 정보

        bus_info_list.append({
            "노선": route["name"],
            "첫 번째 도착": arrmsg1,
            "두 번째 도착": arrmsg2,
        })

    # DataFrame 형태로 출력
    st.table(bus_info_list)

