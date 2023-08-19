class BackwardChaining:
    def __init__(self):
        self.DiseaseFound = False
        self.varsize = 18
        self.concsize = 30
        self.clausesize = 180
        self.var_inc = 6
        self.varlist = [None] * self.varsize
        self.conclist = [None] * self.concsize
        self.clausevarlist = [None] * self.clausesize
        self.clausevarlistValidConditions = [None] * self.clausesize
        self.knbase = [None] * self.concsize
        self.str1 = ""
        self.str2 = ""
        self.disease = ""
        self.rule_number = {}
        self.clause_number = {}
        self.clause_number_valid_condition = {}
        self.varlist_instan = {}
        self.finalized_conclusions = {}
        self.ruleno_concllist = {}
        self.conclusion_stack = []
        self.conclusion_stack_clause_number = []
        self.rule_number_stack = []
        self.finalized_conclusions2 = {}
        self.true_conclusions = set()
        self.varibles_questions = {}

    def knowledgebase(self):
        # Define the knowledgebase contents here

    def filetoarray(self):
        # Read data from files and populate arrays

    def assignRuleKnBase(self):
        # Implement assignRuleKnBase

    def assignRuleConclist(self):
        # Implement assignRuleConclist

    def assignClauseNumber(self):
        # Implement assignClauseNumber

    def assignClauseNumber_validCondition(self):
        # Implement assignClauseNumber_validCondition

    def varlistInstan(self):
        # Implement varlistInstan

    def DiseaseIdentification(self):
        # Implement DiseaseIdentification

    def questionUser(self):
        # Implement questionUser

    def CompareStrings(self, s1, s2):
        return s1.upper() == s2.upper()
