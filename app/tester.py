from typing import List
from . import question_testcase

# allow for user code to import
import collections
import heapq
import time
from collections import *

class Tester:
    def __init__(self, code, question_id):
        self.checkVulnerability(code, question_id)
        self.code = code
        self.test_information = question_testcase.info[question_id]
        self.question_testcase = self.test_information["testcase"].copy() # copy -since python pass by reference
    
    def exectuteTest(self):
        # exectue code in string 
        exec(self.code)
        user_solution = locals()['Solution']()
        user_func = getattr(user_solution, self.test_information["attr"])
        
        count = 0
        for answer, case in self.question_testcase:
            if user_func(*case) == answer:
                count += 1
            else:
                return False, "Incorrect, passed {}/{} \n Incorrect Case: {}".format(count,
                                                    len(self.question_testcase), 
                                                    case)
        return True, "Correct, passed {}/{}\n".format(count, 
                                                    len(self.question_testcase))
    

    def checkVulnerability(self, code, question_id):
        check_code = code.replace(' ','').replace('\n','')
        if "importos" in check_code:
            raise Exception('You cannot import library "os" for this platform')
        if "importsys" in check_code:
            raise Exception('You cannot import library "sys" for this platform')
        if question_id not in question_testcase.info.keys():
            raise Exception('Test Environment not ready for Question',question_id)