print("Yahya Shamim")
print("24k-0020")
print("Q2")
print()

social_posts = [
    {'id': 1, 'text': "I LOVE the new #GulPhone! Battery life is amazing."},
    {'id': 2, 'text': "My #GulPhone is a total disaster. The screen is already broken!"},
    {'id': 3, 'text': "Worst customer service ever from @GulPhoneSupport. Avoid!"},
    {'id': 4, 'text': "The @GulPhoneSupport team was helpful and resolved my issue. Great service!"}
]

PUNCTUATION_CHARS = ['.', ',', '!', '?', ':', ';', "'", '"']
STOPWORDS_SET = {'i', 'me', 'my', 'an', 'the', 'is', 'am', 'was', 'to', 'of', 'by', 'for', 'and', 'with', 'this', 'that'}

POSITIVE_WORDS = {'love', 'amazing', 'great', 'helpful', 'resolved'}
NEGATIVE_WORDS = {'disaster', 'broken', 'bad', 'worst', 'avoid'}

def preprocessText(text, punctuationList, stopwordsSet):
    lowercase_text = text.lower()
    for symbol in punctuationList:
        lowercase_text = lowercase_text.replace(symbol, "")
    word_list = lowercase_text.split()
    return [term for term in word_list if term not in stopwordsSet]

def analyzePosts(postsList, punctuation, stopwords, positive, negative):
    def calculatePostScore(post_item):
        cleaned_words = preprocessText(post_item["text"], punctuation, stopwords)
        sentiment_value = 0
        for term in cleaned_words:
            if term in positive:    sentiment_value += 1
            elif term in negative:  sentiment_value -= 1
        return {
            "id": post_item["id"],
            "text": post_item["text"],
            "processedText": cleaned_words,
            "score": sentiment_value
        }
    return [calculatePostScore(post) for post in postsList]

def getFlaggedPosts(scoredPosts, sentimentThreshold=-1):
    return [post_item for post_item in scoredPosts if post_item["score"] <= sentimentThreshold]

def findNegativeTopics(flaggedPosts):
    topic_counts = {}
    for post_item in flaggedPosts:
        for term in post_item["processedText"]:
            if term.startswith("#") or term.startswith("@"):
                topic_counts[term] = topic_counts.get(term, 0) + 1
    return topic_counts

scored_posts_result = analyzePosts(social_posts, PUNCTUATION_CHARS, STOPWORDS_SET, POSITIVE_WORDS, NEGATIVE_WORDS)
flagged_posts_result = getFlaggedPosts(scored_posts_result, sentimentThreshold=-1)
negative_topics_result = findNegativeTopics(flagged_posts_result)

print("Post Analysis Results:\n", scored_posts_result)
print("\nPosts Flagged as Negative:\n", flagged_posts_result)
print("\nNegative Posts:\n", negative_topics_result)