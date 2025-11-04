import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.set_page_config(page_title="Twitter Trending Hashtags", layout="wide")
st.title("الهاشتاجات المتصدرة على تويتر 🌟")

country = st.radio("اختر الدولة:", ["Worldwide", "Egypt", "USA", "UK"])

urls = {
    "Worldwide": "https://trends24.in/",
    "Egypt": "https://trends24.in/egypt/",
    "USA": "https://trends24.in/united-states/",
    "UK": "https://trends24.in/united-kingdom/"
}

url = urls[country]

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # بعض الصفحات الجديدة تستخدم div بدل a
    trend_tags = soup.select(".trend-card__list a") or soup.select(".trend-card__list li a")
    trends = [tag.get_text(strip=True) for tag in trend_tags if tag.get_text(strip=True)]

    if trends:
        df = pd.DataFrame(trends, columns=["Hashtags"])
        st.success(f"تم العثور على {len(trends)} ترند 🎉")
        st.table(df)
    else:
        st.warning("لم يتم العثور على ترندات حالياً 😅")

except Exception as e:
    st.error(f"حدث خطأ أثناء جلب الترندات: {e}")
