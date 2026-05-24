from init import preprocess_text

def search(query, documents, inverted_index, tfidf_scores, top_n=3):
    """Process query and return most relevant documents"""
    # Preprocess query
    query_terms = preprocess_text(query)
    if not query_terms:
        return []

    # Get documents containing at least one query term
    relevant_docs = set()
    for term in query_terms:
        if term in inverted_index:
            for doc_id, _ in inverted_index[term]:
                relevant_docs.add(doc_id)
    relevant_docs = list(relevant_docs)

    # Calculate relevance scores between query and each relevant document
    scores = []
    for doc_id in relevant_docs:
        score = 0.0
        for term in query_terms:
            if term in tfidf_scores.get(doc_id, {}):
                score += tfidf_scores[doc_id][term]

        # Normalize score (divide by number of query terms)
        score /= len(query_terms)
        scores.append((doc_id, score))

    # Sort by score
    scores.sort(key=lambda x: x[1], reverse=True)

    # Return top N results
    results = []
    for doc_id, score in scores[:top_n]:
        if score > 0:
            results.append({
                'document': documents[doc_id],
                'score': score,
                'doc_id': doc_id
            })

    return results

# Test search functionality
if __name__ == "__main__":
    import math  # Ensure math library is imported
    # query = "machine learning"
    # results = search(query, documents, inverted_index, tfidf_scores)
    # print(f"Query: {query}")
    # for i, result in enumerate(results, 1):
    #     print(f"\n Result {i} (Score: {result['score']:.4f}):")
    #     print(result['document'])
    pass