from typing import List, Tuple
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
    """ Tester Class for testing user's code for correctness """
    
    def __init__(self, solution_code, question_id) -> None:
        self.checkVulnerability(solution_code)
        self.solution_code = solution_code
        self.test_information = question_testcase.info[question_id]
        self.classname = self.test_information["classname"]
        self.logic = self.test_information["logic"]
        self.type = self.test_information["type"]
        self.question_testcase = self.test_information["testcase"].copy() 

    def executeTest(self) -> Tuple[bool, str, str]:
        if self.type == "simple":
            return self.simpleTest()
        elif self.type == "oop":
            return self.oopTest()

    def oopTest(self) -> Tuple[bool, str, str]:
        if not self.checkFunctionExist():
            return False, "", "Incorrect, function does not exis. Do not change the name of the function\n"
        
        # get user's code system print logs
        user_print = StringIO()
        sys.stdout = user_print
    
        answer_count = 0
        for test_answer, test_case, test_funcs in self.question_testcase:
            # initialize solution_code class
            exec(self.solution_code)
            user_solution = locals()[self.classname]()

            # there are multiple functions to be called
            user_func = dict()
            for func_names in self.test_information["attr"]:
                user_func[func_names] = getattr(user_solution, func_names)

            correct = True
            num_of_funcs = len(test_funcs)

            # check class with different functions and test cases
            for idx in range(num_of_funcs):
                user_answer = user_func[test_funcs[idx]](*test_case[idx])
                if not self.logic(user_answer,test_answer[idx]):
                    correct = False
                    break
            
            if not correct:
                sys.stdout = sys.__stdout__
                return False, user_print.getvalue(), "Incorrect, passed {}/{} \n Incorrect Case: {}".format(answer_count,
                                                                                    len(self.question_testcase), 
                                                                                    test_case)
            answer_count += 1

        sys.stdout = sys.__stdout__
        return True, user_print.getvalue(), "Correct, passed {}/{}\n".format(answer_count, len(self.question_testcase))
    
    def simpleTest(self) -> Tuple[bool, str, str]:
        # exectue solution_code in string as python code
        exec(self.solution_code)
        user_solution = locals()[self.classname]()
        user_func = getattr(user_solution, self.test_information["attr"])
        
        # get user's code system print logs
        user_print = StringIO()
        sys.stdout = user_print

        answer_count = 0
        for test_answer, test_case in self.question_testcase:
            user_answer = user_func(*test_case)

            if self.logic(user_answer,test_answer):
                answer_count += 1
            else:
                sys.stdout = sys.__stdout__
                return False, user_print.getvalue(), "Incorrect, passed {}/{} \n Incorrect Case: {}".format(answer_count,
                                                                                    len(self.question_testcase), 
                                                                                    test_case)
        sys.stdout = sys.__stdout__
        return True, user_print.getvalue(), "Correct, passed {}/{}\n".format(answer_count, len(self.question_testcase))


    def checkVulnerability(self,solution_code) -> None:
        check_code =solution_code.replace(' ','').replace('\n','')
        if "importos" in check_code or "fromos" in check_code:
            raise Exception('You cannot import library "os" for this platform')
        if "importsys" in check_code or "fromsys" in check_code:
            raise Exception('You cannot import library "sys" for this platform')
    
    def checkFunctionExist(self) -> bool:
        exec(self.solution_code)
        user_solution = locals()[self.classname]()
        for funcs in self.test_information["attr"]:
            print(funcs)
            if hasattr(user_solution, funcs) and callable(getattr(user_solution, funcs)):
                pass
            else:
                return False
        return True