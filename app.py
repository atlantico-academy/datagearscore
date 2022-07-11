import streamlit as st
import pandas as pd
import joblib
from PIL import Image
import plotly.graph_objects as go


model = joblib.load('./models/best_model.joblib')

image = Image.open('Logo.jpg') 

st.set_page_config(
    page_title="Score DataGear",
    layout="centered",
    page_icon=image
 )

if 'n' not in st.session_state:
    st.session_state['n'] = 0

    
def clear_form():
    st.session_state["idade"] = 18
    st.session_state["marriage"] = 'casado'
    st.session_state["sex"] = 'feminino'
    st.session_state["education"] = 'pós-graduação'
    st.session_state["limit"] = 0.0
    st.session_state['n'] = 0

with st.form("myform"):
   
    col1, col2 = st.columns(2)

    col1.image(image, width=150)

    col2.title("Consulte seu Score DataGear")
    st.subheader("Insira as informações abaixo")
    col1, col2, col3, col4 = st.columns(4)
    age = col1.number_input(
        'Informe sua idade', min_value=18, max_value=120, value=18, step=1, key='idade'
    )
    option_marriage = col2.selectbox(
        'Escolha o seu estado civil', ('casado', 'solteiro', 'outros'), key='marriage'
    )
    option_sex = col3.selectbox(
        'Escolha o seu sexo', ('feminino', 'masculino'), key='sex'
    )
    option_education = col4.selectbox(
        'Escolha sua escolaridade',
         ('pós-graduação', 'universidade', 'ensino médio', 'outros'), key='education'
    )

    with st.expander('Informações adicionais'):
        limit_bal = st.number_input(
            'Limite do seu cartão de crédito', min_value=0.0, step=100.0, key='limit'
        )
        col1, col2, col3 = st.columns([.8, .05, .05])
        col1.info('Adicione detalhes das suas faturas anteriores')
        if col2.form_submit_button('+'):
            if st.session_state.n <= 5:
                st.session_state.n += 1
        if col3.form_submit_button('-'):
            if st.session_state.n >= 1:
                st.session_state.n -= 1  

        col1, col2, col3, col4 = st.columns([.4, .4, .1, .1])

        bill_amt = []
        pay_amt = []
        for i in range(st.session_state.n):
            bill_amt.append(col1.number_input(f'Total da fatura do {i+1}º mês', min_value=0.0, step=100.0))
            pay_amt.append(col2.number_input(f'Pagamento do {i+1}º mês', min_value=0.0, step=100.0))


    saldo = {key: value for key, value in enumerate(bill_amt)}
    pago = {key: value for key, value in enumerate(pay_amt)}


    x = pd.DataFrame({      
        'limite': [limit_bal],
        'sexo': [option_sex],
        'educacao': [option_education],
        'estado_civil': [option_marriage],
        'idade': [age],
        'saldo_0509': [saldo.get(0, None)],
        'saldo_0508': [saldo.get(1, None)], 
        'saldo_0507': [saldo.get(2, None)], 
        'saldo_0506': [saldo.get(3, None)],
        'saldo_0505': [saldo.get(4, None)], 
        'saldo_0504': [saldo.get(5, None)], 
        'pago_0509': [pago.get(0, None)], 
        'pago_0508': [pago.get(1, None)], 
        'pago_0507': [pago.get(2, None)],
        'pago_0506': [pago.get(3, None)], 
        'pago_0505': [pago.get(4, None)], 
        'pago_0504': [pago.get(5, None)]
    })

    predict_proba = model.predict_proba(x)
    
    col1, col2 = st.columns([8, 1.8])
    submit = col1.form_submit_button(label="Calcular Score")
    clear = col2.form_submit_button(label="Novo Cálculo", on_click=clear_form)

if submit:
    current_value = predict_proba[0][0]*1000
    min_value = 0
    max_value = 1000 
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        delta = {'reference': 600},
        value = current_value,
        gauge = {'axis': {'range': [min_value, max_value]},
                'bar': {'color': "darkblue"},
                'steps' : [
                    {'range': [0, 200], 'color': "red"},
                    {'range': [200, 600], 'color': "yellow"}],},
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Score DataGear"}))
    st.plotly_chart(fig, use_container_width=True)

if clear:
    x = pd.DataFrame()   
    
