# Chatbot using DialoGPT and Tkinter

This project is a simple chatbot application built using Python. The chatbot uses the DialoGPT model for conversational responses and Tkinter for the graphical user interface (GUI). The application features an interactive chat window with a gradient background.

## Features
- **Conversational AI**: The chatbot responds to user inputs using the DialoGPT model.
- **GUI with Tkinter**: A simple, user-friendly graphical interface with a chat window.
- **Gradient Background**: The background of the chat window has a smooth gradient from purple to blue for a visually appealing look.
- **Real-Time Interaction**: You can chat with the bot in real-time by typing your message and pressing Enter.

## Requirements
- Python 3.6 or higher
- The following Python libraries:
  - `transformers`
  - `torch`
  - `tkinter`

## Installation

1. Clone the repository or download the `main.py` file.
2. Install the required libraries by running the following command:

    ```bash
    pip install transformers torch
    ```

3. Ensure you have the `tkinter` library installed. It's included by default with most Python distributions, but if needed, you can install it as follows:

    ```bash
    pip install tk
    ```

## Usage

1. Run the `main.py` script:

    ```bash
    python main.py
    ```

2. The chatbot GUI will appear. You can start chatting by typing a message in the input box at the bottom and pressing **Enter**. The bot will respond in the chat history window above.
3. Type "exit" to close the application.

## Example Interaction
You: Hi Bot: Hey! :D

You: How old are you? Bot: I'm good, how about you?

You: What is the purpose of life? Bot: I'm not sure

You: exit

## Customization

- **Background Color**: The gradient background can be changed by modifying the `create_rectangle` colors in the code.
- **Model**: You can change the conversational model by replacing `microsoft/DialoGPT-medium` with any other model from the Hugging Face model hub.
- **Temperature and Other Parameters**: Adjust the `temperature`, `top_p`, and `top_k` parameters in the `model.generate()` method to change the behavior of the chatbot's responses.


