# Streamlit GPT Application

## Overview

This project is a Streamlit application that integrates a GPT model using LangChain, with a backend powered by FastAPI. The application provides a user-friendly interface to interact with the language model, allowing users to leverage advanced natural language processing capabilities through a web-based platform.

## Features

- **User Interface**: Built with Streamlit for an intuitive and interactive web interface.
- **Language Model**: Utilizes GPT models through LangChain for advanced conversational AI and text generation.
- **Backend**: FastAPI serves as the backend, handling API requests and integrating with the GPT model.
- **Responsive Design**: Designed to provide a seamless user experience across different devices.

## Technologies Used

- **Streamlit**: For building the front-end interface.
- **LangChain**: For facilitating interactions with the GPT model.
- **GPT Model**: For natural language processing and text generation.
- **FastAPI**: For creating a performant and modern API backend.
- **Python**: The primary programming language used in this project.

## Installation

To set up and run this application locally, follow these steps:

1. **Clone the Repository**
    ```
    git clone https://github.com/Abdul-Ikram/Streamlit-Chat-bot.git
    cd Streamlit-Chat-bot
    ```

2. **Create and Activate a Virtual Environment**
    ```
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**
Create a .env file in the root directory of the project. This file should include your OpenAI API key:
    ```
    OPENAI_API_KEY="your_openai_api_key_here"
    ```

5. **Run the FastAPI Backend**
    ```
    fastapi dev app.py
    ```

6. **Run the Streamlit Application**
    ```
    streamlit run gui.py
    ```
