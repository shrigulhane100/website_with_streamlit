import streamlit as st
import time

st.write(""""""
         # Subtraction of two given numbers
         """""")
st.header('Calculate subtraction of two number.')


def user_input():
    numnber_1 = st.number_input('Number 1:', min_value=1, max_value=10000000)
    numnber_2 = st.number_input('Number 2:', min_value=1, max_value=10000000)
 
    st.button('Subtract')
    st.write("Subtraction of number is :", numnber_1 - numnber_2)

    
user_input()
