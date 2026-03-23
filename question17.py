sentence = input("Entrez une phrase : ")
words = sentence.lower().split()
word_count = len(words)
# mot le plus long
longest_word = max(words, key=len)
# comptage des occurrences
from collections import Counter
occurrences = Counter(words)

print(f"Nombre total de mots : {word_count}")
print(f"Mot le plus long : {longest_word}")
print("Occurrences :")
for word, count in occurrences.items():
    print(f" - {word} : {count}")
