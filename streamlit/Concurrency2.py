import streamlit as st

@st.cache
def get_start_time():
    from datetime import datetime
    return datetime.now()

start_time = get_start_time()
st.write(start_time)

count = 0

if st.button('Increment'):
    count += 1
    st.write('Clicked! Start Time {}; Count {}'.format(start_time, count))
