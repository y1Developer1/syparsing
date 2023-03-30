import unittest
from syparsing.rule import Rule
from syparsing.cyk import CYK

class Test_createRecognitionTable_cyk(unittest.TestCase):
    # regularity pre-test
    def test_createRecognitionTable_regular_1(self):
        terminal_term_1 = "UNIT"
        terminal_term_2 = "TEST"
        non_terminal_term_1 = "unit"
        non_terminal_term_2 = "test"
        start_term = "unittest"
        root_rule = Rule(start_term,[non_terminal_term_1,non_terminal_term_2])
        terminal_rule_1 = Rule(non_terminal_term_1,[terminal_term_1])
        terminal_rule_2 = Rule(non_terminal_term_2,[terminal_term_2])
        ruleset = {root_rule,terminal_rule_1,terminal_rule_2}
        cyk = CYK(ruleset)
        cyk.setSentence(["UNIT","TEST"])
        cyk.createRecognitionTable()
        recog_table = cyk.getRecognitionTable()
        cyk.printRecogTable()
        
if __name__ == '__main__':
    unittest.main()
