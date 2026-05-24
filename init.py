import string

# Define English stop words set
STOP_WORDS = {
    'a', 'an', 'and', 'the', 'or', 'of', 'to', 'in', 'for', 'on', 'with',
    'at', 'by', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him',
    'her', 'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their', 'this',
    'that', 'these', 'those', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
    'may', 'might', 'must', 'can', 'could', 'as', 'but', 'if', 'or', 'because',
    'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
    'into', 'through', 'during', 'before', 'after', 'above', 'below', 'from', 'up',
    'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
    'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
    'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
    'only', 'own', 'same', 'so', 'than', 'too', 'very'
}

def preprocess_text(text):
    """Preprocess text: case conversion, punctuation removal, tokenization, stop word removal"""
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Tokenization (simple space splitting; more complex logic can be used in practical applications)
    tokens = text.split()

    # Remove stop words and empty strings
    tokens = [token for token in tokens if token not in STOP_WORDS and token.strip() != '']

    # Simple stemming (simplified version)
    tokens = [stem_token(token) for token in tokens]

    return tokens

def stem_token(token):
    """Simple stemming function (more complex algorithms can be used in practical applications)"""
    # Handle common suffixes
    suffixes = ['ing', 'ly', 'ed', 'es', 's']
    for suffix in suffixes:
        if token.endswith(suffix) and len(token) > len(suffix):
            return token[:-len(suffix)]
    return token

# Test the preprocessing function
if __name__ == "__main__":
    sample_text = "Machine learning is a subset of artificial intelligence focused on developing algorithms that learn from data."
    processed_tokens = preprocess_text(sample_text)
    print("Preprocessed terms:", processed_tokens)