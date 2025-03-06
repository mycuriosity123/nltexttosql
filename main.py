import streamlit as st
import requests
import json


st.title('Fetching info from database table from natural language text input')

st.divider()

text = st.text_input("Enter the natural language text to be converted to sql query:","")
st.button("Generate query")

print(text)
if text:
    try:
        resp = requests.post(url="http://127.0.0.1:5001/generate_query",json={"question":text})

        print("*************",resp)
        resp.raise_for_status()
        res=json.loads(resp.text)

        st.write(res["query"])  

        sql_query = st.text_input("Enter the sql query to fetch information from table:")
        st.button("run query")

        if sql_query:
            response = requests.post(url="http://127.0.0.1:5001/execute_sql_query",json={"query":sql_query})
            res = json.loads(response.text)
            # print("********",res)
            st.write("The output after running the query on database table is:",res["result"])

    except requests.exceptions.RequestException as e:
        print(e)
    except json.decoder.JSONDecodeError as e:
        print(f"JSON decode error:{e}")
    except Exception as e:
        print(f"*********{e}")






