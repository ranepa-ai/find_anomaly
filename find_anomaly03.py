import os
import streamlit as st
import pandas as pd
import numpy as np
import base64
from streamlit_option_menu import option_menu
from site_pages import *

#@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''<p style='text-align:center; color:grey;'> <a href="{target_url}">  <img src="data:image/{img_format};base64,{bin_str}" />  </a></p>'''
    return html_code


# Заголовок приложения
#st.title("""Поиск аномалий в отчетности.""")
st.set_page_config(page_title="Поиск аномалий в отчетности.")

#Картинка слева
with st.sidebar:
    redirect_url = "http://83.143.66.61:27369/"
    logo_image = '/home/nikolas/find_anomaly03/venv/images/logo-lck100x100.png'
    logo_html_100100 = get_img_with_href(logo_image, redirect_url)
    st.markdown(logo_html_100100, unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu('',["1) Актуальность тематики","2) Кто заинтересован в данной работе?",
                               "3) Этапы разработки кейса","4) Пример функционирования","5) Вопросы по теме"])

if selected == "1) Актуальность тематики":
    first_page()
elif selected == "2) Кто заинтересован в данной работе?":
    second_page()
elif selected == "3) Этапы разработки кейса":
    third_page()

