import csv
from init import preprocess_text
from collections import defaultdict

def build_inverted_index(documents):
    """Build inverted index and store as CSV file"""
    inverted_index = defaultdict(list)  # Structure: {term: [(doc_id, positions), ...]}

    for doc_id, doc in enumerate(documents):
        # Preprocess the document
        tokens = preprocess_text(doc)

        # Record positions of each term in the current document
        term_positions = defaultdict(list)
        for pos, term in enumerate(tokens):
            term_positions[term].append(pos)

        # Update inverted index
        for term, positions in term_positions.items():
            inverted_index[term].append((doc_id, positions))

    # Store inverted index as CSV file
    with open('inverted_index.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['term', 'doc_id', 'positions'])
        for term, doc_info in inverted_index.items():
            for doc_id, positions in doc_info:
                # Convert position list to string for storage
                positions_str = str(positions)
                writer.writerow([term, doc_id, positions_str])

    return inverted_index

# Sample document collection
documents = [
    "Machine learning is a subset of artificial intelligence focused on developing algorithms that learn from data.",
    "Artificial intelligence involves creating systems that can perform tasks requiring human intelligence.",
    "Deep learning is a type of machine learning based on artificial neural networks with multiple layers.",
    "Natural language processing allows computers to understand and generate human language.",
    "Computer vision enables machines to interpret and understand the visual world.",
    "Reinforcement learning is an area of machine learning concerned with how agents take actions in an environment.",
    "Supervised learning algorithms learn from labeled training data to make predictions on new data.",
    "Unsupervised learning deals with unlabeled data, finding patterns and structures within it.",
    "A neural network is a computational model inspired by the human brain's structure and function.",
    "Big data refers to large and complex data sets that require advanced processing techniques."
]

# Build inverted index
if __name__ == "__main__":
    inverted_index = build_inverted_index(documents)
    print(f"Inverted index built, containing {len(inverted_index)} terms")