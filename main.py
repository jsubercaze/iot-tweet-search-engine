# file for test

from parser import Parser
from user import User

if __name__ == '__main__':
	corpus = Parser.parsing_iot_corpus('corpus/fake-iot-corpus.tsv')

	print(corpus)

	# model = gensim.models.KeyedVectors.load_word2vec_format('corpus/GoogleNews-vectors-negative300.bin', binary=True)
	#
	# tweet_cliked_1 = tweet2vec(corpus[1]['Text'], model)
	# tweet_cliked_2 = tweet2vec(corpus[2]['Text'], model)
	# tweet_cliked_3 = tweet2vec(corpus[3]['Text'], model)

	tweet_cliked_1 = corpus[1]['Vector']
	tweet_cliked_2 = corpus[2]['Vector']
	tweet_cliked_3 = corpus[3]['Vector']

	u1 = User()
	u1.update_profile(tweet_cliked_1)
	u1.save()

	u2 = User()
	u2.update_profile(tweet_cliked_2)
	u2.save()

	u3 = User()
	u3.update_profile(tweet_cliked_3)
	u3.save()
