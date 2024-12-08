import utils
import streamlit as st
from streaming import StreamHandler

# from fewshotvector import chain

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# st.set_page_config(page_title="Chatbot", page_icon="💬")
st.header('Basic Chatbot')
st.write('Allows users to interact with the LLM')
st.write('[![view source code ](https://img.shields.io/badge/view_source_code-gray?logo=github)](https://github.com/shashankdeshpande/langchain-chatbot/blob/master/pages/1_%F0%9F%92%AC_basic_chatbot.py)')

class VectorDBChatbot:

    def __init__(self):
        # utils.sync_st_session()

        # self.llm = utils.configure_llm()
        # print("running init")

        if "messages" not in st.session_state:
            st.session_state["messages"] = []
        #load embedding model


    # def setup_chain(self):
    #     chain = ConversationChain(llm=self.llm, verbose=False)
    #     print("running chain")
    #     return chain
    
    @utils.enable_chat_history
    def main(self):
        print("running main")
        # chain = self.setup_chain()
        user_query = st.chat_input(placeholder="Ask me anything!")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())

                # print("invoking")
                # result = chain.invoke(
                #     {"input": "get some beef recipe"},
                #     {"callbacks": [st_cb]}
                # )
                # print(result)
                result = "hard code"
                # response = result["content"]

                # result = self.llm.invoke(
                #     {"input":user_query},
                #     {"callbacks": [st_cb]}
                # )

                # print(result)
                # response = str(result["response"])

                st.session_state.messages.append({"role": "assistant", "content": result})
                # print(st.session_state.messages)
                utils.print_qa(VectorDBChatbot, user_query, result)

# if __name__ == "__main__":
obj = VectorDBChatbot()
obj.main()