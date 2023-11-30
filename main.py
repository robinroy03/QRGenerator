import streamlit as st
import segno
import time
import datetime


def datetime_to_unix(dt: datetime.datetime):
    return int(time.mktime(dt.timetuple()))

def generate_qr(qr_prompt: str):
    unix_time = datetime_to_unix(datetime.datetime.now())
    path = f'./generated/qr_{unix_time}.png'
    segno.make_qr(qr_prompt).save(path, scale=10)
    return path


def main():
    st.sidebar.markdown("""
            A simple webapp for easy QR code generation.\n
            Idk why ppl put paywall over this.
            
            A very quick hack to give a free QR code generation portal.\n
            Repo is [here](https://github.com/robinroy03/QRGenerator)
                
            __Interesting features we can add :)__\n
            Make the generation colourful using some huggingface models like [this](https://huggingface.co/spaces/huggingface-projects/QR-code-AI-art-generator)\n
            More customization options (size, orientation ...)    
            """)

    prompt = st.text_input("Enter the text to be encoded")
    if prompt is not None and prompt != "":
        path = generate_qr(prompt)
        st.image(path, use_column_width=True)

        with open(path, "rb") as file:
            download_btn = st.download_button(
                label="Download QR",
                data=file,
                file_name="qr.png",
                mime="image/png",
            )


if __name__ == "__main__":
    main()
