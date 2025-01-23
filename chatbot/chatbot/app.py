import os
import asyncio
import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent

from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"]="AIzaSyA-1Yo0_VuJx3fOk7L5qtF_mQMUWnsog_4"

async def get_answer_by_sql_query(db,input):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-8b",temperature=0)
    agent_executor = create_sql_agent(llm, db=db, verbose=True)
    
    response= agent_executor.invoke({"input": input})
    return response


def main():
    st.header('Chat with your resQSquad Chatbot...')
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "activate_chat" not in st.session_state:
        st.session_state.activate_chat = False

    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.chat_history=[]

    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar = message['avatar']):
            st.markdown(message["content"])

    with st.sidebar:
        st.subheader('resQSquad Chatbot connected to database according to given credentials.')
        username = 'postgres'
        password=  '8564'
        hostname=  'localhost'
        port_number=  '5432'
        db_name=  'postgres'
        if username is not None and password is not None:
                postgres_uri = f"postgresql+psycopg2://{username}:{password}@{hostname}:{port_number}/{db_name}"
                st.write(f'Processed database: {postgres_uri}')
                st.write(f'Connection to database successfully..')

                db = SQLDatabase.from_uri(postgres_uri)
                if "db" not in st.session_state:
                    st.session_state.db = db
                st.session_state.activate_chat = True

    if st.session_state.activate_chat == True:
        if prompt := st.chat_input("Ask your question from the Database"):
            with st.chat_message("user", avatar = '👨🏻'):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user",  "avatar" :'👨🏻', "content": prompt})
            db = st.session_state.db
            response = asyncio.run(get_answer_by_sql_query(db,prompt))
            cleaned_response=response["output"]
            with st.chat_message("assistant", avatar='🤖'):
                st.markdown(cleaned_response)
            st.session_state.messages.append({"role": "assistant",  "avatar" :'🤖', "content": cleaned_response})
        else:
            st.markdown('Please Enter your credentials to chat')


if __name__ == '__main__':
    main()