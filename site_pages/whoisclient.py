import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from site_pages.structure import third_page

def second_page():

    st.subheader("2) Кто заинтересован в данной работе?", divider='green')
    st.write('* студентам финансовых и экономических специальностей;\n'
             '* студентам направления аналитики и консалтинга;\n'
             '* студентам маркетинговых направлений;\n'
             '* научным сотрудникам.')
    selected_2 = st.button('Следующая страница 3')
    if selected_2:
        third_page()