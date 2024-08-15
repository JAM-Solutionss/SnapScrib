from llama_summarizer import Llama_Summarizer


def get_summarizer():

    choice = int(input("Enter 1 for the LLAMA summary \n"))

    if choice == 1:
        return Llama_Summarizer
