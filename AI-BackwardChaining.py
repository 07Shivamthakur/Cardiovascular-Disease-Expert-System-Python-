class BackwardChaining:
    def __init__(self):
        self.DiseaseFound = False
        self.knbase = {}
        self.varibles_questions = {}
        self.varlist = []
        self.conclist = []
        self.clausevarlist = []
        self.clausevarlistValidConditions = []
        self.varlist_instan = {}
        self.clause_number = {}
        self.clause_number_valid_condition = {}
        self.rule_number = {}
        self.ruleno_concllist = {}
        self.conclusion_stack = []
        self.conclusion_stack_clause_number = []
        self.finalized_conclusions = {}
        self.finalized_conclusions2 = {}
        self.var_inc = 6
        self.varsize = 19  # Set this to the actual size
        self.concsize = 30  # Set this to the actual size
        self.clausesize = 31  # Set this to the actual size

    def knowledgebase(self):
        self.knbase[0] = "IF SYMPTOM=NO THEN DISEASE=NO"
        self.knbase[1] = "IF SYMPTOM=YES && BREATHLESSNESS=NO && FOOTSORE=YES THEN ABTEST=YES"
        # ... Add the rest of the knowledge base rules

        self.varibles_questions = {
            "SYMPTOM": "Are you experiencing any symptom(s)?",
            "BREATHLESSNESS": "Are you experiencing any breathlessness?",
            "FOOTSORE": "Are you experiencing any footsore?",
            # ... Add the rest of the questions
        }

    def filetoarray(self):
        # Read data from files and populate the respective arrays

    def assignRuleKnBase(self):
        rule = 10
        for i in range(self.concsize):
            self.rule_number[rule] = self.knbase[i]
            rule += 10

    def assignRuleConclist(self):
        rule = 10
        for i in range(self.concsize):
            self.ruleno_concllist[rule] = self.conclist[i]
            rule += 10

    def assignClauseNumber(self):
        clauseno = 1
        for i in range(self.clausesize):
            self.clause_number[clauseno] = self.clausevarlist[i]
            clauseno += 1

    def assignClauseNumber_validCondition(self):
        clauseno = 1
        for i in range(self.clausesize):
            self.clause_number_valid_condition[clauseno] = self.clausevarlistValidConditions[i]
            clauseno += 1

    def varlistInstan(self):
        for var in self.varlist:
            self.varlist_instan[var] = "NI"

    def CompareStrings(self, s1, s2):
        return s1.upper() == s2.upper()

    def questionUser(self):
        # Implement the questionUser logic here

    def DiseaseIdentification(self):
        final_conclusion_to_find = "DISEASE"
        local_conclusion_to_find = final_conclusion_to_find
        found_disease = ""

        index = 300
        for _ in range(self.concsize):
            self.rule_number_stack.append(index)
            index -= 10

        while self.rule_number_stack:
            rule_no = self.rule_number_stack.pop()
            conclusion_conc_list = self.ruleno_concllist.get(rule_no, "")
            
            if self.CompareStrings(local_conclusion_to_find, conclusion_conc_list):
                clause_no = (((rule_no // 10) - 1) * 6) + 1
                self.conclusion_stack.append(rule_no)
                self.conclusion_stack_clause_number.append(clause_no)
                result = self.questionUser()
                if final_conclusion_to_find in self.finalized_conclusions2:
                    found_disease = self.rule_number.get(rule_no, "").split("=")[-1].strip()
                    if found_disease == "NO":
                        print("\nCongrats! you don't have any Cardiovascular(Heart) disease.\n")
                    else:
                        print("===================================================================================")
                        print(f"You have been diagnosed with {found_disease}")
                        self.DiseaseFound = True
                        return found_disease
                    break

        if not found_disease:
            print("===================================================================")
            print("\tWe don't have rules specified as of now for your symptoms")
            print("===================================================================")
        
        return found_disease


# Main part of the code
def main():
    exit_program = False

    print("\t\t\t==============================================================================")
    print("\t\t\t    Welcome to Expert System for diagnosing Cardiovascular(Heart) Diseases ")
    print("\t\t\t==============================================================================\n")

    while not exit_program:
        print()
        print("\tChoose an option from the following:")
        print("\t\t1.Identification of a Cardiovascular(Heart) Disease")
        print("\t\t2.Treatment for a specific Cardiovascular(Heart
