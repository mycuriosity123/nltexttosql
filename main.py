import streamlit as st
import requests
import json


st.title('Fetching info from database table from natural language text input')

st.divider()

text = st.text_input("Enter the natural language text to be converted to sql query:","")
st.button("Generate query")

if text:
    resp = requests.post(url="http://localhost:5001/generate_query",json={"question":text})

    res=json.loads(resp.text)

    st.write(res["query"])

    sql_query = st.text_input("Enter the sql query to fetch information from table:")
    st.button("run query")

    if sql_query:
        response = requests.post(url="http://localhost:5001/execute_sql_query",json={"query":sql_query})
        res = json.loads(response.text)
        # print("********",res)
        st.write("The output after running the query on database table is:",res["result"])

    # st.write(res["query"])








