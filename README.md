import streamlit as st

st.set_page_config(page_title="Smart Notes", page_icon="📝")

st.title("نظام الملاحظات الذكي")

task = st.text_input("أدخل مهمتك هنا (بالعربية)")

if st.button("إضافة المهمة"):
    st.success("تمت إضافة المهمة بنجاح: " + task)
