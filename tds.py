import streamlit as st


st.title("Largest in three numbers")

x = st.number_input("Enter first number:", step = 0.0001, value = 0.0000, format = "%5.4f")
y = st.number_input("Enter second number:", step = 0.0001, value = 0.0000, format = "%5.4f")
z = st.number_input("Enter third number:", step = 0.0001, value = 0.0000, format = "%5.4f")


greatest = max(x,y,z)
greatest = round(greatest, 4)



st.write("The largest among these three numbers:", greatest)

if st.button("Click me!"):
    st.balloons()

         
