from .ruleError import ruleError
class Rule:
    
    '''
    left_term -> right_term1 right_term2 ...
    '''

    # l.h.s. term
    l:str = None
    # r.h.s. terms 
    r:list[str] = None

    # messages for error
    non_str_input_msg = "non str input"
    non_list_input_msg = "non list input"
    non_rule_input_msg = "non rule input"
    null_output_msg = "null output"

    def __init__(self,left_term:str,right_terms:list[str])->None:
        self.setLeftTerm(left_term)
        self.setRightTerms(right_terms)
        

    def getLeftTerm(self)->str:
        return self.l + ""
    
    def getTheRightTerms(self)->list[str]:
        copy_right_terms = []
        for term in self.r:
            copy_right_terms.append(term + "")
        return copy_right_terms
        

    def setLeftTerm(self,new_left_term:str)->str:
        # check types of inputs
        if(not type(new_left_term) is str):
            raise ruleError(self.non_str_input_msg)
        # set the copies
        self.l = new_left_term + ""

    def setRightTerms(self,new_right_terms:list[str])->None:
        # check types of inputs
        if(not type(new_right_terms) is list):
            raise ruleError(self.non_list_input_msg)
        for term in new_right_terms:
            if(not type(term) is str):
                raise ruleError(self.non_str_input_msg)
        # copy the inputs
        copy_new_right_terms = []
        for term in new_right_terms:
            copy_new_right_terms.append(term + "")
        # set the copies
        self.r = copy_new_right_terms
    
    def equals(self,another_rule)->bool:
        if(not type(another_rule) is Rule):
            raise ruleError(self.non_rule_input_msg)
        another_left_term = another_rule.getLeftTerm()
        another_right_terms = another_rule.getTheRightTerms()
        if(self.l != another_left_term):
            return False
        if(self.r != another_right_terms):
            return False
        return True

    def clone(self):
        left_term = self.getLeftTerm()
        right_terms = self.getTheRightTerms()
        clone = Rule(left_term,right_terms)
        return clone