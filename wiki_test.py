import wikipedia

wikipedia.set_lang("en")

try:
    print(wikipedia.summary("Prabhas", sentences=2))
except Exception as e:
    print(type(e))
    print(e)