from typing import List
import streamlit as st

st.title("Chatbot with streamlit")
st.subheader("メッセージを入力してから送信をタップしてください")
name: str = st.text_input(label="おなまえ")
message: str = st.text_input("メッセージ")
comments: List[str] = []


def append():
    global comments
    if (len(comments) > 0):
        comments.append("\r\n")
    comments.append(f"{name}:{message}")
    st.write(comments)


if st.button('コメント'):
    append()
