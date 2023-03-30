import unittest
from syparsing.rule import Rule
from syparsing.cyk import CYK

class Test_hasCNFGrammer_cyk(unittest.TestCase):
    def test_hasCNFGrammer_regular_1(self):
        left_term1 = "unittest"
        right_terms1 = ["unit","test"]
        left_term2 = "unit"
        right_terms2 = ["UNIT"]
        left_term3 = "test"
        right_terms3 = ["TEST"]
        rule1 = Rule(left_term1,right_terms1)
        rule2 = Rule(left_term2,right_terms2)
        rule3 = Rule(left_term3,right_terms3)
        ruleset:set[Rule] = {rule1,rule2,rule3}
        cyk = CYK(ruleset)
        hasCNF = cyk.hasCNFGrammer()
        self.assertEqual(hasCNF,True)

    def test_hasCNFGrammer_regular_2(self):
        left_term1 = "unit"
        right_terms1 = ["UNIT"]
        left_term2 = "UNIT"
        right_terms2 = ["FAIL UNIT"]
        rule1 = Rule(left_term1,right_terms1)
        rule2 = Rule(left_term2,right_terms2)
        ruleset:set[Rule] = {rule1,rule2}
        cyk = CYK(ruleset)
        hasCNF = cyk.hasCNFGrammer()
        self.assertEqual(hasCNF,False)
    
    def test_hasCNFGrammer_regular_3(self):
        left_term1 = "fail"
        right_terms1 = ["fail unittest"]
        left_term2 = "fail unittest"
        right_terms2 = ["fail_unit","fail_test"]
        rule1 = Rule(left_term1,right_terms1)
        rule2 = Rule(left_term2,right_terms2)
        ruleset:set[Rule] = {rule1,rule2}
        cyk = CYK(ruleset)
        hasCNF = cyk.hasCNFGrammer()
        self.assertEqual(hasCNF,False)

    def test_hasCNFGrammer_regular_4(self):
        left_term = "test"
        right_terms = ["TEST"]
        rule = Rule(left_term,right_terms)
        ruleset:set[Rule] = {rule}
        cyk = CYK(ruleset)
        hasCNF = cyk.hasCNFGrammer()
        self.assertEqual(hasCNF,True)

    def test_hasCNFGrammer_regular_5(self):
        left_term = "unittest"
        right_terms = ["unit","test"]
        rule = Rule(left_term,right_terms)
        ruleset:set[Rule] = {rule}
        cyk = CYK(ruleset)
        hasCNF = cyk.hasCNFGrammer()
        self.assertEqual(hasCNF,False)
        
if __name__ == '__main__':
    unittest.main()
