def text_statistics(text):
    # Clean and prepare text
    words = text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').split()
    
    # Basic stats
    char_count = len(text)
    word_count = len(words)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    # Word frequency
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Find most common word
    most_common = max(word_freq.items(), key=lambda x: x[1]) if word_freq else ("", 0)
    
    # Average word length
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    
    return {
        "characters": char_count,
        "words": word_count,
        "sentences": sentence_count,
        "avg_word_length": round(avg_word_length, 2),
        "most_common_word": most_common[0],
        "most_common_count": most_common[1],
        "word_frequencies": word_freq
    }

# Test text
sample_text = "Hello world! This is a test. Hello again, world. This test is working!"
print(text_statistics(sample_text))