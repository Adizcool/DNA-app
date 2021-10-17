from altair.vegalite.v4.schema.channels import Color
import streamlit as st
import altair as alt
import pandas as pd
from PIL import Image

image = Image.open('dna-logo.png')

st.image(image, use_column_width=True)

st.write(''' # DNA Nucleotide Count Web Application
            This app counts the nucleotide composition of query DNA
         ''')
st.write(''' *** ''')   # *** creates horizontal line

# --------INPUT TEXT BOX----------

st.header('Enter DNA sequence')
sequence_input = ">DNA Query\n"

sequence = st.text_area("Sequence Input", sequence_input, height=200)
sequence = sequence.splitlines()
if(sequence[0] == '>DNA Query'):
    sequence = sequence[1:]
sequence = ''.join(sequence)

temp = ''
nucl = ['A', 'T', 'G', 'C']
for i in range(len(sequence)):
    if sequence[i] in nucl:
        temp = temp + sequence[i]
sequence = temp  # removing non nucleotide characters

st.write(''' *** ''')

st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count)')

# ----------1st Method-------------
st.subheader('1. Print Dictionary')


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d


a = DNA_nucleotide_count(sequence)
a

st.write(''' *** ''')

# -----------2nd Method------------
st.subheader('2. Print Text')
st.write('There are ' + str(a['A']) + ' Adenine (A)')
st.write('There are ' + str(a['T']) + ' Thymine (T)')
st.write('There are ' + str(a['G']) + ' Guanine (G)')
st.write('There are ' + str(a['T']) + ' Cytosine (C)')

st.write(''' *** ''')

# -----------3rd Method------------
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(a, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})

st.write(df)

st.write(''' *** ''')

# -----------4th Method-------------
st.subheader('4. Display Bar Chart')
b = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y=alt.Y('count', scale=alt.Scale(domain=[1, max(a.values()) + 1])),
    color=alt.value('#7D3C98')
)

b = b.properties(
    width=alt.Step(80),   # controls width of bar
    height=500
)

st.write(b)

st.write(''' *** ''')

st.button(label='Rerun')
