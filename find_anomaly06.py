import streamlit as st
import pickle as pkle
import os.path
import base64

from pathlib import Path
from streamlit_option_menu import option_menu
from site_pages import *

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(img_to_bytes(img_path))
    return img_html


st.set_page_config(page_title="Закон первой цифры", page_icon="👾", layout="wide")
if 'count_page' not in st.session_state:
    st.session_state['count_page'] = 0

def increment_counter():
    if st.session_state.count_page != 4:
        st.session_state.count_page += 1
    else:
        st.session_state.count_page = 0

with st.sidebar:
    redirect_url = "http://83.143.66.61:27369/"
    logo_image = 'C:\\PycharmProjects\\search_anomaly01\\venv\\images\\logo-lck100x100.png'
    #st.markdown(f'<a href="http://83.143.66.61:27369/"><img src="C:\\PycharmProjects\\search_anomaly01\\venv\\images\\logo-lck100x100.png" width="100" height="100"/></a>', unsafe_allow_html=True)
    st.markdown("<p style = 'text-align: center; color: grey;' > "+img_to_html(logo_image)+" </p> ", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu('',["1) Актуальность тематики", "2) Кто заинтересован в данной работе?", "3) Этапы разработки кейса", "4) Пример функционирования", "5) Вопросы по теме"], default_index=st.session_state.count_page)

if selected == "1) Актуальность тематики":
    st.session_state['count_page'] = 0
elif selected == "2) Кто заинтересован в данной работе?":
    st.session_state['count_page'] = 1
elif selected == "3) Этапы разработки кейса":
    st.session_state['count_page'] = 2
elif selected == "4) Пример функционирования":
    st.session_state['count_page'] = 3
elif selected == "5) Вопросы по теме":
    st.session_state['count_page'] = 4


if st.session_state.count_page == 0:
    first_page()
elif st.session_state.count_page == 1:
    second_page()
elif st.session_state.count_page == 2:
    third_page()
elif st.session_state.count_page == 3:
    fourth_page()
elif st.session_state.count_page == 4:
    fifth_page()


if st.button('Следующая страница'):
    increment_counter()
