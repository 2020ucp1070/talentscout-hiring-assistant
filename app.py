import streamlit as st
from prompts import get_intro_prompt, get_tech_questions_prompt
from utils import ask_llm

st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")

st.title("🧠 TalentScout Hiring Assistant Chatbot")
st.write("Welcome to TalentScout! I’ll help collect your info and assess your tech skills.")

if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "step" not in st.session_state:
    st.session_state.step = 0
if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}

def handle_conversation(user_input):
    step = st.session_state.step
    candidate_data = st.session_state.candidate_data

    if step == 0:
        st.session_state.conversation.append(("bot", get_intro_prompt()))
        st.session_state.step += 1

    elif step == 1:
        candidate_data["name"] = user_input
        st.session_state.step += 1
        st.session_state.conversation.append(("bot", "Great! What's your email address?"))

    elif step == 2:
        candidate_data["email"] = user_input
        st.session_state.step += 1
        st.session_state.conversation.append(("bot", "Phone number?"))

    elif step == 3:
        candidate_data["phone"] = user_input
        st.session_state.step += 1
        st.session_state.conversation.append(("bot", "How many years of experience do you have?"))

    elif step == 4:
        candidate_data["experience"] = user_input
        st.session_state.step += 1
        st.session_state.conversation.append(("bot", "Which position are you applying for?"))

    elif step == 5:
        candidate_data["position"] = user_input
        st.session_state.step += 1
        st.session_state.conversation.append(("bot", "What’s your current location?"))

    elif step == 6:
        candidate_data["location"] = user_input
        st.session_state.step += 1
        st.session_state.conversation.append(("bot", "Please list your tech stack (languages, frameworks, databases, etc)."))

    elif step == 7:
        candidate_data["tech_stack"] = user_input
        st.session_state.step += 1
        # Generate tech questions
        question_prompt = get_tech_questions_prompt(candidate_data["tech_stack"])
        questions = ask_llm(question_prompt)
        st.session_state.conversation.append(("bot", "Thanks! Here are some technical questions based on your skills:\n\n" + questions))
        st.session_state.conversation.append(("bot", "This concludes our interview. We'll get back to you soon. Thanks!"))
    
    else:
        st.session_state.conversation.append(("bot", "Thank you! Type 'exit' to end the chat."))

st.session_state.conversation.append(("bot", get_intro_prompt()))
user_input = st.chat_input("Type your response here...")

if user_input:
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.session_state.conversation.append(("bot", "Thanks for your time! Goodbye 👋"))
    else:
        st.session_state.conversation.append(("user", user_input))
        handle_conversation(user_input)

for speaker, message in st.session_state.conversation:
    with st.chat_message(speaker):
        st.markdown(message)
