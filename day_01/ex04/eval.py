class Evaluator:
	@staticmethod
	def check_input(coefs, words):
		try:
			if not isinstance(coefs, list):
				raise Exception("coefs")
			if not all(isinstance(elem, float) for elem in coefs):
				raise Exception("elem in coefs")
			if not isinstance(words, list):
				raise Exception("words")
			if not all(isinstance(elem, str) for elem in words):
				raise Exception("elem in words")
			if len(coefs) != len(words):
				raise Exception("list don't have same length")
		except Exception as e:
			print("Error :", e)
			return -1

	@staticmethod
	def zip_evaluate(coefs, words):
		if Evaluator.check_input(coefs, words) == -1:
			return -1
		return sum(i * len(elem) for i, elem in list(zip(coefs,words)))

	@staticmethod
	def enumerate_evaluate(coefs, words):
		if Evaluator.check_input(coefs, words) == -1:
			return -1
		return sum(len(words[i]) * c for i, c in enumerate(coefs))