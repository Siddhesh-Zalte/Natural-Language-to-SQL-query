from dotenv import load_dotenv
load_dotenv()#load all thge env variables
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

#configure api key
genai.configure(api_key=os.getenv("api_key"))

#create function to load google gemini model and provide query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response=model.generate_content([prompt[0],question ])
    return response.text

##create another function to retrieve query from SQL database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cur.execute(sql)
    rows=cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#define the prompt
prompt=[
    """
    You are an expert in converting English questions into SQl Query!
    The SQL database has the name STudent and has the following columnns- NAME, CLASS, SECTION, MARKS.
    \n\nFor example 1- How many entries of record are present
    \n\nExample 2 - tell me all the students studying in Data science class?
    the SQl command will be something like this SELECT * FROM STUDENT WHERE CLASS='Data science';
    also the sql code shoid not have ``` in beginning and end of the code and sql word in the output.

"""
]  

st.set_page_config(page_title="SQL QUERY")
st.header("Gemini LLM SQL data Application")
question=st.text_input('Input: ', key="input")
submit=st.button("Ask the question")

#if submit is clicked
if submit:
    response=get_gemini_response(question, prompt)
    print(response)
    data=read_sql_query(response, "Student.db")
    st.subheader("The response is ")
    for row in data:
        print(row)
        st.header(row)
