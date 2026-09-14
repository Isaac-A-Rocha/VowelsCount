import unittest
from count_utils import count_vowels

class CountVowels(unittest.TestCase):

    #Teste com uma String vazia.
    def testEmptyString(self):
        self.assertEqual(count_vowels(""), 0)
    #Teste usando um valor numérico como entrada, caso a entrada cause um TypeError, está correto.
    def testNumber(self):
        with self.assertRaises(TypeError):
            count_vowels(0)
    #Teste se não há vogais.
    def testNoVowels(self):
        self.assertEqual(count_vowels("wxyz"), 0)

    # Teste se símbolos são ignorados sem interferir na contagem das vogais.
    def testSymbols(self):
        self.assertEqual(count_vowels("a!e@i#o$u%"), 5)

    # Teste com letras maiúsculas e minúsculas.
    def testUpperAndLowerCase(self):
        self.assertEqual(count_vowels("OpenAI"), 4)

    # Teste com uma frase próxima de uma entrada real da aplicação.
    def testSentence(self):
        self.assertEqual(count_vowels("Teste e Validacao de Sistemas!"), 12)

if __name__ == '__main__':
    unittest.main()
#ou: 'python3 -m unittest unittest_vowels.py -v' no terminal para exibir cada teste separadamente.
