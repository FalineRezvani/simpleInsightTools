## Language Modeling

Natural Language Processing (NLP) is a field of study combining linguistics, statistics, and machine learning.  Users might find this useful for information extraction, text summarization, question answering, or translation.

### [Extractive Text Summarization with Sentence Transformers and LexRank](https://github.com/FalineRezvani/simpleInsightTools/blob/main/languageModeling/sentenceTransformersWithLexRank.ipynb)

Using language models with pre-trained embeddings, such as [Sentence Transformers](https://sbert.net/) allows users to quickly discover similarities in text that has been parsed with a tool, such as [LexRank](https://github.com/crabcamp/lexrank/tree/dev), with the help of [sumy](https://miso-belica.github.io/sumy/) for extractive text summarization, and tokenized with a tool, such as [NLTK](https://www.nltk.org/install.html).

### [Generating Text with N-Grams](https://github.com/FalineRezvani/simpleInsightTools/blob/main/languageModeling/countBasedLanguageModel.ipynb)
Count-based language models use conditional probability, specifically [n-grams](https://www.youtube.com/watch?v=p-wgw9R3fRU&list=PLhLmrhdjYUTGLt-q7mPvS-Mh2zjn43bLs&index=1), for word prediction.  These models predict the second word based on one word (bigram), the third word based on two words (trigram), and so on.
