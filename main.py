import os
import sys
from index import documents, build_inverted_index
from load import load_inverted_index_from_csv
from tfidf import calculate_tfidf
from process import search

def main():
    print("--- Starting Search Engine Orchestration ---")

    # Step 1: Validate Documents
    print("Step 1: Validating document collection...")
    if not documents or len(documents) == 0:
        print("Error: Document collection is empty.")
        sys.exit(1)
    print(f"Success: Found {len(documents)} documents.")

    # Step 2: Build Inverted Index
    print("\nStep 2: Building inverted index...")
    inverted_index = build_inverted_index(documents)
    if not inverted_index:
        print("Error: Inverted index construction failed.")
        sys.exit(1)
    
    csv_file = 'inverted_index.csv'
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} was not created.")
        sys.exit(1)
    print(f"Success: Inverted index built and saved to {csv_file}.")

    # Step 3: Load Inverted Index from CSV
    print("\nStep 3: Loading inverted index from CSV...")
    loaded_index = load_inverted_index_from_csv(csv_file)
    if not loaded_index or len(loaded_index) == 0:
        print("Error: Failed to load inverted index from CSV.")
        sys.exit(1)
    print(f"Success: Loaded {len(loaded_index)} terms from CSV.")

    # Step 4: Calculate TF-IDF Scores
    print("\nStep 4: Calculating TF-IDF scores...")
    tfidf_scores = calculate_tfidf(documents, loaded_index)
    if not tfidf_scores:
        print("Error: TF-IDF calculation failed.")
        sys.exit(1)
    print("Success: TF-IDF scores calculated.")

    # Step 5: Execute Search
    query = "machine learning"
    print(f"\nStep 5: Executing search for query: '{query}'...")
    results = search(query, documents, loaded_index, tfidf_scores)
    
    if not isinstance(results, list):
        print("Error: Search function did not return a list.")
        sys.exit(1)
    
    if len(results) == 0:
        print("Warning: No results found.")
    else:
        print(f"Success: Found {len(results)} results.")
        for i, result in enumerate(results, 1):
            print(f"\n Result {i} (Score: {result['score']:.4f}):")
            print(f" Doc ID {result['doc_id']}: {result['document']}")

    print("\n--- Search Engine Orchestration Completed Successfully ---")

if __name__ == "__main__":
    main()
