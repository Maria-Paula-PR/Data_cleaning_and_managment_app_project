import pandas as pd
from pandas import DataFrame
import streamlit as st


#backend
class DataCleaning:
    def __init__(self,df: DataFrame):
        self.df = df
    
    def null_cleaning(self):
        for column in self.df.columns:
            if self.df[column].dtype in ["float64", "int64"]:
                self.df[column].fillna(self.df[column].mean(), inplace= True)

            if self.df[column].dtype in ["object"]:
                self.df[column].fillna(self.df[column].mode()[0], inplace=True)
        
        return self.df

    def show_user(self):
        return self.df.isnull().sum()

#frontend
st.title("Data Cleaning MP")

st.write("This is a Data Cleaning project created by Maria Paula, here you can drop a dirty csv and it will return it with no nulls. ")


file = st.file_uploader("Upload csv", type=["csv","CSV"])

if file:
    df = pd.read_csv(file)
    cleaner = DataCleaning(df)
    st.write(f"The csv has {cleaner.show_user()} nulls")
    if st.button("Clean"):
        st.write("Cleaning ...")
        cleaner.null_cleaning()
        st.write("Its clean now !")
        st.dataframe(cleaner.df)
        st.write(f"NOW the csv has {cleaner.show_user()} nulls")
        st.download_button(
            label="Download clean data",
            data = cleaner.df.to_csv(index= False),
            file_name= "Clean_csv",
            mime= "Text/csv"

        )

                
