from typing import List
from . import question_testcase

# allow for user code to import
import collections

class Tester:
    def __init__(self, code, questionId):
        self.checkVulnerability(code)

        # exectue code in string 
        exec(code)
        
        # get attribute name and cases
        self.testInformation = question_testcase.info[questionId]
        self.Solution = locals()['Solution']()
        self.userFunc = getattr(self.Solution, self.testInformation["attr"])
        self.questionTestcase = self.testInformation["testcase"]
        print(self.testInformation)
    
    def exectuteTest(self):
        count = 0
        for answer, case in self.questionTestcase:
            if self.userFunc(*case) == answer:
                count += 1
            else:
                return False, "Incorrect, passed {}/{} \n Incorrect Case: {}".format(count,
                                                    len(self.questionTestcase), 
                                                    case)
        return True, "Correct, passed {}/{}\n".format(count, 
                                                    len(self.questionTestcase))
    
    def checkVulnerability(self, code):
        check_code = code.replace(' ','').replace('\n','')
        if "importos" in check_code:
            raise Exception('You cannot import library "os" for this platform')
        if "importsys" in check_code:
            raise Exception('You cannot import library "sys" for this platform')