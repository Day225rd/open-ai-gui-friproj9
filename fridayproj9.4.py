import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import openai

from dotenv import load_dotenv
import os
load_dotenv()
# Set the API key
openai.api_key = os.getenv("key")



# Create the main application
class AIapp:
    def __init__(self, master):
        master.geometry('500x400')
        master.title("Chat with GPT")

        # Welcome Label
        self.label1 = ttk.Label(master, text="Welcome")
        self.label1.place(x=20, y=10)

        # Instruction Label
        self.label2 = ttk.Label(master, text="Please enter a query into the field below")
        self.label2.place(x=20, y=40)

        # Query Label
        self.label3 = ttk.Label(master, text="Query:")
        self.label3.place(x=20, y=80)

        # Input Text Field
        self.txtfield1 = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.txtfield1.place(x=20, y=110, width=460, height=100)

        # Submit Button
        self.btn1 = ttk.Button(master, text="Submit Question", command=self.AIsubmit)
        self.btn1.place(x=20, y=220)

        # Output Area
        self.output_label = ttk.Label(master, text="Response:")
        self.output_label.place(x=20, y=260)
        self.output_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, state='disabled')
        self.output_area.place(x=20, y=290, width=460, height=80)

    def AIsubmit(self):
        # Get the user's query
        query = self.txtfield1.get("1.0", "end-1c").strip()
        if not query:
            self.update_output("Please enter a valid query.")
            return

        # Fetch response from OpenAI
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query},
                ]
            )
            response = completion.choices[0].message['content']
        except Exception as e:
            response = f"Error: {str(e)}"

        # Update the output area with the response
        self.update_output(response)

    def update_output(self, text):
        # Enable the output area to update content
        self.output_area.config(state='normal')
        self.output_area.delete("1.0", "end")  # Clear previous output
        self.output_area.insert("1.0", text)
        self.output_area.config(state='disabled')  # Disable editing of the output area


# Main Program Execution
root = tk.Tk()
app = AIapp(root)
root.mainloop()