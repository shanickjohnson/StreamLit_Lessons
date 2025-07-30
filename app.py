import streamlit as st
import time

st.set_page_config(layout="wide")

# --- Funky Background Color ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] > .main {
    background-color: #E0F7FA; /* A nice light blue */
}
</style>
""", unsafe_allow_html=True)


st.title("💻✨ Build Your First Chatbot! 🤖")
st.caption("Click through the tabs below to learn how!")

# --- Create Tabs for the Slideshow with Emojis ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "👋 Intro", 
    "🐍 The 'Boring' Script", 
    "Step 1: Making it Pretty ✨", 
    "Step 2: Giving it a Brain 🧠", 
    "Step 3: Let's Chat! 💬",
    "🎉 You Did It!"
])

# --- Slide 1: Introduction ---
with tab1:
    st.header("Welcome!")
    st.markdown("""
    This guide will show you how to take a simple Python script and turn it into an interactive chatbot application using Streamlit. It's way easier than you think!

    We'll start with a basic command-line script and then, step-by-step, add Streamlit's magic to bring it to life in a web browser.
    """)
    st.subheader("Our Goal:")
    st.info("To build a simple, conversational AI chatbot that remembers our chat.")
    st.image("https://storage.googleapis.com/agentbuilder-workbench-prod-artifacts/bot-logo.png", width=200)
    st.snow()


# --- Slide 2: The Starting Point ---
with tab2:
    st.header("The Starting Point: A Plain Python Script")
    st.markdown("""
    Here is a basic Python script that simulates a chatbot conversation in your terminal. It's not interactive; it just prints a pre-defined conversation. To change anything, you have to edit the code directly.
    
    This script works, but it's not very user-friendly. Let's fix that!
    """)
    
    st.code('''
# --- basic_chatbot_script.py ---

def get_bot_response(user_input):
    """A simple function to simulate a bot's response."""
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! Thanks for asking."
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return f"I'm not sure how to respond to that. You said: '{user_input}'"

# --- Main part of the script ---
# A pre-defined, non-interactive conversation
conversation = [
    {"role": "user", "content": "Hello bot!"},
    {"role": "assistant", "content": get_bot_response("Hello bot!")},
    {"role": "user", "content": "How are you?"},
    {"role": "assistant", "content": get_bot_response("How are you?")},
]

# Print the conversation to the console
print("--- Chatbot Conversation ---")
for message in conversation:
    print(f"{message['role'].title()}: {message['content']}")
print("--------------------------")
''', language='python')

# --- Slide 3: Step 1 ---
with tab3:
    st.header("Step 1: Displaying a Conversation with `st.chat_message`")
    st.markdown("""
    First, let's get our static conversation to display in a proper chat interface. We'll replace the `print()` statements with Streamlit's `st.chat_message` context manager. This gives us the nice chat bubble UI.
    """)
    
    st.code('''
# --- app.py (Version 1) ---
import streamlit as st

def get_bot_response(user_input):
    # ... (same function as before)
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! Thanks for asking."
    else:
        return "I don't understand."

# --- Streamlit Interface ---
st.title("My First Streamlit Chatbot")

conversation = [
    {"role": "user", "content": "Hello bot!"},
    {"role": "assistant", "content": get_bot_response("Hello bot!")},
    {"role": "user", "content": "How are you?"},
    {"role": "assistant", "content": get_bot_response("How are you?")},
]

# Display the static conversation
for message in conversation:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
''', language='python')

# --- Slide 4: Step 2 ---
with tab4:
    st.header("Step 2: Adding Memory with Session State")
    st.markdown("""
    A real chatbot needs to remember the conversation. In Streamlit, the perfect tool for this is `st.session_state`. It's a dictionary-like object that persists across user interactions.

    We'll initialize `st.session_state.messages` to hold our chat history.
    """)
    st.code('''
# --- app.py (Version 2) ---
import streamlit as st

# (get_bot_response function is the same as before)

st.title("Chatbot with Memory")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your friendly chatbot. How can I help?"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# For now, we'll just show that it works with a button.
if st.button("Press me to say hi! 👋"):
    st.session_state.messages.append({"role": "user", "content": "Hello"})
    st.rerun()
''', language='python')

# --- Slide 5: Step 3 ---
with tab5:
    st.header("Step 3: Making it Truly Interactive with `st.chat_input`")
    st.markdown("""
    Now for the final, most important step. Let's replace the button with `st.chat_input` to allow the user to type their own messages. This widget stays pinned to the bottom of the screen and is the core of any Streamlit chatbot.
    """)
    st.code('''
# --- app.py (Version 3 - Final) ---
import streamlit as st
import time

# A more fun bot response function
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hey there! What's up?"
    elif "how are you" in user_input:
        return "Awesome, thanks for asking! Ready to chat."
    elif "your name" in user_input:
        return "I am the Streamlit-Bot 9000. But you can call me Streamy."
    elif "bye" in user_input:
        return "Catch you later! 👋"
    else:
        return "LOL, I have no idea what that means. Try asking something else!"

st.title("🤖 Simple Echo Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! How can I assist you today?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get and display assistant response with a "typing" effect
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = get_bot_response(prompt)
        
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
''', language='python')

# --- Slide 6: Conclusion ---
with tab6:
    st.balloons()
    st.header("You Did It! 🎉")
    st.markdown("""
    Congratulations! You have successfully built a real, interactive chatbot. You learned the three most important concepts for building chatbots in Streamlit:

    - **`st.chat_message`**: To display conversation history in a clean, professional way.

    - **`st.session_state`**: To give your app "memory" and store the chat history across interactions.

    - **`st.chat_input`**: The primary widget for capturing user input in a conversational app.

    You can now use this template to build much more complex bots!
    """)
    st.write("---")
    st.subheader("How was this tutorial?")
    st.radio("Let us know!", ("🤩 Awesome!", "🙂 It was good", "😐 Kinda boring"), horizontal=True)

