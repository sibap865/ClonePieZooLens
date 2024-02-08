
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
import json
# api =st.secrets["GOOGLE_API_KEY"]
api ="AIzaSyDeUEvKEdpwwRnDXDFS12HOOpnZR1-xvyM"
genai.configure(api_key=api)

def get_gemini_repsonse(input,img):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,img])
    return response.text


def get_geminipro_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text
input_promt ="""
Concider yourself as a zookeeper; you are an authority when it comes to imparting knowledge about reptiles and other animals.
You have to make an educated estimate based on the image: Is it a real animal? if it is a real animal image advise me on the animal. find species that are comparable.
if image not contain real animal ,response most be "Image not contain any animal images".
if image not conatain real animals image, such as people, equipment  and ai generated don't provide information about image.
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
response =""
visibility =True
if uploaded_file is not None: 
    img = Image.open(uploaded_file)        
    response =get_gemini_repsonse(input_promt,img)
    if response:
        try:
            res = json.loads(response)
            st.image(img, caption=res["image description"], width=400, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
            st.subheader(res['Name'], divider='rainbow')
            st.subheader(res["detailed summary"])
        except:
            st.subheader("image may not contain any animal image")
            visibility =False
        # print(res['Name'])
try:
    if response !="" and visibility:
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
except:
    st.subheader("image not contain any animal image")

        
    




