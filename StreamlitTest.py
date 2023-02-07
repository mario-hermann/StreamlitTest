# Online Python - IDE, Editor, Compiler, Interpreter
import streamlit as st
# Applicant Recommendation System (ARS)
# written by Mario Hermann, Katowice/Poland in February 2023

#from matplotlib import pyplot as plt
#from tabulate import tabulate
import random

import time
import datetime
#from pathlib import Path
import sys
st.write("Welcome to system 1.1")
time.sleep(3)
st.write("The input field comes now...")
time.sleep(3)
a = st.text_input("Please enter something: ")
time.sleep(2)
st.write(a)
i = 1
a = st.camera_input("Please take aphoto")
counter = 1
while True:
  a = random.random()
  i += a*i
  
  st.write("Aktuelle Zufallszahl: " + str(a))
  st.write("Hallo, dies ist Durchgang: " + str(counter))
  time.sleep(0.000001)
  if counter == 100:
    break
  counter +=1
