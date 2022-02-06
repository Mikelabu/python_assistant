# Wolfram ID 52EE7V-6X76VJVT2K

import wolframalpha

input = input("Question: ")
app_id = "52EE7V-6X76VJVT2K"
client = wolframalpha.Client(app_id)

res = client.query(input)
# .text will ensure text amswers only
answer = next(res.results).text

print(answer)
