from llama_summarizer import Llama_Summarizer


def get_summary(text):

    choice = int(input('Enter 1 for the LLAMA summary \n 2 for the openAI summary \n 3 for the ... summary'))

    if choice == 1:
        return Llama_Summarizer