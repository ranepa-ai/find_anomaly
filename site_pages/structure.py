import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from site_pages.example import fourth_page

def third_page():
    st.subheader('Этапы разработки кейса',divider='green')
    st.write('Подготовка набора данных -> Выделение текста из документов при помощи ИИ -> Анализ текста и выделение чисел при помощи ИИ -> Визуализация данных')
    selected_3 = st.button('Следующая страница 4')
    if selected_3:
        fourth_page()
