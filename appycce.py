import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
# st.write(":Streamlit: Hello Tanushree")
# st.write("Hello Tanushree")
st.write(":100: Hello Tanushree")
st.text("Lets Start")

name=st.text_input("Enter Name: ")
if st.button("Greet"):
    st.success(f"Hello, {name}")

#creating charts using pandas and numpy
df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

#Sidebar, image and video
st.sidebar.title("Navigation")
st.subheader("Display Image")
st.image("sample_image.webp", caption="Sample Image")
st.video("https://youtu.be/ryUxrFUk6MY?si=bYR5J3TpjAvEHivy")

#upload csv file
upload_csv=st.file_uploader("upload a CSV File", type="csv")

if upload_csv:
    df = pd.read_csv(upload_csv)
    st.dataframe(df)

#text and markdown formatting
st.header("This is a Header")
st.subheader("This ia a Subheader")

st.markdown("***Bold**,*Italic*,'code' [Link](http://streamlit.io)")
st.code("for i in range(s): print(i)", language="python")

#input component is streamlit
st.text_input("What's your name?")
st.text_area("write something...")
st.number_input("pick a number",min_value=0,max_value=100)
st.slider("Choose a range",0,100)
st.selectbox("select a fruit",["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings ", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one",["Option=A", "Option= B"])
st.checkbox("I aggree to this item.")

#matplotlib integration
import matplotlib.pyplot as plt
fig, ax=plt.subplots()
ax.plot([1,2,3],[1,4,9])
st.pyplot(fig)