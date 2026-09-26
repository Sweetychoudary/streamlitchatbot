import streamlit as st
st.header(" WELCOME TO AI CHATBOT")
st.subheader("i am here to help you")
st.caption("hii... ")
text = st.text_input("ask any thing")
if st.button("send"):
    if text:
        st.success("successfully entered")
        st.write("you entered:", text)
    else:
        st.error("error please enter something here")

