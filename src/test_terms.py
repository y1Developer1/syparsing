import unittest
from syparsing.terms import Terms
from syparsing.rule import Rule

class Test_test_1(unittest.TestCase):
    def test_A(self):
        left_term = "test"
        right_terms = ["result"]
        rule = Rule(left_term,right_terms)
        initial_terms = ["test"]
        terms = Terms(initial_terms)
        terms.applyRuleForAllTerms(rule)
        result = terms.getTerms()
        print("result : ")
        print(result)
        self.assertEqual(result[0],right_terms[0])

    def test_B(self):
        left_term = "test"
        right_terms = ["result"]
        rule = Rule(left_term,right_terms)
        initial_terms = ["test1"]
        terms = Terms(initial_terms)
        terms.applyRuleForAllTerms(rule)
        result = terms.getTerms()
        print("result : ")
        print(result)
        self.assertEqual(result[0],initial_terms[0])



if __name__ == '__main__':
    unittest.main()
