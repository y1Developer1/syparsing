from .termsError import termsError
from .rule import Rule

class Terms:

    terms = None

    # messages for error
    non_str_input_msg = "non str input"
    non_list_input_msg = "non list input"
    non_rule_input_msg = "non rule input"

    def __init__(self,terms):
        self.setTerms(terms)

    def setTerms(self,new_terms):
        # check types of inputs
        if(not type(new_terms) is list):
            raise termsError(self.non_list_input_msg)
        for term in new_terms:
            if(not type(term) is str):
                raise termsError(self.non_str_input_msg)
        # copy inputs
        copy_new_terms = []
        for term in new_terms:
            copy_new_terms.append(term + "")
        # set copy
        self.terms = copy_new_terms

    def getTerms(self):
        # copy inputs
        copy_terms = []
        for term in self.terms:
            copy_terms.append(term + "")
        # return copy
        return copy_terms
    
    def applyRuleForATerm(self,term,rule):
        if(not type(term) is str):
            raise termsError(self.non_str_input_msg)
        if(not type(rule) is Rule):
            raise termsError(self.non_rule_input_msg)
        left_term = rule.getLeftTerm()
        if(term != left_term):
            term_list = []
            term_list.append(term + "")
            return term_list
        return rule.getTheRightTerms()

    def applyRuleForAllTerms(self,rule):
        if(not type(rule) is Rule):
            raise termsError(self.non_rule_input_msg)
        all_applied_terms = []
        for term in self.terms:
            applied_terms = self.applyRuleForATerm(term,rule)
            all_applied_terms = all_applied_terms + applied_terms
        self.terms = all_applied_terms
    