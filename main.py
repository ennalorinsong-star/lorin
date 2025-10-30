import streamlit as st
st.title('나의 첫 웹 서비스 만들기!')
st.write('ㅎㅇ')
name=st.text_input('이름.')
if st.button('인사말 생선'):
 st.write(name+'안녕하시긔')
 st.balloons()
