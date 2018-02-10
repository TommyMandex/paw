from .base import paw_test


class gen_wordlist_test(paw_test):
    def test_gen_wordlist(self):
        self.paw.gensets = '[ABC][123]'
        self.paw.parse_cset()
        words1 = list(self.paw.gen_wordlist())
        self.paw.cset = {}
        self.paw.gensets = '[A][123]'
        self.paw.parse_cset()
        words2 = list(self.paw.gen_wordlist())
        self.assertEqual(words1, ['A1', 'A2', 'A3', 'B1', 'B2',
                                  'B3', 'C1', 'C2', 'C3'], "test successful")
        self.assertEqual(words2, ["A1", "A2", "A3"])

    def test_gen_wordlist_no_duplicates(self):
        self.paw.gensets = '[AA][11]'
        self.paw.parse_cset()
        no_duplicates = list(self.paw.gen_wordlist())
        self.assertEqual(no_duplicates, ["A1"])

    def test_gen_wordlist_from_file_no_duplicates(self):
        self.paw.infile = "paw/tests/test_files/gen_words_sample.txt"
        self.paw.gen_custom_charset()
        words3 = list(self.paw.gen_wordlist())
        self.assertEqual(words3, ["B1"])
