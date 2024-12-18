# 🌟 **StudyBuddy- Student Companion Bot** 

This project is designed to help students interact with a bot in multiple ways, whether through speech or text. The bot uses natural language processing (NLP) and text-to-speech (TTS) technologies to generate and deliver responses. The system allows flexibility in input methods, accommodating different preferences for a seamless user experience.

## 🎤 **User Interaction Workflow**
### Flow Overview
![image](https://github.com/user-attachments/assets/806b6940-d4ec-46ca-90db-c9802e9252de)

The workflow begins when the user interacts with the system and chooses their preferred method of input. The system processes the input, generates a response, and delivers it back to the user in text or speech format.

### **Start: User Interaction**
- The user initiates an interaction with the system.

### **Step 1: Choose Input Method**
- The user is presented with three input options:
    - 🎙️ **Use Microphone**: Users provide input via speech.
    - 📂 **Upload Audio File**: Users upload a pre-recorded audio file for the bot to process.
    - 💬 **Enter Text**: Users directly type their question into the system.

### **Step 2: Processing the Input**
- Depending on the user's choice of input method, the system will process the input accordingly:
    - **Recognize Speech**: If the microphone is used, the system converts the speech into text.
    - **Process Uploaded Audio**: If an audio file is uploaded, the system processes and extracts text from the file.
    - **User Types Question**: If the user types their question, it proceeds directly to the next step.

### **Step 3: Speech Recognition**
- For **microphone** or **uploaded audio** inputs, speech recognition is performed to generate text.

### **Step 4: Generate Response**
- Once the system has the text input (from any method), it generates a response using natural language processing models, I have used HuggingFaceTB/SmolLM-135M for this purpose for faster response.

### **Step 5: Response Delivery**
- The system delivers the response in two formats:
    - **Display Response**: The text-based response is displayed to the user.
    - **Speak Response**: The response is converted into speech using a Text-to-Speech engine and played back to the user.
