from .cykError import cykError
from .rule import Rule
from .ruleError import ruleError
class CYK:

    gram:set[Rule] = set()
    recog_table:list[list[list[Rule]]] = [[[]]]
    sentence : list[str] = []
    one_right_gram:set[Rule] = set()
    two_right_gram:set[Rule] = set()

    null_input_msg = "null inputs"
    null_output_msg = "null outputs"
    non_set_input_msg = "non set inputs"
    non_rule_input_msg = "non rule inputs"
    process_does_not_complete_msg = "process does not complete"
    non_positive_int_input_msg = "non positive int inputs"
    empty_set_input_msg = "empty set inputs"
    empty_set_output_msg = "empty set outputs"

    def refreshAllMembers(self):
        self.gram:set[Rule] = set()
        self.recog_table:list[list[list[Rule]]] = [[[]]]
        self.sentence : list[str] = []
        self.one_right_gram:set[Rule] = set()
        self.two_right_gram:set[Rule] = set()

    def __init__(self,grammer:set[Rule])->None:
        self.refreshAllMembers()
        if(grammer == None):
            raise cykError(self.null_input_msg)
        if(not type(grammer) is set):
            raise cykError(self.non_set_input_msg)
        for each_rule in grammer:
            if(not type(each_rule) is Rule):
                raise cykError(self.non_rule_input_msg)
        copy:set[Rule] = set()
        for each_rule in grammer:
            each_clone = each_rule.clone()
            copy.add(each_clone)
        self.gram = copy

    def hasCNFGrammer(self)->bool:
        # each rule must have r.h.s. terms consist of one term or two terms
        for each_rule in self.gram:
            each_right_terms:list[str] = each_rule.getTheRightTerms()
            if(each_right_terms == None): return None
            if(len(each_right_terms) != 1 and len(each_right_terms) != 2):
                return False
        # separate rules as two sets of one r.h.s.term rules and two r.h.s.term rules resp.
        for each_rule in self.gram:
            each_right_terms:list[str] = each_rule.getTheRightTerms()
            if(each_right_terms == None): return None
            if(len(each_right_terms) == 1):
                each_clone = each_rule.clone()
                self.one_right_gram.add(each_clone)
                continue
            if(len(each_right_terms) == 2):
                each_clone = each_rule.clone()
                self.two_right_gram.add(each_clone)
                continue
        # for one r.h.s.term it must be a terminal
        for each_one_right_rule in self.one_right_gram:
            each_one_rights:list[str] = each_one_right_rule.getTheRightTerms()
            if(each_one_rights == None): return None
            each_one_right:str = each_one_rights[0]
            if(each_one_right == None): return None
            # search two r.h.s terms for match
            for each_two_right_rule in self.two_right_gram:
                each_two_left:str = each_two_right_rule.getLeftTerm()
                if(each_two_left == None): return None
                if(each_one_right == each_two_left):
                    return False
            # seach one r.h.s. terms for match
            for each_one_right_rule in self.one_right_gram:
                each_one_left:str = each_one_right_rule.getLeftTerm()
                if(each_one_left == None): return None
                if(each_one_right == each_one_left):
                    return False
        # for two r.h.s.term these must be non-terminals
        for each_two_right_rule in self.two_right_gram:
            each_two_right:list[str] = each_two_right_rule.getTheRightTerms()
            if(each_two_right == None): return None
            each_two_right_one_side:str = each_two_right[0]
            if(each_two_right_one_side == None): return None
            each_two_right_another_side:str = each_two_right[1]
            if(each_two_right_another_side == None): return None
            non_terminal_flag:bool = False
            # search one r.h.s. terms for match 
            for each_one_right_rule in self.one_right_gram:
                each_one_right:str = each_one_right_rule.getLeftTerm()
                if(each_two_right_one_side == each_one_right or each_two_right_another_side == each_one_right):
                    non_terminal_flag = True
                    break
            # search two r.h.s. terms for match
            if(not non_terminal_flag):
                for each_two_right_rule2 in self.two_right_gram:
                    each_two_right2:str = each_two_right_rule2.getLeftTerm()
                    if(each_two_right_one_side == each_two_right2 or each_two_right_another_side == each_two_right2):
                        non_terminal_flag = True
                        break
            if(not non_terminal_flag):
                return False
        return True

    def generateInitRecogTable(self,length:int)->list[list[list[Rule]]]:
        if(not type(length) is int): return None
        if(length < 1): return None
        init_table:list[list[list[Rule]]] = []
        for i in range(0,length):
            init_table.append([])
            for j in range(0,length-i):
                init_table[i].append([])
        return init_table

    
    def initRecognTable(self):
        if(self.sentence == None): cykError(self.process_does_not_complete_msg)
        l = len(self.sentence)
        self.recog_table = self.generateInitRecogTable(l)


    def setSentence(self,sentence:list[str])->None:
        if(sentence == None):
            raise cykError(self.null_input_msg)
        copy:list[str] = []
        for each_str in sentence:
            each_clone = each_str + ""
            copy.append(each_clone)
        self.sentence = copy
    
    def addRuleToRecogTable(self,row:int,column:int,rule:Rule)->None:
        # validate inputs
        if(rule == None):
            raise cykError(self.null_input_msg)
        if(row < 1 or column < 1):
            raise cykError(self.non_positive_int_input_msg)
        copy = rule.clone()
        if(copy == None): raise ruleError(rule.null_output_msg)
        self.recog_table[row-1][column-1].append(copy)

    def addRulesToRecogTable(self,row:int,column:int,rules:set[Rule])->None:
        # validate inputs
        if(rules == None):
            raise cykError(self.null_input_msg)
        if(len(rules) == 0):
            raise cykError(self.empty_set_input_msg)
        for each_rule in rules:
            if(each_rule == None): raise cykError(self.null_input_msg)
        if(row < 1 or column < 1):
            raise cykError(self.non_positive_int_input_msg)
        for each_rule in rules:
            self.addRuleToRecogTable(row,column,each_rule)
    
    def getRulesFromRecogTableAt(self,row:int,column:int)->set[Rule]:
        # validate inputs
        if(row == None or column == None): return None
        if(row < 1 or column < 1):
            return None
        rules:set[Rule] = self.recog_table[row-1][column-1]
        if(rules == None):
            return None
        if(len(rules) == 0):
            empty_set:set[Rule] = set()
            return empty_set
        # copy the rules
        copy:set[Rule] = set()
        for each_rule in rules:
            each_clone = each_rule.clone()
            if(each_clone == None): return None
            copy.add(each_clone)
        return copy
    
    def getRulesFromRecogTableAts(self,coordinates:set[tuple[int]])->set[Rule]:
        # validate inputs
        if(coordinates == None): return None
        if(len(coordinates) == 0): return set()
        for coordiante in coordinates:
            if(len(coordiante) != 2): return None
            if(coordiante[0] == None or coordiante[1] == None): return None
            if(coordiante[0] < 1 or coordiante[1] < 1): return None
        # get rules
        all_rules = set()
        for coodinate in coordinates:
            rules = self.getRulesFromRecogTableAt(coodinate[0],coodinate[1])
            for each_rule in rules:
                all_rules.add(each_rule)
        return all_rules

    def findTheTwoRHSRulesWithRHSLeftSide(self,left_side_str:str)->set[Rule]:
        # validate inputs
        if(left_side_str == None):
            return None
        # find rule
        if(self.two_right_gram == None): return None
        match_rules:set[Rule] = set()
        for each_rule in self.two_right_gram:
            right_hand_side = each_rule.getTheRightTerms()
            if(right_hand_side == None): return None
            left_side = right_hand_side[0]
            if(left_side == None): return None
            if(left_side == left_side_str):
                each_clone = each_rule.clone()
                if(each_clone == None): return None
                match_rules.add(each_clone)
        return match_rules
    
    def findTheTwoRHSRulesWithRHSRightSide(self,right_side_str:str)->set[Rule]:
        # validate inputs
        if(right_side_str == None):
            return None
        # find rule
        if(self.two_right_gram == None): return None
        match_rules:set[Rule] = set()
        for each_rule in self.two_right_gram:
            right_hand_side = each_rule.getTheRightTerms()
            if(right_hand_side == None): return None
            right_side = right_hand_side[1]
            if(right_side == None): return None
            if(right_side == right_side_str):
                each_clone = each_rule.clone()
                if(each_clone == None): return None
                match_rules.add(each_clone)
        return match_rules
    
    def findTheTwoRHSRulesWithRHS(self,left_side_str,right_side_str)->set[Rule]:
        # validate inputs
        if(left_side_str == None or right_side_str == None):
            return None
        if(len(left_side_str) == 0 or len(right_side_str) == 0):
            return None
        rules_left_side_str = self.findTheTwoRHSRulesWithRHSLeftSide(left_side_str)
        if(rules_left_side_str == None): return None
        rules_right_side_str = self.findTheTwoRHSRulesWithRHSRightSide(right_side_str)
        if(rules_right_side_str == None): return None
        # take the intersection of sets of rules gotten from the left and the right
        rules = set()
        for each_left_rule in rules_left_side_str:
            for each_right_rule in rules_right_side_str:
                if(each_left_rule.equals(each_right_rule)):
                    clone_rule = each_left_rule.clone()
                    rules.add(clone_rule)
        return rules        
    
    def findTheOneRHSRulesWithRHS(self,str:str)->set[Rule]:
        # validate
        if(str == None):
            return None
        # find rule
        if(self.one_right_gram == None): return None
        match_rules:set[Rule] = set()
        for each_rule in self.one_right_gram:
            right_hand_side = each_rule.getTheRightTerms()
            if(right_hand_side == None): return None
            right_term = right_hand_side[0]
            if(right_term == None): return None
            if(right_term == str):
                each_clone = each_rule.clone()
                if(each_clone == None): return None
                match_rules.add(each_clone)
        return match_rules
    
    def findTheTwoRHSRulesFollowedBy(self,left_rules:set[Rule],right_rules:set[Rule])->set[Rule]:
        if(left_rules == None or right_rules == None): return None
        rules = set()
        for each_left_rule in left_rules:
            for each_right_rule in right_rules:
                each_left_LHS = each_left_rule.getLeftTerm()
                if(each_left_LHS == None): return None
                each_right_LHS = each_right_rule.getLeftTerm()
                if(each_right_LHS == None): return None
                each_rules = self.findTheTwoRHSRulesWithRHS(each_left_LHS,each_right_LHS)
                if(each_rules == None): return None
                for each_rule in each_rules:
                    rules.add(each_rule)
        return rules

    def calCoordinatesToRegardForLeft(self,row_no:int,column_no:int)->set[tuple[int]]:
        if(row_no == None or column_no == None): return None
        if(row_no < 1 or column_no < 1): return None
        coordinates:set[tuple[int]] = set()
        for i in range(1,row_no):
            coordinate = (i,column_no+0)
            coordinates.add(coordinate)
        return coordinates
    
    def calCoordinatesToRegardForRight(self,row_no:int,column_no:int)->set[tuple[int]]:
        if(row_no == None or column_no == None): return None
        if(row_no < 1 or column_no < 1): return None
        coordinates:set[tuple[int]] = set()
        for i in range(1,row_no):
            coordinate = (i,column_no+row_no-i)
            coordinates.add(coordinate)
        return coordinates

    def createRecognitionTable(self)-> None:
        # validate grammer
        has_cnf:bool = self.hasCNFGrammer()
        if(has_cnf == None): raise cykError(self.null_output_msg)
        if(has_cnf == False): raise cykError(self.process_does_not_complete_msg)
        # initialize the recognition table with given sentence
        self.initRecognTable()
        # fill the terminal row in the recognition table
        l = len(self.sentence)
        for j in range(l):
            each_str = self.sentence[j]
            if(each_str == None): raise cykError(self.null_output_msg)
            each_column_no = j + 1
            match_rules = self.findTheOneRHSRulesWithRHS(each_str)
            if(match_rules == None): raise cykError(self.null_output_msg)
            self.addRulesToRecogTable(1,each_column_no,match_rules)
        # fill the non-terminal rows in the recognition table
        for i in range(l-1):
            each_row_no = i + 2
            for j in range(0,l-each_row_no+1):
                each_column_no = j + 1
                # calculate coordinates along the triangle topped by (each_row_no,each_column_no)
                coordinates_4_left = self.calCoordinatesToRegardForLeft(each_row_no,each_column_no)
                if(coordinates_4_left == None): raise cykError(self.null_output_msg)
                if(len(coordinates_4_left) == 0): raise cykError(self.empty_set_output_msg)
                coordinates_4_right = self.calCoordinatesToRegardForRight(each_row_no,each_column_no)
                if(coordinates_4_right == None): raise cykError(self.null_output_msg)
                if(len(coordinates_4_right) == 0): raise cykError(self.empty_set_output_msg)
                # get rules from recognition table (with already gotten rules)
                rules_4_left = self.getRulesFromRecogTableAts(coordinates_4_left)
                if(rules_4_left == None): raise cykError(self.null_output_msg)
                if(len(rules_4_left) == 0): continue
                rules_4_right = self.getRulesFromRecogTableAts(coordinates_4_right)
                if(rules_4_right == None): raise cykError(self.null_output_msg)
                if(len(rules_4_right) == 0): continue
                # find the rules followed by the rules along the triangle
                rules_required = self.findTheTwoRHSRulesFollowedBy(rules_4_left,rules_4_right)
                if(rules_required == None): return None
                # add the rules to recognition table
                self.addRulesToRecogTable(each_row_no,each_column_no,rules_required)

    def getRecognitionTable(self)->list[list[list[Rule]]]:
        if(self.sentence == None): return None
        l = len(self.sentence)
        copy_table = self.generateInitRecogTable(l)
        for row_no in range(len(self.recog_table)):
            each_row = self.recog_table[row_no]
            if(each_row == None): return None
            for column_no in range(len(each_row)):
                each_rules = each_row[column_no]
                for each_rule in each_rules:
                    clone = each_rule.clone()
                    copy_table[row_no][column_no].append(clone)
        return copy_table
    
    def printRecogTable(self):
        l = len(self.recog_table)
        for i in range(0,l):
            each_row = self.recog_table[l-i-1]
            print_str = ""
            for j in range(0,len(each_row)):
                each_rules = each_row[j]
                for each_rule in each_rules:
                    left_term = each_rule.getLeftTerm()
                    right_terms = each_rule.getTheRightTerms()
                    print_str += left_term + " -> ["
                    first_term = right_terms[0]
                    print_str += first_term
                    for k in range(len(right_terms)):
                        if(k == 0): continue
                        print_str += "," + right_terms[k]
                    print_str += " ]"
                print_str += " | "
            print(print_str)