import streamlit as st

st.title("Make A Form")
selected_page = st.sidebar.selectbox("Select a page", ["Fill Form", "Submitted Form"])

if selected_page=="Fill Form":
    form=st.form(key='my_form')
    with form:
        i=st.camera_input("Take a picture")
        fname=st.text_input("Enter Your First Name: ")
        lname=st.text_input("Enter Your Last Name: ")
        date=st.date_input("Choose Your Birthdate")
        sex=st.radio("Choose Your Gender:",["Male","Female","Rather Not Say","Custom"])
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Submitted")
            selected_page="Submitted Form"
            st.image(i)
            st.write(fname,lname)
            st.write("Age: ",2023-date.year)
            st.write(sex)


else:
    st.write("Please fill the form!")

