print("Chill guy translator - test version")
print("Use only korean.")

filter_texts = ["칠", "치", "질", "지", "7"]

text = input(">>")

for i in filter_texts:
    text = text.replace(i, "chill")

print(f"translator text : {text}")