'''
import requests
import streamlit as st
import xml.etree.ElementTree as ET

# 🔑 API Key (코드에 직접 삽입)
API_KEY = "uIYKKROcKMqB9rev3vsyJMh9o15YJDYGeH%2FVE2DdTl3DGaynT%2FnzprNZdJ7uTsgThA88DwdSyh4dL%2BXLOwVydA%3D%3D"  # 여기 YOUR_API_KEY를 실제 API 키로 변경하세요.

# API 호출 함수
def get_bus_info(station_id, bus_route_id, ord):
    url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?serviceKey={API_KEY}&stId={station_id}&busRouteId={bus_route_id}&ord={ord}"
    response = requests.get(url)
    st.text(response.text)

    if response.status_code == 200:
        root = ET.fromstring(response.content)  # XML 파싱

        # XML 구조에서 <item> 태그 안의 정보 추출
        results = []
        for item in root.findall(".//item"):
            bus_number = item.findtext("rtNm", "정보 없음")  # 버스 번호
            station_name = item.findtext("stationNm", "정보 없음")  # 정류장 이름
            arrival_time = item.findtext("arrmsg1", "도착 정보 없음")  # 도착 예정 시간
            results.append(f"🚍 {bus_number}번 버스 ({station_name})\n도착 예정: {arrival_time}")

        return "\n\n".join(results) if results else "버스 도착 정보 없음"
    else:
        return "API 요청 실패"

# Streamlit UI
st.title("서울 버스 도착 정보")

# 입력 받기
station_id = st.text_input("📍 정류소 ID 입력", "119000070")
bus_route_id = st.text_input("🚌 버스 노선 ID 입력", "100100097")
ord = st.text_input("📌 정류소 순번 입력", "55")

if st.button("🔍 조회하기"):
    result = get_bus_info(station_id, bus_route_id, ord)
    st.text(result)
'''


import requests
import xml.etree.ElementTree as ET
import streamlit as st

# ✅ API 요청 (디코딩된 API 키 사용)
API_KEY = "uIYKKROcKMqB9rev3vsyJMh9o15YJDYGeH/VE2DdTl3DGaynT/nzprNZdJ7uTsgThA88DwdSyh4dL+XLOwVydA=="  # 여기에 디코딩된 인증키 입력
URL = "http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute"

params = {
    "serviceKey": API_KEY,
    "stId": "119000070",  # 정류소 ID
    "busRouteId": "100100097",  # 버스 노선 ID
    "ord": "55"  # 정류소 순번
}



# ✅ Streamlit 제목
st.title("📍 서울 버스 도착 정보")

if st.button("버스 도착 정보 조회"):
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        root = ET.fromstring(response.content)

        # ✅ API 응답 상태 확인
        header_cd = root.findtext(".//headerCd")
        if header_cd != "0":
            st.error("❌ 오류 발생: API 응답 실패")
        else:
            item = root.find(".//itemList")  # 첫 번째 도착 정보만 가져오기
            if item is not None:
                # ✅ XML 데이터 파싱
                bus_number = item.findtext("rtNm", "정보 없음")  # 버스 번호
                station_name = item.findtext("stNm", "정보 없음")  # 정류소 이름
                arrival_time_1 = item.findtext("arrmsg1", "도착 정보 없음")  # 첫 번째 도착 예정 시간
                arrival_time_2 = item.findtext("arrmsg2", "도착 정보 없음")  # 두 번째 도착 예정 시간
                bus_plate_1 = item.findtext("plainNo1", "정보 없음")  # 첫 번째 버스 차량번호
                bus_plate_2 = item.findtext("plainNo2", "정보 없음")  # 두 번째 버스 차량번호

                # ✅ Streamlit UI에 출력
                st.success(f"📍 **정류소:** {station_name}")
                st.subheader(f"🚌 **{bus_number}번 버스 도착 정보**")
                st.write(f"🚍 첫 번째 버스: **{arrival_time_1}** ({bus_plate_1})")
                st.write(f"🚍 두 번째 버스: **{arrival_time_2}** ({bus_plate_2})")
            else:
                st.warning("해당 정류소에는 버스 도착 정보가 없습니다.")
    else:
        st.error("❌ API 요청 실패")