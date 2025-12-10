# started at 5:30 am to 6:30am 

# write a python function that takes a sentence and returns the longest word along with its length

def longest_word(sentence):

# slpit() convets the string into list or the sentence into words
    words=sentence.split()

# using max function for longest word 
    longest_word=max(words,key=len)

    return longest_word

# user input

sentence=input("Enter a sentnce:")
result=longest_word(sentence)

print(f"the longest word is : {result}")




