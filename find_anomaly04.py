import streamlit as st
import pickle as pkle
import os.path
from streamlit_option_menu import option_menu
from site_pages import *


pages = ["1) Актуальность тематики","2) Кто заинтересован в данной работе?","3) Этапы разработки кейса","4) Пример функционирования","5) Вопросы по теме"]

if os.path.isfile('next.p'):
    next_clicked = pkle.load(open('next.p', 'rb'))
    if next_clicked == len(pages):
        next_clicked = 0
else:
    next_clicked = 0

if next:
    next_clicked = next_clicked+1
    if next_clicked == len(pages):
        next_clicked = 0

st.set_page_config(page_title="Поиск аномалий в отчетности.")
st.header('Поиск аномалий в отчетности.')
st.write('Применение закона первой цифры (Закон Бенфорда) для аудита финансовой отчетности')

#with st.sidebar:
#    selected = option_menu('',["1) Актуальность тематики","2) Кто заинтересован в данной работе?",
#                               "3) Этапы разработки кейса","4) Пример функционирования","5) Вопросы по теме"],index=next_clicked)

selected = st.sidebar.radio("Содержание",('1) Актуальность тематики','2) Кто заинтересован в данной работе?', '3) Этапы разработки кейса','4) Пример функционирования','5) Вопросы по теме'), index=next_clicked)
pkle.dump(pages.index(selected), open('next.p', 'wb'))

if selected == "1) Актуальность тематики":
    first_page()
elif selected == "2) Кто заинтересован в данной работе?":
    second_page()
elif selected == "3) Этапы разработки кейса":
    third_page()
elif selected == "4) Пример функционирования":
    fourth_page()
elif selected == "5) Вопросы по теме":
    fifth_page()


next = st.button('Следующая страница')