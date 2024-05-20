import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import json

# Default file path for loading responses
default_file_path = r"C:\Users\mado2\Downloads\my-bot\responses.json.json"

# Function to load responses from JSON file
def load_responses(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return {}

# Function to handle sending messages
def send_message():
    user_message = entry_message.get()
    if user_message.strip() == "":
        return
    chatbox.config(state=tk.NORMAL)
    chatbox.insert(tk.END, "You: " + user_message + "\n")
    chatbox.config(state=tk.DISABLED)
    chatbox.yview(tk.END)
    entry_message.delete(0, tk.END)
    bot_response = get_bot_response(user_message)
    chatbox.config(state=tk.NORMAL)
    chatbox.insert(tk.END, "Bot: " + bot_response + "\n")
    chatbox.config(state=tk.DISABLED)
    chatbox.yview(tk.END)

# Function to get bot response based on user input
def get_bot_response(message):
    message = message.lower()
    return responses.get(message, "I'm sorry, I don't have enough information.")

# Function to handle pressing the Enter key
def on_enter_key(event):
    send_message()

# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Set the background color to purple
root.configure(background='purple')

# Create the chatbox for displaying messages
chatbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 12), bg='white', fg='black', state=tk.DISABLED)
chatbox.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the entry widget for typing messages
entry_message = tk.Entry(root, font=("Helvetica", 12), bg='white', fg='black')
entry_message.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
entry_message.bind("<Return>", on_enter_key)

# Create the send button
button_send = tk.Button(root, text="Send", command=send_message, bg='purple', fg='white', font=("Helvetica", 12, "bold"))
button_send.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Function to change button color on hover
def on_enter_button(e):
    e.widget['background'] = 'grey'

def on_leave_button(e):
    e.widget['background'] = 'purple'

# Bind hover events to the button
button_send.bind("<Enter>", on_enter_button)
button_send.bind("<Leave>", on_leave_button)

# Configure the grid to expand equally
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

# Function to select JSON file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        global responses
        responses = load_responses(file_path)
        chatbox.config(state=tk.NORMAL)
        chatbox.insert(tk.END, f"Bot: Loaded responses from {file_path}\n")
        chatbox.config(state=tk.DISABLED)
        chatbox.yview(tk.END)

# Create the load button
button_load = tk.Button(root, text="Load JSON", command=select_file, bg='purple', fg='white', font=("Helvetica", 12, "bold"))
button_load.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Bind hover events to the load button
button_load.bind("<Enter>", on_enter_button)
button_load.bind("<Leave>", on_leave_button)

# Initialize responses dictionary
responses = load_responses(default_file_path)

# Run the main loop
root.mainloop()