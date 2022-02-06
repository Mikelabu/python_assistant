# importing the module
import wikipedia

while True:
    # user question input
    question = input("Q:")
    # set refered language https://meta.wikimedia.org/wiki/List_of_Wikipedias
    wikipedia.set_lang("en")
    # need a summary of input
    answer = wikipedia.summary(question, sentences=2)
    print(answer)
