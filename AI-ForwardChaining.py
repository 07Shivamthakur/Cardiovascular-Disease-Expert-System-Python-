class ForwardChaining:
    def __init__(self):
        self.rulesize = 12
        self.clausevarsize = 36
        self.ClauseVarlist = [None] * self.clausevarsize
        self.kn_base = [None] * self.rulesize
        self.assign_rule_number = {}
        self.assign_clause_number = {}
        self.var_list_Ins = {}
        self.conc_var_queue = []
        self.Result = ""

        self.knowledgebase_FW()
        self.Filecopy()
        self.MapRuleNumber_kn_base()
        self.MapClauseNumber_ClauseVarList()
        self.Varlist_Instantiation()

    def knowledgebase_FW(self):
        # Define the knowledgebase contents here

    def Filecopy(self):
        # Read data from files and populate arrays

    def MapRuleNumber_kn_base(self):
        rule = 10
        for i in range(self.rulesize):
            self.assign_rule_number[rule] = self.kn_base[i]
            rule += 10

    def MapClauseNumber_ClauseVarList(self):
        Clause_no = 1
        for i in range(self.clausevarsize):
            self.assign_clause_number[Clause_no] = self.ClauseVarlist[i]
            Clause_no += 1

    def Varlist_Instantiation(self):
        self.var_list_Ins["DISEASE"] = "NI"

    def CompareStrings(self, s1, s2):
        return s1.upper() == s2.upper()

    def Treatment(self, disease):
        self.conc_var_queue.append("DISEASE")
        self.var_list_Ins["DISEASE"] = disease
        Clause_no = 1

        if disease:
            while self.conc_var_queue:
                for Clause_no, clause_var in self.assign_clause_number.items():
                    if clause_var != "s":
                        Rule_no = (((Clause_no // 3) + 1) * 10)

                compare = self.assign_rule_number[Rule_no].split("=")[1].strip()

                if self.CompareStrings(compare, disease):
                    Result = self.assign_rule_number[Rule_no].split("=")[1].strip()
                    print(Result)
                    break
                else:
                    Clause_no += 2  # moving to the position of disease

        else:
            print("Apologies..!!!! Could not specify the treatment as we are not able to detect the disease!!!!")


# Create an instance of the ForwardChaining class
forward_chaining = ForwardChaining()

# Example usage
forward_chaining.Treatment("Angina")
