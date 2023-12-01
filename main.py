import streamlit as st
import segno
import io


def generate_qr(qr_prompt: str) -> str:
    return segno.make_qr(qr_prompt).svg_data_uri(scale = 100)

def get_qr_binary(qr_prompt: str) -> bytes:
    buff = io.BytesIO()
    segno.make(qr_prompt).save(buff, kind="png", scale=100)
    buff.seek(0)
    return buff.read()

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
        generated = generate_qr(prompt)
        st.image(generated, use_column_width=True)

        qr_binary = get_qr_binary(prompt)
        download_btn = st.download_button(
            label="Download QR",
            data=qr_binary,
            file_name="qr.png",
            mime="image/png",
        )


if __name__ == "__main__":
    main()
