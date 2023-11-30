import streamlit as st
import segno


def generate_qr(qr_prompt: str):
    return segno.make_qr(qr_prompt).svg_data_uri(scale = 100)

def download_qr(qr_prompt: str):
    return segno.make_qr(qr_prompt).save("qr.png", scale = 100)


def main():
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

        generate = st.form_submit_button("Generate")
        if generate and qr_prompt != "":
            st.image(generate_qr(qr_prompt))
        
        download = st.form_submit_button("Download")
        if download and qr_prompt != "":
            download_qr(qr_prompt)
            st.success("QR has been downloaded successfully!")



if __name__ == "__main__":
    main()