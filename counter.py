import streamlit as st

st.header("Online AI Counter")

button_style = """
    <style>
    .big-btn {
        font-size: 50px;
        height: 80px;
        width: 80px;
        border-radius: 15px;
        text-align: center;
        margin: 0 auto;
        cursor: pointer;
        user-select: none;
        font-weight: bold;
        color: white;
        border: none;
    }
    .btn-green {
        background-color: #28a745;
    }
    .btn-red {
        background-color: #dc3545;
    }
    .count-display {
        font-size: 160px;
        text-align: center;
        padding-top: 20px;
        user-select: none;
    }
    </style>
"""


increment_col , ctr_display , decrement_col = st.columns(3)
st.markdown(button_style, unsafe_allow_html=True)

with increment_col:
    if st.button("INCREMENT"):
        st.session_state.counter += 1
        # st.write(st.session_state.counter)

with ctr_display:
    if "counter" not in st.session_state:
        st.session_state.counter = 0
        # st.write(st.session_state.counter)
    st.markdown(f"<div class='count-display'>{st.session_state.counter}</div>", unsafe_allow_html=True)


with decrement_col:
    if st.button("DECREMENT"):
        st.session_state.counter -= 1


