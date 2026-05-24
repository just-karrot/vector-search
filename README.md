# Python based tf-idf search engine
This is a simple inverted index search engine built entirely from scratch in python. it does not use any third party libraries, so you can see exactly how the core concepts work behind the scenes.

## How it Works
A search engine basically does four things. it cleans up the text, builds a map of the words, figures out what is important, and then searches through that map when you ask for something.

### Text Processing
before we can search for anything we have to clean up the raw text. we make everything lowercase, take out the punctuation, and split the sentences into individual words. we also filter out common stop words like "the" and "and" because they just take up space and do not help us find what we are looking for.

### Inverted Index
This is the heart of the search engine. instead of reading every single document every time you search, we build an index beforehand. it works just like the index at the back of a book. we record every word we find, which documents have it, and exactly where it showed up in the text. we save all of this to a csv file so we can just load it up later without having to do the work again.

### Scoring with TF-IDF
this is how we rank the results so you get the most relevant stuff first. it stands for term frequency and inverse document frequency, but the concept is pretty straightforward. term frequency is just how often a word appears in a specific document. the more it shows up, the more relevant that document probably is. Inverse document frequency looks at how rare the word is across all the documents we have. if a word is everywhere, it is not very helpful for finding specific things, so it gets a lower score. if it is rare, it gets a high score. we just multiply these two numbers together to get the final score for each word in a document.

### How to Run it
all the files are laid out so they handle one specific part of the job. just run the main script and it will execute everything in sequence and check if each step is working properly. python main.py

## Project Structure
- init.py: handles the text cleanup and filtering
- index.py: reads the documents and builds the inverted index
- load.py: loads the saved index from the csv file
- tfidf.py: does all the math to calculate the relevance scores
- process.py: takes your search query and ranks the matching documents
- main.py: runs all of these steps in order and validates them