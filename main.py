import streamlit as st
import pandas

col1,col2= st.columns(2)

# with is used to access the data of the columns
with col1:

    col1= st.image("images/photo.jpeg")

with col2:

    # st.title(" Shivi Sharma ")
    # This will change color of title using html in python code...
    st.markdown("<h1 style='color:DarkBlue;'>Shivi Sharma</h1>", unsafe_allow_html=True)
    content = ''' 
    Results-oriented Software Engineer with strong SQL, Java, Python, and data warehousing skills. Experience in Supply Chain Management (OMP) and Finance (AITRA). Developed and maintained applications for logistics optimization and AR/AP reconciliation. Focus on delivering robust and scalable solutions."
     '''
    col2 = st.info(content)

# This will add new horizontal line below image and description
st.markdown("---")

content2 = '''
                Below mentioned are some Apps I have built in Python. Feel Free to contact me!!!
                '''
st.write(content2)

# Why we are using pandas.. bcoz pandas will give help you in reading csv along with it will give you data in tabluar format
# you can use with open() to read csv file but that will return content in one single string then you need to use string methods to part ways the data in desired format it will be length process

col3,col4 = st.columns(2)
df = pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
