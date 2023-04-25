from typing import List
from . import question_testcase
from io import StringIO
import sys

# allow for usersolution_code to import
import collections
import heapq
import time
import itertools
from collections import *


class Tester:
    def __init__(self, solution_code, question_id):
        self.checkVulnerability(solution_code)
        self.solution_code =solution_code
        self.test_information = question_testcase.info[question_id]
        self.logic = self.test_information["logic"]

        # copy -since python pass by reference
        self.question_testcase = self.test_information["testcase"].copy() 

    def exectuteTest(self):
        # exectuesolution_code in string 
        exec(self.solution_code)
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
    

    def checkVulnerability(self,solution_code):
        check_code =solution_code.replace(' ','').replace('\n','')
        if "importos" in check_code or "fromos" in check_code:
            raise Exception('You cannot import library "os" for this platform')
        if "importsys" in check_code or "fromsys" in check_code:
            raise Exception('You cannot import library "sys" for this platform')