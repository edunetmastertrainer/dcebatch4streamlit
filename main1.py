import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu

def connect_db():
    conn = sqlite3.connect("mydb.db")
    return conn
def create_Table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS student (name text,password text,roll int primary key,branch text)')
    conn.commit()
    conn.close()
def addRecord(data):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO student(name,password,roll,branch) values(?,?,?,?)',data)
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        st.error("User Already Registered")
        conn.close()

def view_record():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM student')
    result = cur.fetchall()
    conn.close()
    return result
def display():
    data = view_record()
    st.table(data)
def signup():
    st.title("Registration Page")
    name = st.text_input("Enter Your Name")
    password = st.text_input("Enter Your Password",type='password')
    repass = st.text_input("Enter Your retype Password",type='password')
    roll = st.number_input("Enter your Roll Number",format="%d")
    branch = st.selectbox("Enter your Branch",options=['CSE','AIML','IT','IOT','ECE','ME'])
    if st.button("SignIn"):
        if password != repass:
            st.error("Password Not Match")
        else:
            addRecord((name,password,roll,branch))
            st.success("Student Registered")
    
create_Table()
with st.sidebar:
        selected = option_menu('Select From Here',['SignUp','Display All Record'])

if selected == 'SignUp':
    signup()
else:
    display()