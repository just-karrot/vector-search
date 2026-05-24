import math
from init import preprocess_text

def calculate_tfidf(documents, inverted_index):
    """Calculate TF-IDF values for each term in each document"""
    num_docs = len(documents)
    tfidf = {}  # Structure: {doc_id: {term: tfidf_value, ...}, ...}

    # Calculate total number of terms for each document
    doc_lengths = []
    for doc in documents:
        tokens = preprocess_text(doc)
        doc_lengths.append(len(tokens))

    # Calculate document frequency for each term (number of documents containing the term)
    doc_freq = {term: len(entries) for term, entries in inverted_index.items()}

    # Calculate TF-IDF
    for term, entries in inverted_index.items():
        # Calculate IDF
        idf = math.log(num_docs / (doc_freq[term] + 1))  # +1 to avoid division by zero

        for doc_id, positions in entries:
            # Calculate TF
            tf = len(positions) / doc_lengths[doc_id] if doc_lengths[doc_id] > 0 else 0

            # Calculate TF-IDF
            tfidf_value = tf * idf

            # Store results
            if doc_id not in tfidf:
                tfidf[doc_id] = {}
            tfidf[doc_id][term] = tfidf_value

    return tfidf

# Calculate TF-IDF values
if __name__ == "__main__":
    tfidf_scores = calculate_tfidf(documents, inverted_index)
    print("TF-IDF calculation completed")