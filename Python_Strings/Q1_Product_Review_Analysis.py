# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". 
# Print out each review with the keywords in uppercase so they stand out.

#python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

# keywords = ['good','excellent','bad','poor','average']
# keyword_list = []
# def keyword_check():
#     for review in python_reviews:
#         for word in keywords:
#             if word in review.lower():
#                 keyword_list.append(review)
        
#     for review in keyword_list:
#         word_check = review.split()
#         for segment in word_check:
#             if word in segment.lower():
#                 print(segment.upper())

# this is the old code that i complete prior to review in preclass below is the new solution.

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

        
# def keyword_check():
#     python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
#     keywords = ['good','excellent','bad','poor','average']
#     for review in python_reviews:
#         for word in keywords:
#             if word in review.lower():
#                 keyword_reviews = review.lower().replace(word,word.upper())
                #print(keyword_reviews)


#keyword_check()

#Task 2: Sentiment Tally
#Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative
#words to check against. The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def pos_and_neg_count():
    for review in python_reviews:
        for word in positive_words:
            if word in review.lower():
                print(review)

pos_and_neg_count()