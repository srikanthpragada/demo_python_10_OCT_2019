# Word frequency
f = open("words.txt","rt")
freq = {}

for line in f:
    words = line.strip("\n").strip(" ").split(" ")
    for w in words:
        if len(w.strip(" ")) == 0:
            continue

        # if word is already in dict then increment count
        # otherwise add it with count 1
        if w in freq:
            freq[w] = freq[w] + 1
        else:
            freq[w] = 1

f.close()

for word,count in sorted(freq.items()):
    print(f"{word:10s} {count}")


