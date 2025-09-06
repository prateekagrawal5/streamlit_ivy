import streamlit as st

st.title("My first streamlit app")

st.subheader("Experimenting with Streamlit")

st.write("Hello, how are you doing?")

name = st.text_input("Enter your name:")

#if name:
#    st.write(f"Hello {name}")

age = st.number_input("Enter your age:", min_value=0, max_value=100)

wt = st.slider("Enter your weight:", 1)

# Dropdown
hobby = st.selectbox("Pick a hobby:", ["Reading", "Gaming", "Coding", "Sports"])

# Button
if st.button("Submit"):
    st.sidebar.title("Results")
    st.write(f"Hello, {name}! You are {age} years old, your weight is {wt} and love {hobby}.")
