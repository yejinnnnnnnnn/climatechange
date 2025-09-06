import streamlit as st
import pandas as pd

st.title('🌡️ 날짜별 기후 변화 시각화')
st.markdown('웹에 게시된 데이터를 바탕으로 연월별 기온 변화를 그래프로 나타냅니다.')

# 웹에 게시된 CSV 파일의 URL을 입력합니다.
# GitHub의 'blob' URL은 '?raw=true'를 추가해야 원본 데이터를 불러올 수 있습니다.
url = "https://github.com/yejinnnnnnnnn/-/blob/main/data.csv.csv" + "?raw=true"

try:
    # 1. URL에서 CSV 데이터 불러오기
    df = pd.read_csv(url, encoding='cp949')

    # 2. 데이터 전처리
    # '연월' 열을 날짜 형식으로 변환 (e.g., 'Jan-21' -> 2021-01-01)
    df['연월'] = pd.to_datetime(df['연월'], format='%b-%y')
    
    # '최고기온', '최저기온', '기온편차' 열을 숫자로 변환
    df['최고기온'] = pd.to_numeric(df['최고기온'], errors='coerce')
    df['최저기온'] = pd.to_numeric(df['최저기온'], errors='coerce')
    df['기온편차'] = pd.to_numeric(df['기온편차'], errors='coerce')
    
    # 날짜 순으로 정렬
    df = df.sort_values(by='연월')

    # 3. Streamlit으로 시각화
    st.header('📈 최고/최저 기온 추이')
    temp_data_for_chart = df[['연월', '최고기온', '최저기온']].set_index('연월')
    st.line_chart(temp_data_for_chart)

    st.header('📊 기온 편차 추이')
    st.bar_chart(df.set_index('연월')['기온편차'])

    st.subheader('🔍 원본 데이터')
    st.dataframe(df)

except Exception as e:
    st.error(f"데이터를 불러오는 데 오류가 발생했습니다: {e}")
    st.info("URL이 올바른지, 파일이 공개 설정인지 확인해주세요.")
