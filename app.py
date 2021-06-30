import streamlit as st
import pickle
import pandas as pd

# db management
import sqlite3
conn = sqlite3.connect("data.db")
c = conn.cursor()



def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT, password TEXT)')

def add_userdata(username, password):
    c.execute('INSERT INTO usertable(username, password) VALUES (?,?)', (username, password))
    conn.commit()

def login_user(username, password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password =?', (username, password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    return data



def main():
    # simple login app

    st.title("Simple Login App")

    menu = ("Home", "Login", "SignUp")
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type= "password")
        if st.sidebar.checkbox("Login"):

            create_usertable()
            result = login_user(username, password)
            if result:

                st.success("Logged in as {}".format(username))

                # This is our dashboard
                task = st.selectbox("Task", ["Add Post", "Analytics", "Profile"])
                
                if task == "Add Post":
                    st.subheader("Add Your Post")
                elif task == "Analytics":
                    st.subheader("Analytics")
                elif task == "Profile":
                    st.subheader("User Profile")
                    
                    st.write("Username :  " + username )
                    st.write("Password : " + password)

            else:
                st.error("Invalid Username/Password")




    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_username = st.sidebar.text_input("User Name")
        new_password = st.sidebar.text_input("Password", type= "password")

        if st.sidebar.button("SignUp"):
            create_usertable()
            add_userdata(new_username, new_password)
            st.success("You have successfully created an account")
            st.info("Go To Login Menu to Login")









if __name__ == "__main__":
    main()