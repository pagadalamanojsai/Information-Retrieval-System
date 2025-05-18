import streamlit as st
from src.helper import get_pdf_text
from src.helper import get_text_chunks
from src.helper import get_vector_store
from src.helper import get_conversational_chain
# from dotenv import load_dotenv

def user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i%2 == 0:
            st.write("User: ", message.content)
        else:
            st.write("Reply: ", message.content)



def main():
    st.set_page_config("Information Retrieval")
    st.header ("Information-Retrieval-System")

    user_question = st.text_input("Ask a question about the PDF documents:")

    if 'conversation' not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if user_question:
        user_input(user_question)  
    


    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload PDF", type="pdf", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.snipper("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chuncks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chuncks)
                st.session_state.conersation =  get_conversational_chain(vector_store)



                st.success("Done")

 

if __name__ == "__main__":
    main()
# This is the main entry point of the application. It sets up the Streamlit app and runs the main function.
# The main function sets the page configuration and header for the Streamlit app.
# The `if __name__ == "__main__":` block ensures that the main function is called when the script is run directly.
# The `main()` function is defined to encapsulate the main logic of the application.
# The `st.set_page_config` function is used to set the configuration for the Streamlit app, such as the title and layout.
# The `st.header` function is used to display a header in the Streamlit app.
# The `st` module is imported from the Streamlit library, which is used for building web applications in Python.
# The `main()` function is called to start the application.

# run it in terminal
# streamlit run app.py