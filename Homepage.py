import streamlit as st 
from streamlit_option_menu import option_menu
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
</style>            
""", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: black;'>Welcome To The Homepage</h1>",unsafe_allow_html=True)

selected=option_menu(
    menu_title=None,
    options=["Home","Diabetic Predictor","Heart Attack Predictor","Liver Predictor","Migrane Predictor"],
    orientation="horizontal"
    )

if selected == "Diabetic Predictor":
    st.page_link("Pages\DiabeticPredictor.py")
if selected == "Heart Attack Predictor":
    st.page_link("Pages\HeartattackPredictor.py")
if selected == "Liver Predictor":
    st.page_link("Pages\LiverPredictor.py")
if selected == "Migrane Predictor":
    st.page_link("Pages\MigranePredictor.py")       
     
    
    
