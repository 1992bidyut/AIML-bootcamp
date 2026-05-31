# Regular expressions, or "regex" for short, is a special syntax for searching for strings that meets a specified pattern. 
# It's a great tool to filter and sort through text when you want to match patterns rather than a hard coded string or strings.

# There are loads of options for the syntax so it's best to just jump in and get started with some examples.

import re

# re.search is a function which allows us to check if a certain pattern is in a string. It uses the logic re.search("pattern to find", "string to find it in"). 
# It will return the pattern if it is found in the string, or else it will return None if the pattern is not found.
result_search = re.search("pattern", r"string containing the pattern")
print(result_search)

print(result_search.group()) # returns just the matching pattern

result_search = re.search("pattern",r"the phrase to find isn't in this string")
print(result_search) # returns None


# re.sub allows us to find certain text and replace it. It uses the logic re.sub("pattern to find", "replacement text", "string").
string = r"sara was able to help me find the items i needed quickly"
new_string = re.sub(r"sara", r"sarah", string) # replace the incorrect spelling of sarah
print(new_string)

# The real power of regex is being able to leverage the syntax to create more complex searches/replacements.
customer_reviews = ['sam was a great help to me in the store', 
                    'the cashier was very rude to me, I think her name was eleanor', 
                    'amazing work from sadeen!', 
                    'sarah was able to help me find the items i needed quickly', 
                    'lucy is such a great addition to the team', 
                    'great service from sara she found me what i wanted'
                   ]


# Find only sarah's reviews but account for the spelling of sara
sarahs_reviews = []
pattern_to_find = r"sarah?" 
# the ? after r means it is an optional character to match, so our search will look for sarah and sara
for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        sarahs_reviews.append(string)
print(sarahs_reviews)


# Find reviews that start with the letter a
a_reviews = []
pattern_to_find = r"^a" # the ^ operator to indicates the start of a string
for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        a_reviews.append(string)
print(a_reviews)


# Find reviews that end with the letter y
y_reviews = []
pattern_to_find = r"y$" # the $ operator to indicate the end of a string
for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        y_reviews.append(string)
print(y_reviews)


# Find reviews that contain the words needed or wanted
needwant_reviews = []
pattern_to_find = r"(need|want)ed" # the pipe operator | can be used to mean OR
for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        needwant_reviews.append(string)
print(needwant_reviews)


# Remove anything from the review that isn't a word or a space (i.e. remove punctuation)
no_punct_reviews = []
pattern_to_find = r"[^\w\s]" 
# [^ ] means "not", \w means word and \s means whitespace: so find anything that is not a word or a space
for string in customer_reviews:
    no_punct_string = re.sub(pattern_to_find, "", string)
    no_punct_reviews.append(no_punct_string)
print(no_punct_reviews)