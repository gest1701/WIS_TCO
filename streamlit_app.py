import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Watts In Store TCO calculator",  # Title that appears in the browser tab
    page_icon="https://wattsinstore.nl/wp-content/themes/watts/favicon/favicon-32x32.png",         # Icon that appears in the browser tab (optional)
    layout="centered",                  # Layout options: 'centered' or 'wide'
)

st.image('https://wattsinstore.nl/wp-content/uploads/2024/02/Logo-WattsInStore.svg',width=400,caption='Watts In Store TCO calculator')


col1,col2,col3,col4 = st.columns(4)

with col1:
    st.write('**Elektrisch**', )
    aantal_e = st.number_input(label='Aantal e-trucks',min_value=1,step=1,key='aantal_e')
    prijs_e = st.number_input(label='Aanschafprijs',
                              min_value=50000,max_value=500000,
                              step=10000,value=350000,
                              key='prijs_e')
    jaren_e = st.number_input(label='Jaren inzetbaar',
                              min_value=1,max_value=25,
                              step=1,value=5,
                              key='jaren_e')
    afschrijving_e = st.number_input(label='Afschrijving per jaar (percentage)',
                              min_value=1.0,max_value=99.0,
                              step=1.0,value=25.0,
                              key='afschrijving_e')/100
    restwaarde_e = (aantal_e * prijs_e) * (1-afschrijving_e)**jaren_e
    st.write(f'Restwaarde na {jaren_e} jaar € {restwaarde_e:,.2f}.')

with col2:
    for r in range(10):
        st.write(' ')
    st.write(f'Totaal € {aantal_e*prijs_e}')
with col3:
    st.write('**Diesel**', )
    aantal_d = st.number_input(label='Aantal diesel trucks',min_value=1,step=1,key='aantal_d')
    prijs_d = st.number_input(label='Aanschafprijs',
                              min_value=50000,max_value=500000,
                              step=10000,value=125000,
                              key='prijs_d')
with col4:
    for r in range(10):
        st.write(' ')
    st.write(f'Totaal € {aantal_d*prijs_d}')