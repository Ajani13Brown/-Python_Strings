# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". 
# Print out each review with the keywords in uppercase so they stand out.

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
keywords = ['good','excellent','bad','poor','average']
keyword_list = []
def keyword_check():
    for review in python_reviews:
        for word in keywords:
            if word in review.lower():
                keyword_list.append(review)
        
    for review in keyword_list:
        word_check = review.split()
        for segment in word_check:
            if word in segment.lower():
                print(segment.upper())


        
keyword_check()

# The assignmet isnt complete, Unfortunatly i had a great deal trouble with this assignmet and was unable to get very far
# I am uploading what i have managed to complete so far and if able will resubmit the completed assignmet before the start of the next week.


