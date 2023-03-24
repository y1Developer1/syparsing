from .ruleError import ruleError
class Rule:
    
    '''
    left_term -> right_term1 right_term2 ...
    '''

    # l.h.s. term
    l = None
    # r.h.s. terms 
    r = None

    # messages for error
    non_str_input_msg = "non str input"
    non_list_input_msg = "non list input"

    def __init__(self,left_term,right_terms):
        self.setLeftTerm(left_term)
        self.setRightTerms(right_terms)
        

    def getLeftTerm(self):
        return self.l + ""
    
    def getTheRightTerms(self):
        copy_right_terms = []
        for term in self.r:
            copy_right_terms.append(term + "")
        return copy_right_terms
        

    def setLeftTerm(self,new_left_term):
        # check types of inputs
        if(not type(new_left_term) is str):
            raise ruleError(self.non_str_input_msg)
        # set the copies
        self.l = new_left_term + ""

    def setRightTerms(self,new_right_terms):
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