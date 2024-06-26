from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained("Unbabel/gec-t5_small")
tokenizer = T5Tokenizer.from_pretrained('t5-small')

def correct(sentence):
    tokenized_sentence = tokenizer('gec: ' + sentence, max_length=128, truncation=True, padding='max_length', return_tensors='pt')
    corrected_sentence = tokenizer.decode(
        model.generate(
            input_ids = tokenized_sentence.input_ids,
            attention_mask = tokenized_sentence.attention_mask,
            max_length=128,
            num_beams=5,
            early_stopping=True,
        )[0],
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True
    )
    return corrected_sentence

import streamlit as st


st.title('Grammar Correction Tool')
user_input = st.text_area('Enter your text:')
if st.button('Correct Grammar'):
    corrected_text = correct(user_input)
    st.write('Corrected Text:')
    st.write(corrected_text)
