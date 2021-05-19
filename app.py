import streamlit as st

from langcalc import ari

st.set_page_config(page_title='Readability Calculator')

st.title('Automated Readability Index Calculator')

description = '''
This app assesses the readability of an excerpt of text using the Automated Readability Index.
'''

st.markdown(description)

demo_string = '''
As we wound on our endless way, and the sun sank lower and lower behind us,
the shadows of the evening began to creep round us. This was emphasized by
the fact that the snowy mountain-top still held the sunset, and seemed to
glow out with a delicate cool pink. Here and there we passed Cszeks and slovaks,
all in picturesque attire, but I noticed that goitre was painfully prevalent.
By the roadside were many crosses, and as we swept by, my companions all
crossed themselves. Here and there was a peasant man or woman kneeling before
a shrine, who did not even turn round as we approached, but seemed in the
self-surrender of devotion to have neither eyes nor ears for the outer world.
There were many things new to me. For instance, hay-ricks in the trees, and
here and there very beautiful masses of weeping birch, their white stems
shining like silver through the delicate green of the leaves.
'''


s = st.text_area('Input your text here:', value=demo_string, height=300)

results = ari(s)

st.markdown(f'This text recieved a score of {results[0]}, which is suitable for readers aged around {results[1]} years old.')