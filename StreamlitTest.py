# Online Python - IDE, Editor, Compiler, Interpreter
import streamlit as st

st.write("""
#Welcome to the print machine
This is the first Streamlit test
""")
a = 1
b = 2
def sum(a, b):
    return (a + b)

print(f'Sum of {a} and {b} is {sum(a, b)}')
