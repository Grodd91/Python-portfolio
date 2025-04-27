import tkinter as tk
from tkinter import scrolledtext
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

chat_history_ids = None

def chat_with_bot(event=None):
    global chat_history_ids
    user_input = entry.get()

    if user_input.lower() == 'exit':
        window.quit()
        return
    
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
    else:
        bot_input_ids = new_user_input_ids

    chat_history_ids = model.generate(
        bot_input_ids, 
        max_length=1000, 
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.9,
        top_p=0.95,
        top_k=60
    )

    bot_output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_input + '\n')
    chat_history.insert(tk.END, "Bot: " + bot_output + '\n\n')
    chat_history.config(state=tk.DISABLED)

    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Chatbot")

gradient_bg = tk.Canvas(window, width=400, height=500)
gradient_bg.pack(fill="both", expand=True)
gradient_bg.create_rectangle(0, 0, 400, 500, fill="#8e2de2", outline="#8e2de2")
gradient_bg.create_rectangle(0, 0, 400, 500, fill="#4a00e0", outline="#4a00e0", stipple="gray12")

chat_history = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=15, state=tk.DISABLED, bg='#f0f0f0', fg='#333', font=('Arial', 12))
chat_history.place(x=10, y=10)

entry = tk.Entry(window, width=40, font=('Arial', 14))
entry.place(x=10, y=380)

send_button = tk.Button(window, text="Send", width=20, command=chat_with_bot, bg='#4a00e0', fg='white', font=('Arial', 12))
send_button.place(x=250, y=375)

window.bind('<Return>', chat_with_bot)

window.geometry("400x500")
window.mainloop()
