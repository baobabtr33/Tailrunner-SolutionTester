class Tester:
    def __init__(self, code, questionId):
        exec(code)
        self.Solution = locals()['Solution']
        self.questionTestcase = {
            5: [3,2],
            4: [2,2],
            0: [0,0]
        }
    
    def exectuteTest(self):
        count = 0
        for answer, case in self.questionTestcase.items():
            if self.Solution.submitSolution(case) == answer:
                count += 1
            else:
                return False, "Incorrect, passed {}/{}\n Case: {}".format(count,
                                                    len(self.questionTestcase), 
                                                    case)
        return True, "Correct, passed {}/{}\n".format(count, 
                                                    len(self.questionTestcase))