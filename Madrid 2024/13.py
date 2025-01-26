subjects = input().split(",")
verbs = input().split(",")
sentences = input().split(",")

sol = []
def fsentence(subject,verb):
    first = verb
    for i in sentences:
        for j in range(len(i)):
            if i[j] > first[j]:
                sol.append(subject + " " + verb + " " + i)
                break
            if i[j] < first[j]:
                break
            
def fverb(subject):
    first = subject.lower()

    for i in verbs:
        for j in range(len(i)):
            if i[j] > first[j]:
                fsentence(subject,i)
                break
            if i[j] < first[j]:
                break

for i in subjects:
    fverb(i)

for i in sol:
    print(i)