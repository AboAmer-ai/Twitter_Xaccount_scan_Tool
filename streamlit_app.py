import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="Twitter Trending Hashtags", layout="wide")
st.title("الهاشتاجات المتصدرة على تويتر 🌟")

# اختيار الدولة
country = st.radio("اختر الدولة:", ["Worldwide", "Egypt", "USA", "UK"])

# روابط المواقع حسب الدولة
urls = {
    "Worldwide": "https://trends24.in/",
    "Egypt": "https://trends24.in/egypt/",
    "USA": "https://trends24.in/united-states/",
    "UK": "https://trends24.in/united-kingdom/"
}

# جلب الترندات
url = urls[country]
try:
    response = requests.get(url)
    response.raise_for_status()  # للتأكد من نجاح الطلب
    soup = BeautifulSoup(response.text, "html.parser")
    trends = [tag.text.strip() for tag in soup.find_all("a", class_="trend-card__name")]

    # عرض النتائج
    if trends:
        df = pd.DataFrame(trends, columns=["Hashtags"])
        st.table(df)
    else:
        st.warning("لم يتم العثور على ترندات حالياً 😅")

except Exception as e:
    st.error(f"حدث خطأ أثناء جلب الترندات: {e}")
