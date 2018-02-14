#Python program to count the occurrences of each word in a given sentence

# Example sentence
str1 = 'Reading Is To The Mind, As Exercise Is To The Body.'

# Function to count the occurrences of each word in a given sentence
def count_word_times(str):
    
    words_count = dict()
    words = str.split()

    for word in words:
        if word in words_count:
            words_count[word]+=1
        else:
            words_count[word]=1
    return words_count

# Testing the above defined function
print("Occurrences of each word in given sentence:: ", count_word_times(str1))
 
