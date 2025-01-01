streamlit

st.title #titulo de la pagina 

st.header # titulo dentro

st.input (text, number etc)

st.sidebar (barra lateral para manejar)


"""
if st.checkbox("te gusta el azucar"):
    st.checkbox("no")
    st.checkbox("si")

"""



File upload

file = st.uploader("Upload csv", type=["csv","CSV"])

