import streamlit as st
from PIL import Image




if 'n' not in st.session_state:
    st.session_state['n'] = 0

image = Image.open('Logo.jpg')    
    
st.set_page_config(
    page_title="Score DataGear",
    layout="centered",
    page_icon=image
 )

col1, col2 = st.columns(2)
    
col1.image(image, width=150)
    
col2.title("Consulte seu Score DataGear")
st.subheader("Insira as informações abaixo")
col1, col2, col3, col4 = st.columns(4)
age = col1.number_input(
    'Informe sua idade', min_value=18, max_value=120, value=18, step=1
)
option_marriage = col2.selectbox(
    'Escolha o seu estado civil', ('Casado', 'Solteiro', 'Outros')
)
option_sex = col3.selectbox('Escolha o seu sexo', ('Feminino', 'Masculino'))
option_education = col4.selectbox(
    'Escolha sua escolaridade',
     ('Pós graduação', 'Universidade', 'Ensino Médio', 'Outros')
)

with st.expander('Informações adicionais'):
    limit_bal = st.number_input('Limite do seu cartão de crédito', min_value=0.0, step=100.0)
    
    col1, col2, col3 = st.columns([.8, .05,.05])
    col1.info('Adicione detalhes das suas faturas anteriores')
    if col2.button('+'):
        if st.session_state.n <= 5:
            st.session_state.n += 1
    if col3.button('-'):
        if st.session_state.n >= 1:
            st.session_state.n -= 1  
    
    
    col1, col2, col3, col4 = st.columns([.4, .4, .1, .1])
    
    bill_amt = []
    pay_amt = []
    for i in range(st.session_state.n):
        bill_amt.append(col1.number_input(f'Total da fatura do {i+1}º mês', min_value=0.0, step=100.0))
        pay_amt.append(col2.number_input(f'Pagamento do {i+1}º mês', min_value=0.0, step=100.0))
    

        
if st.button('Calcular score'):
    st.text(bill_amt)
    st.text(pay_amt)