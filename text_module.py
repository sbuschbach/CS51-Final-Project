
def name = # scrapy name of article

def publication = # scrapy's publication in ArticleItem

# frequency of each pronoun's occurence in textcd
def pronoun_list = 
    # text -> (int*pronoun) list
  
# frequency of different conjunctions  
def conjunction =
    # text -> (int*conjunctions) list

# frequency of different punctuation characters
def punctuation =
    # text -> (character*conjunctions) list

# length of words in article on average
def average_word =
    # text -> int
    
# length of sentences in article on average
def average_sentence = 
    # text -> int
    
# list of words that appear above a threshold number of times
def freq_words =
    # text -> int -> string list
