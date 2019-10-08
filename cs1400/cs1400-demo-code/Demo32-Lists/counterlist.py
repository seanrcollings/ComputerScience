str1 = "ancnklweldalksdfolnqpqwenzvlldifalkdflnqlasdliasfnla"

counter_list = [0] * 26

for ch in str1:
    counter_list[ord(ch) - ord("a")] += 1

for i in range(len(counter_list)):
    print(chr(i + ord("a")) + ": " + str(counter_list[i]))