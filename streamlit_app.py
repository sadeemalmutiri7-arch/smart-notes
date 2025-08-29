import streamlit as st

st.set_page_config(page_title="Smart Notes", page_icon="📝")

st.title("📒 مفكرتي الذكية")
st.write("مرحبًا بك في تطبيق تنظيم المهام اليومية!")

task = st.text_input("اكتبي مهمتك هنا:")
if st.button("أضف المهمة"):
    st.success(f"تمت إضافة المهمة: {task}")
  أول نسخة من التطبيق
