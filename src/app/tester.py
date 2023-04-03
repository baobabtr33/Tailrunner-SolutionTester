from typing import List
from . import question_testcase
from io import StringIO
import sys

# allow for user code to import
import collections
import heapq
import time
from collections import *


class Tester:
    def __init__(self, code, question_id):
        self.checkVulnerability(code)
        self.code = code
        self.test_information = question_testcase.info[question_id]
        self.logic = self.test_information["logic"]
        
        # copy -since python pass by reference
        self.question_testcase = self.test_information["testcase"].copy() 

    def exectuteTest(self):
        # exectue code in string 
        exec(self.code)
        user_solution = locals()['Solution']()
        user_func = getattr(user_solution, self.test_information["attr"])
        
        user_print = StringIO()
        sys.stdout = user_print

        count = 0
        for test_answer, test_case in self.question_testcase:
            user_answer = user_func(*test_case)

            if self.logic(user_answer,test_answer):
                count += 1
            else:
                sys.stdout = sys.__stdout__
                return False, user_print.getvalue(), "Incorrect, passed {}/{} \n Incorrect Case: {}".format(count,
                                                                                    len(self.question_testcase), 
                                                                                    test_case)
        sys.stdout = sys.__stdout__
        return True, user_print.getvalue(), "Correct, passed {}/{}\n".format(count, 
                                                    len(self.question_testcase))
    

    def checkVulnerability(self, code):
        check_code = code.replace(' ','').replace('\n','')
        if "importos" in check_code:
            raise Exception('You cannot import library "os" for this platform')
        if "importsys" in check_code:
            raise Exception('You cannot import library "sys" for this platform')