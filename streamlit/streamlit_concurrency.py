import streamlit as st

from datetime import datetime
start_time = datetime.now()
st.write(start_time)

count = 0

if st.button('Increment'):
    count += 1
    st.write('Clicked! Start Time {}; Count {}'.format(start_time, count))
