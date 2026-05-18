import streamlit as st
import random

st.title("🎈 Hi There")
st.write(
    "My name is"
)
st.title("Marcell Jeremy W")
st.write(
    "I'm a data scientist, my NIM is 0706012110013."
)

st.title("Random Dog Facts")

fun_facts = [
    "Dogs have three eyelids.",
    "A dog's nose print is unique, like a human fingerprint.",
    "Dogs can hear four times farther than humans.",
    "The Basenji is the only barkless dog.",
    "Dogs have about 1,700 taste buds.",
    "A dog's sense of smell is about 100,000 times stronger than ours.",
    "Dogs can learn over 1,000 words.",
    "The Saluki is the oldest known breed of domesticated dog."
]

st.write(random.choice(fun_facts))