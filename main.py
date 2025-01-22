import streamlit as st

col1,col2= st.columns(2)


with col1:

    col1= st.image("images/photo.jpeg")

with col2:

    # st.title(" Shivi Sharma ")

    st.markdown("<h1 style='color:DarkBlue;'>Shivi Sharma</h1>", unsafe_allow_html=True)
    content = ''' 
    Results-oriented Software Engineer with strong SQL, Java, Python, and data warehousing skills. Experience in Supply Chain Management (OMP) and Finance (AITRA). Developed and maintained applications for logistics optimization and AR/AP reconciliation. Focus on delivering robust and scalable solutions."
     '''
    col2 = st.info(content)

st.markdown("---")
content2 = '''
                Below mentioned are some Apps I have built in Python. Feel Free to contact me!!!
                '''
st.write(content2)