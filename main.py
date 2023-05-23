from langchain import * 
import streamlit as st
import pandas as pd
from lgchain import chain
from streamlit import components
from streamlit_chat import message




st.title("SnowBot ❄️")
st.caption("**********")


with open(r"C:\Users\rohanthareja\OneDrive - Microsoft\Desktop\Py\snowflke\styles.md") as styles_file:
    styles_content = styles_file.read()

st.write(styles_content, unsafe_allow_html=True)


if 'history' not in st.session_state:
        st.session_state['history'] = []

if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello ! I'm your Snowbot ,Talk your way through data " " 🤗"]

if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey ! 👋"]
        
#container for the chat history
response_container = st.container()
#container for the user's text input
container = st.container()


with container:
        with st.form(key='my_form', clear_on_submit=True):
            
            user_input = st.text_input("Query:", placeholder="Type your query here...", key='input',value="",label_visibility="hidden")
            submit_button = st.form_submit_button(label='Submit')
            
        if submit_button and user_input:
            output = (chain(user_input))
        
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)
      
            
if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")



