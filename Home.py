import streamlit as st
from senhas import check_password
st.set_page_config(
    page_title="Ferramentas do Allan",
    page_icon="🛠️",
)

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

st.markdown('# Boas-vindas às ferramentas do Allan')

st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3pxZm5oeWU2dGswcDQyNWcwMnd3M3NmeHZyY2JvbndjZWx3NjYxbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/m94Z9sz9TtM1mCcnw2/giphy.gif")