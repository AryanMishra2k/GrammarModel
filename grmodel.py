from gramformer import Gramformer
import torch

gf = Gramformer(models = 1, use_gpu=False)


def correct(sentence):
    res = gf.correct(sentence) # Gramformer correct
    return res[0] # Return first value in res array


import gradio as gr


interface = gr.Interface(fn=correct, 
                        inputs=gr.Textbox(lines=2, placeholder="Enter sentence here..."),
                         outputs='text', 
                        title='Sup, I\'m Gramformer')
interface.launch()
