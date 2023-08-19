class BackwardChaining:
    def __init__(self):
        self.DiseaseFound = False
    
    def DiseaseIdentification(self):
        # Implement the DiseaseIdentification logic here
        # Return the identified disease

class ForwardChaining:
    def Treatment(self, disease):
        # Implement the Treatment logic here

exit_program = False

print("\t\t\t==============================================================================")
print("\t\t\t    Welcome to Expert System for diagnosing Cardiovascular(Heart) Diseases ")
print("\t\t\t==============================================================================\n")

while not exit_program:
    print()
    print("\tChoose an option from the following:")
    print("\t\t1.Identification of a Cardiovascular(Heart) Disease")
    print("\t\t2.Treatment for a specific Cardiovascular(Heart) Disease")
    print("\t\t3.To exit")
    choice = int(input())
    
    bw = BackwardChaining()
    fw = ForwardChaining()
    
    if choice == 1:
        print("\t=================================================================================\n")
        print("\t\tEntering the Heart Disease Identification System")
        print("\t\tInitiating the KnowledgeBase")
        print("\t\tPlease enter YES/NO for the following symptoms unless specified.")
        print("\t=================================================================================\n")
        disease = bw.DiseaseIdentification()
        
        if bw.DiseaseFound:
            print("===================================================================================\n")
            response = input(f"Do you want to proceed to treatment for the identified \"{disease}\" (YES/NO):\n").upper()
            if response == "YES":
                print("==================================================================================\n")
                print(f"Treatment for \"{disease}\" is")
                fw.Treatment(disease)
            print()
            print()
            print("Exiting Disease Identification System.")
    
    elif choice == 2:
        disease = input("Enter the Disease name:\n").upper()
        print(f"Treatment for \"{disease}\" is")
        fw.Treatment(disease)
    
    elif choice == 3:
        exit_program = True
        print("\t\tBYE BYE :)")
    
    else:
        print("Please enter a valid choice")
