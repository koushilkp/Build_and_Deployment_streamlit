import openai
import streamlit as st
import time
import random


# st.title('Chatbot with OpenAI and ChatGPT')

# openai.api_key = st.secrets["open_api_Key"]

# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "GPT-4o mini"

# # initizate the chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # dispaly the chat history from chat app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message['role']):
#         st.markdown(message['content'])

# # react to the user input
# promp = st.chat_input("What is up?")
# if promp:
#     with st.chat_message("user"):
#         st.markdown(promp)
#         st.session_state.messages.append(
#             {
#                 "role": "user",
#                 "content": promp
#             }
#         )

#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response =""

#         for response in openai.chat.completions.create(
#             model= st.session_state["openai_model"],
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         ):
            
#             full_response += response['choices'][0].delta.get('content',"")
#             message_placeholder.markdown(full_response + "🖊️")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append(
#             {
#                 "role": "assistant",
#                 "content": full_response
#             }
#         )

# ---------------------------------------------------------
# stream response Application
def response_genarate():
    response =random.choice(

        [
            "hey_check_this_out_and_update_the_link  : https://www.youtube.com/watch?v=9n4Ch2Dgex0&t=85s ",
            "for_the_excel_Automation_video : https://www.youtube.com/watch?v=Sb0A9i6d320"
        ]
    )

    for word in response.split():
        yield word +''
        time.sleep(0.05)

st.title('Chatbot')

# initizalize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# dispaly the chat message from the history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Accept the user input
if prompt:= st.chat_input("what is up?"):
    # add the uses message in the chat history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # display the chat message in the chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display the Assistance respone in that message container
    with st.chat_message("assistant"):
        response =st.write_stream(response_genarate())

    # Add assistance to response to chagt history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    ) 