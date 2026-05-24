import csv
from collections import defaultdict

def load_inverted_index_from_csv(filename):
    """Load inverted index from CSV file"""
    inverted_index = defaultdict(list)

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header

        for row in reader:
            term = row[0]
            doc_id = int(row[1])

            # Convert position string back to list
            positions = eval(row[2])  # Note: eval has security risks; use safer methods in practical applications

            inverted_index[term].append((doc_id, positions))

    return inverted_index

# Test loading inverted index
if __name__ == "__main__":
    try:
        loaded_index = load_inverted_index_from_csv('inverted_index.csv')
        print(f"Inverted index loaded from CSV contains {len(loaded_index)} terms")
    except FileNotFoundError:
        print("inverted_index.csv not found. Please run index.py first.")