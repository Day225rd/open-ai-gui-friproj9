This application provides a simple graphical interface for interacting with OpenAI's GPT-based language model. Users can input queries, 
and the app fetches responses from OpenAI's API in real time. The program uses tkinter for its GUI and integrates the OpenAI API via the openai Python package.

Features
Interactive User Interface: A clean and intuitive interface built with tkinter.
Scrollable Input and Output Areas: Easily input queries and view responses in scrollable text fields.
Seamless OpenAI Integration: Communicates with OpenAI's GPT API to provide intelligent responses to user queries.

Requirements
Python 3.6 or higher
The openai Python library
The python-dotenv library
A valid OpenAI API key

Installation
Install Python 3.6 or later if not already installed on your system.
Install the required Python packages using pip.
Place the .env file in the same directory as the application with the required OpenAI API key.

Usage
Run the application to launch the GUI.
Enter a query in the input field labeled "Query."
Click the "Submit Question" button to send the query to the OpenAI API.
View the response in the "Response" section of the application.
