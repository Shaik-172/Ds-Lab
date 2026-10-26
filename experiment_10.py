# Experiment 10

# ============================================================
# DATA SCIENCE - PROGRAM 10
# CASE STUDY: TEXT EMOTION DETECTION
# ============================================================
#
# AIM:
# ----
# To detect emotions from text messages using
# Machine Learning techniques.
#
# In this program we:
#
# 1. Create sample text data.
# 2. Convert text into numerical features.
# 3. Train a Naive Bayes classifier.
# 4. Predict emotion for new text.
#
# ============================================================

# ============================================================
# IMPORT REQUIRED LIBRARIES
# ============================================================

# CountVectorizer converts text into numerical vectors.
# Machine learning algorithms cannot understand text directly.
# Therefore, text must be converted into numbers.
from sklearn.feature_extraction.text import CountVectorizer

# MultinomialNB is a Naive Bayes classification algorithm.
# It is commonly used for text classification tasks.
from sklearn.naive_bayes import MultinomialNB

# ============================================================
# CREATE SAMPLE TRAINING DATA
# ============================================================

# List of sample text messages.
texts = [
    "I am happy",
    "I am angry",
    "I feel sad",
    "I love this"
]

# Corresponding labels (emotions).
labels = [
    "happy",
    "angry",
    "sad",
    "happy"
]

# Display training data.
print("=" * 60)
print("TRAINING DATA")
print("=" * 60)

for sentence, emotion in zip(texts, labels):
    print(f"Text: {sentence} --> Emotion: {emotion}")

# ============================================================
# TEXT VECTORIZATION
# ============================================================

# Create CountVectorizer object.
#
# CountVectorizer converts words into numerical features.
#
# Example:
#
# Text: "I am happy"
#
# May become:
#
# [1,1,1,0,0]
#
# depending on the vocabulary.
vec = CountVectorizer()

# Learn vocabulary from training data.
# Convert text into numerical matrix.
X = vec.fit_transform(texts)

# Display all learned words.
print("\n")
print("=" * 60)
print("VOCABULARY")
print("=" * 60)

print(vec.get_feature_names_out())

# Display numerical representation.
print("\n")
print("=" * 60)
print("VECTORIZED DATA")
print("=" * 60)

print(X.toarray())

# ============================================================
# TRAIN MACHINE LEARNING MODEL
# ============================================================

# Create Multinomial Naive Bayes model.
model = MultinomialNB()

# Train the model.
#
# X      -> Features
# labels -> Target classes
model.fit(X, labels)

print("\nModel Training Completed Successfully")

# ============================================================
# TEST DATA
# ============================================================

# New sentence whose emotion must be predicted.
new_text = ["I am so sad today"]

print("\n")
print("=" * 60)
print("TEST SENTENCE")
print("=" * 60)

print(new_text)

# Convert test text into numerical representation
# using the vocabulary learned earlier.
test = vec.transform(new_text)

# Display vectorized form of test data.
print("\nVectorized Test Data:")
print(test.toarray())

# ============================================================
# PREDICTION
# ============================================================

# Predict emotion.
prediction = model.predict(test)

# Display prediction.
print("\n")
print("=" * 60)
print("PREDICTED EMOTION")
print("=" * 60)

print(prediction[0])

# ============================================================
# ADDITIONAL TEST CASES
# ============================================================

sample_sentences = [
    "I love my friends",
    "I am angry with you",
    "I feel very sad",
    "Today I am happy"
]

print("\n")
print("=" * 60)
print("MULTIPLE PREDICTIONS")
print("=" * 60)

for sentence in sample_sentences:

    # Convert text into vector
    sample_vector = vec.transform([sentence])

    # Predict emotion
    result = model.predict(sample_vector)

    print(f"{sentence} --> {result[0]}")

# ============================================================
# END OF PROGRAM
# ============================================================

print("\n")
print("=" * 60)
print("TEXT EMOTION DETECTION COMPLETED")
print("=" * 60)
