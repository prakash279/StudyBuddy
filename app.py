import streamlit as st
import speech_recognition as sr
import pyttsx3
import time
from transformers import pipeline

engine = pyttsx3.init()

def speak_text(response_text):
    engine = pyttsx3.init()
    engine.endLoop()  
    engine.say(response_text)
    try:
        engine.runAndWait()
    except RuntimeError:
        pass  
    finally:
        engine.stop()  


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Request error. Please check your internet connection."
        except Exception as e:
            return f"An error occurred: {e}"

def generate_response(question_text):
    pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM-135M", device=-1)
    generated_text = pipe(question_text, max_length=50, num_return_sequences=1, truncation=True, do_sample=False, pad_token_id=0)
    return generated_text[0]['generated_text']

def custom_css():
    st.markdown(""" 
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #222831; /* Dark Background */
                color: #EEEEEE; /* Light Gray Text */
            }
            .stApp {
                background-color: #393E4F; /* Darker Gray */
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1); /* Soft shadow */
            }
            /* Headings styles */
            h1 {
                color: #00ADB5; /* Teal Color */
                font-size: 2.5rem;
            }
            h2 {
                color: #00ADB5; /* Teal Color */
                font-size: 2rem;
            }
            h3 {
                color: #00ADB5; /* Teal Color */
                font-size: 1.5rem;
            }
            /* Flashcard Styles */
            .flashcard {
                background-color: #00ADB5;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 20px;
                margin: 10px;
                transition: all 0.3s ease;
                cursor: pointer;
            }
            .flashcard:hover {
                background-color: #EEEEEE; /* Light gray on hover */
                transform: scale(1.05); /* 5% size increase on hover */
            }
            .flashcard h3 {
                color: #222831; /* Dark Background for flashcard headings */
            }
            .flashcard p {
                font-size: 1.1rem;
                color: #555; /* Darker gray text inside cards */
            }
            /* Input Fields & Buttons */
            .stButton button {
                background-color: #00ADB5; /* Teal Button */
                color: white;
                font-size: 1rem;
                padding: 10px 20px;
                border-radius: 5px;
                transition: all 0.3s;
            }
            .stButton button:hover {
                background-color: #393E4F; /* Darker Gray on hover */
            }
            /* Input and text area style */
            .stTextInput input {
                background-color: #222831; /* Dark Background for input */
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                color: #EEEEEE; /* Light Text in input */
            }
            /* Radio button color */
            .stRadio button {
                color: #00ADB5; /* Teal Color for radio buttons */
            }
            /* For headings */
            h1, h2, h3, h4 {
                color: #EEEEEE;  /* Light Gray Text */
                font-weight: bold;
            }

            /* Flashcards - Title Text */
            .stInfo {
                color: #222831;  /* Dark Text */
            }

            /* Button Styling */
            button {
                background-color: #00ADB5;  /* Teal button with white text */
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

custom_css()
st.title("🌟Study buddy")
st.subheader("Your study Companion Bot")
st.subheader("Ask questions, learn concepts, and get help in real-time!")

st.markdown("### 💡 **Explore Topics:**")
cols = st.columns(3)
topics = [
    ("📊 Machine Learning", "Get insights into supervised and unsupervised learning."),
    ("🤖 Artificial Intelligence", "Learn about AI concepts, tools, and techniques."),
    ("🧠 Deep Learning", "Explore neural networks, CNNs, RNNs, and more.")
    
]


for idx, topic in enumerate(topics):
    with cols[idx]:
        st.markdown(f"""
            <div class="flashcard">
                <h3>{topic[0]}</h3>
                <p>{topic[1]}</p>
            </div>
        """, unsafe_allow_html=True)

if "listening" not in st.session_state:
    st.session_state.listening = False
if "response" not in st.session_state:
    st.session_state.response = ""

st.markdown("### 🎤 **Ask Your Question**")
input_method = st.radio(
    "Choose Input Method:",
    options=["🎙️ Use Microphone", "📂 Upload Audio File", "💬 Enter Text"],
    horizontal=True
)

if input_method == "🎙️ Use Microphone":
    if st.button("🎙️ Start Listening"):
        st.write("🎙️ Listening... Speak now.")
        question = recognize_speech()
        if question.strip():
            st.write(f"**You said:** {question}")
            response = generate_response(question)
            st.success(f"🤖 **Bot's Response:** {response}")
            speak_text(response)
elif input_method == "📂 Upload Audio File":
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
    if uploaded_file:
        st.write("Processing uploaded audio...")
        question = "Audio file processing is not implemented yet."
        response = f"Placeholder response to '{question}'"
        st.success(f"🤖 **Bot's Response:** {response}")
        speak_text(response)
elif input_method == "💬 Enter Text":
    user_input = st.text_input("Type your question here:")
    if user_input:
        response = generate_response(user_input)
        st.success(f"🤖 **Bot's Response:** {response}")
        speak_text(response)

st.markdown("""
    ---
    🤝 Made by Prakashchand Choudhary  
    ✉️ Contact: [choudhary.prakash27903@gmail.com](mailto:choudhary.prakash27903@gmail.com)  
    🖥️ Hosted on Streamlit 
""")
