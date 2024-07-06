import streamlit as st 
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1628348070889-cb656235b4eb?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);  
}
[data-testid="stToolbar"] {
right: 2rem;
}
.st-emotion-cache-czk5ss.e16jpq800{
    visibility: hidden;
}
.st-emotion-cache-mnu3yk.ef3psqc5{
    visibility: hidden;
}
.st-emotion-cache-15ecox0.ezrtsby0{
    visibility: hidden;
}
.st-emotion-cache-fm8pe0.e1nzilvr4{
    color : black;
}
*{
    color : white;
}
</style>            
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>Welcome To The Homepage</h1>",unsafe_allow_html=True)
st.markdown("---")
st.link_button("Diabetic Predictor", "https://diabeticpredictor.streamlit.app/")
st.link_button("Heart Attack Predictior", "https://heartattackpredictor1.streamlit.app/")
st.link_button("Liver Predictior", "https://liverpredictor.streamlit.app/")
st.link_button("Migrane Predictor", "https://migranepredictor.streamlit.app/")
    
