import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from site_pages.whoisclient import second_page

def first_page():
    st.header("1) Актуальность тематики", divider='green')
    st.write('Каждый из нас хоть раз сталкивался с досадной ситуацией, когда обсчитали на кассе. Впрочем, в случае с покупками, это несложно проверить, сверив цифры в чеке. Но что делать, если ошибка закралась в многотомную финансовую или налоговую отчетность? Тем более, если это не случайность, а намеренная фальсификация данных с целью мошенничества?')
    selected_1 = st.button('Следующая страница 2')
    if selected_1:
        second_page()
