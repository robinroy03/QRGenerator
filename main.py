import streamlit as st
import segno

def qr_generator(qr_prompt: str):
    return segno.make_qr(qr_prompt).svg_data_uri(scale = 100)

with st.sidebar:
    st.markdown("""
             A simple webapp for easy QR code generation.\n
             Idk why ppl put paywall over this.
             
             A very quick hack to give a free QR code generation portal.\n
             Repo is [here](https://github.com/robinroy03/QRGenerator)
                
            __Interesting features we can add :)__\n
            Make the generation colourful using some huggingface models like [this](https://huggingface.co/spaces/huggingface-projects/QR-code-AI-art-generator)\n
            More customization options (size, orientation ...)    
            """)

with st.form(key = "form"):
    qr_prompt = st.text_area(label = "Enter the QR value to be entered")
    submitted = st.form_submit_button("Submit")

    if submitted and qr_prompt != "":
        st.image(qr_generator(qr_prompt))