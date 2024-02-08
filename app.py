from dotenv import load_dotenv

load_dotenv()

import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
import json

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input,img):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,img])
    return response.text


def get_geminipro_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text
input_promt ="""
Think of yourself as a zookeeper; you are an authority when it comes to imparting knowledge about reptiles and other animals.
You have to make an educated estimate based on the image: Is it an animal? Please advise me on the animal. find species that are comparable.
You must state, "I am not able to recognize it," if you are unable to identify any animal or estimate what it is.
It is not necessary to include information about anything other than animals, such as people, equipment, etc.
If you come across more than one animal, you must provide information about each one using below format.
It is up to you to speculate as to the animal's specifics. which species it is; you have to make a guess in addition to noting its generic term, such as snake.

I want the response in below should be in double string having the structure if image contain animal
{ image description:"",
Name:"",
related Species:"",
speciality of animal:"",
detailed summary:""}
"""


#streamlit app

st.set_page_config(page_title="ClonePieZooLens")
st.header("ClonePieZooLens🐯🐘🦜🐍🐜")
st.text("This app provides guide about animals (you might have seen in Pokémon)")
uploaded_file = st.file_uploader("Upload animal image...",type=["png","jpg"])


# output = pipe(text)
# st.audio(output["audio"], sample_rate=output["sampling_rate"])
res ={"Name":""}

if uploaded_file is not None: 
    img = Image.open(uploaded_file)        
    response =get_gemini_repsonse(input_promt,img)
    if response:
        st.subheader(response)
        res = json.loads(response)
        # print(res['Name'])
od=st.text_area("Other details you want to know: ",key="input")
submit = st.button("search🙃")
input_promt1 =f"""
Think of yourself as a zookeeper; you are an authority when it comes to imparting knowledge about animals.
You have to make a sort estimate based on animal name name and task
name : {res['Name']}
task : {od}
"""
if od is not None and submit:
    res = get_geminipro_repsonse(input_promt1)
    st.subheader(res)


        
    




