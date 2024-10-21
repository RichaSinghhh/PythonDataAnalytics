# Terminal -> streamlit run file-name -> (like Calculator.py)
import streamlit as st

st.title("Calculator")
st.markdown("Welcome to my first streamlit app")

c1, c2 = st.columns(2)
fnum = c1.number_input("Enter first number", value = 1)
snum = c2.number_input("Enter second number", value = 0)

options = ['Add', 'Subtract', 'Multiply', 'Divide']
choice = st.radio("Select operation", options)

button = st.button ("Calculator")

if button :
    if choice == 'Add':
        result = fnum + snum
    if choice == 'Subtract':
        result = fnum - snum
    if choice == 'Multiply':
        result = fnum * snum
    if choice == 'Divide':
        result = fnum / snum

st.success(f"The result is {result}")


        





