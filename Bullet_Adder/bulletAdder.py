import pyperclip

text = pyperclip.paste()
# text = "Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars"
lines = text.split("\\n")

# Add bullet points
final_text = ""
for i in lines:
    i = "*" + i + "\n"
    final_text += i
pyperclip.copy(final_text)