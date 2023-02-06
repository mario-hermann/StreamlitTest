# Online Python - IDE, Editor, Compiler, Interpreter
import streamlit as st

st.write("""
#Welcome to the print machine
This is the first Streamlit test
""")
def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
