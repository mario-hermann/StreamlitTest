# Online Python - IDE, Editor, Compiler, Interpreter
import streamlit as st
# Applicant Recommendation System (ARS)
# written by Mario Hermann, Katowice/Poland in February 2023

#from matplotlib import pyplot as plt
#from tabulate import tabulate
import time
import datetime
#from pathlib import Path
import sys

DELAY = 1
L = "_"*70
    
class HiringCompany:
    def __init__(self,companyname,headquarters,industry,marketposition,corporateculture):
        self.companyname = companyname
        self.headquarters = headquarters
        self.industry = industry
        self.marketposition = marketposition
        self.corporateculture = corporateculture
        

class Applicant:
    def __init__(self,name,nationality,company,jobposition,joblocation,possiblestartdate,v1,v2,v3,v4,v5):
        self.name = name
        self.nationality = nationality
        self.company = company
        self.jobposition = jobposition
        self.joblocation = joblocation
        self.possiblestartdate = possiblestartdate
        self.value1 = v1 
        self.value2 = v2
        self.value3 = v3
        self.value4 = v4
        self.value5 = v5

        
Mario = Applicant("Mario Hermann","german","Bentley Systems", "Technical Support Engineer with German/English/French",
                  "Krakow (Poland)","01 March 2023","Qualified as Mechanical Engineer (Dipl.-Ing. FH) and\nInterdisciplinary Environmental Scientist (M.Sc.)",
                  "Strong affinity towards IT topics such as Python and SQL","Multilingual personality with German (native), English and French language proficiency",
                  "Vast international and intercultural experience","Strong communication skills, acquired e.g. through acting as official CERN visitors guide")

BentleySystems = HiringCompany("Bentley Systems, Inc.", "685 Stockton Dr, Exton, PA 19341 (USA)", "Infrastructure Engineering Software",
                               "Market leader", "Excellent")

LINKEDIN_LINK = "https://www.linkedin.com/in/mario-hermann/"
SOURCECODE_LINK = "https://www.linkedin.com/in/mario-hermann/XXXXXX"
APPLICATION_LINK = "https://www.applicantRS.com"


def color1(skk): 
        st.write("\033[92m{}\033[00m" .format(skk))

        
def color2(skk): 
        st.write("\033[92m{}\033[00m" .format(skk)) 

        
def message_l_color1(messagetext):
        color1(L + "\n\n\n" + messagetext + "\n\n" +  L + "\n")
        time.sleep(DELAY)

        
def message_m_color2(messagetext):
        color2(L + "\n\n" + messagetext + "\n" +  L + "\n")
        time.sleep(DELAY)

"""        
def userinput():
        ui = st.text_input('Please enter sth.')
        time.sleep(DELAY)
        color1("... processing ...")
        time.sleep(DELAY)
        message_m_color2("Your selection: " + ui)
        time.sleep(DELAY)
        return ui


def printUTCdatetime():
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())    
        message_m_color2("ARS date and time (UTC): " + current_time)
"""
"""

        
def company_info():
        message_m_color2("The following information about " + BentleySystems.companyname + "\nis stored in the ARS database:")
        company = [["Name of organization:",BentleySystems.companyname],
                  ["Global headquarters:",BentleySystems.headquarters],
                  ["Industry:",BentleySystems.industry],
                  ["Market position:",BentleySystems.marketposition],
                  ["Corporate culture:",BentleySystems.corporateculture]
                  ]
        color1(tabulate(company))
        time.sleep(DELAY)
        

def contribution(u):
        message_m_color2("Dear " + u + ", according to the ARS database information,\nthe candidate Mr. " + Mario.name +"\nwill contribute the following skills and experiences to the\nsuccess of " + BentleySystems.companyname + ":")
        contribution = [["1:", Mario.value1],
                        ["2:", Mario.value2],
                        ["3:", Mario.value3],
                        ["4:", Mario.value4],
                        ["5:", Mario.value5]
                       ]
        color1(tabulate(contribution))
        time.sleep(DELAY)
"""

def applicant_recommendation_system():
        message_l_color1("Welcome to the 3ELEPHANTS auto-promotion \nApplicant Recommendation System (ARS) -Version 3.9-")
        
        printUTCdatetime()
        
        message_m_color2("In order to use the Applicant Recommendation System,\nplease choose a session name:")
        u1 = "Mario"
        message_m_color2("Hi " + u1 + ", nice that you are using the Applicant Recommendation System today.")
        
        #company_info()
        
        message_m_color2("Dear " + u1 + ",\nthe ARS has identified 1 promising\nnew entry with possible start date " + Mario.possiblestartdate + " for the position\n\n" + Mario.jobposition + ",\nbased in " + Mario.joblocation + "\n\nin its applicant database.")
        message_m_color2("Do you want to get to know more about this candidate? [Yes/No]")
        u2 = st.text_input('Please enter sth.')
        u2 = u2.casefold()
        
        while True:
            if u2=="yes" or u2=="y":
                break  
            else:
                message_m_color2("Oops! ... this entry was totally unexpected ...\n\nPlease give it another try ...\n\nThe ARS strongly suggests to continue with a positive input ...\n\nPlease try again with 'YES' or 'Yes' or 'y' or 'Y' ...")
                u2 = userinput()
                u2 = u2.casefold()
       
        message_m_color2("Congratulations " + u1 + ", you want to get to know more about the candidate.")
        
        #contribution(u1)
        
        #image_grid()
        
        message_m_color2("END OF CANDIDATE ANALYSIS")
        message_m_color2("Dear " + u1 + ", the ARS dataset analysis of the applicant suggests,\nthat Mr. " + Mario.name + " might be a valuable candidate and future \ncolleague of yours at " + BentleySystems.companyname + "\n\nThus, the ARS recommends, to consider Mr. " + Mario.name + "\nfor a role at " + BentleySystems.companyname)
        message_m_color2("For further inquiries, you may contact Mr. " + Mario.name + "\nvia his LinkedIn profile " + LINKEDIN_LINK)
        message_m_color2("We thank you for using the ARS and wish you a nice day.")
        message_m_color2("SYSTEM SHUTDOWN")
        message_m_color2("p.s.\nIf you are interested, what is going on in the background while\nusing this ARS, check the Python source code by me, " + Mario.name + " here:\n" + SOURCECODE_LINK)       
        message_m_color2("p.s.s.\nIf you like this application and you want to support me,\nfeel free to share the link " + APPLICATION_LINK + "\nwith your friends and colleagues.\nThanks :-)")       
        
        sys.exit

if __name__ == "__main__":
      
      applicant_recommendation_system()
