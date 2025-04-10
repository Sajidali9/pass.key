import streamlit as st 
import re

st.set_page_config(page_title="Password Strenght Checker", page_icon="🔒")

st.title("🔐Passwordstrenght Checker")
st.markdown(""""
"## welcome to the ultimate password strenght checker!👋
use this simple tool to check the strenght of your password and get suggestionss o how to make it stronger.
            we will give you helpful tips to create a *Strong Password*🔒""")  

password = st.text_input("Enter your password", type="password")
                         
feedback = [] 

score = 0 

if password:
    if len(password) >=8:
        score += 1
    else:
        feedback.append("❌Password should be at least 8 characters long.")

    if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lower case characters.")


    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one digit.")

    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special characters(!@#$%&*).")

    if score == 4:
        feedback.append("✅your password is strong!🎉")
    elif score == 3:
        feedback.append("🟡your password is medium strenght.It could be stronger.")  
    else:
        feedback.append("🔴your password is weak. please make it stronger.") 

    if feedback:
        st.markdown("## Improvement Suggestion")
        for tip in feedback:
            st.write(tip)
else:               
    st.info("please enter your password to get started.")