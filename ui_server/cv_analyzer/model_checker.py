import nltk, string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

class ModelChecker:
    def get_score(self, d1, d2):

        documents = [d1, d2]
        # nltk.download('punkt')  # first-time use only
        # nltk.download('wordnet') # first-time use only

        lemmer = nltk.stem.WordNetLemmatizer()

        def LemTokens(tokens):
            return [lemmer.lemmatize(token) for token in tokens]
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        def LemNormalize(text):
            return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

        LemVectorizer = CountVectorizer(tokenizer=LemNormalize, stop_words='english')
        LemVectorizer.fit_transform(documents)

        print (LemVectorizer.vocabulary_)

        tf_matrix = LemVectorizer.transform(documents).toarray()
        print (tf_matrix)


        tfidfTran = TfidfTransformer(norm="l2")
        tfidfTran.fit(tf_matrix)
        print (tfidfTran.idf_)

        import math
        def idf(n,df):
            result = math.log((n+1.0)/(df+1.0)) + 1
            return result

        print ("The idf for terms that appear in one document: " + str(idf(4,1)))
        print ("The idf for terms that appear in two documents: " + str(idf(4,2)))

        tfidf_matrix = tfidfTran.transform(tf_matrix)
        print (tfidf_matrix.toarray())

        cos_similarity_matrix = (tfidf_matrix * tfidf_matrix.T).toarray()
        print (cos_similarity_matrix)

        score_cv = cos_similarity_matrix[0][1]

        print('cv score is ' + str(score_cv))
        return score_cv
