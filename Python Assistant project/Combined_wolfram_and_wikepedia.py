import wolframalpha
import wikipedia

# question needs to be replaced with input when combining code with main
while True:
    question = input("Your Question:")

    try:
        # wolframalpha
        app_id = "52EE7V-6X76VJVT2K"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        # .text will ensure text amswers only
        answer = next(res.results).text
        print(answer)

    except:
        # wikipedia
        answer = wikipedia.summary(question, sentences=2)
        print(answer)
