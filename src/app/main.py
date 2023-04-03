from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from . import question_testcase
from .tester import Tester

class Submit(BaseModel):
    code: str

class SolutionResponse(BaseModel):
    passed: bool
    msg: str
    print_msg: str 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
)

@app.post("/fast/Python/{id}")
async def process_user_code(submit: Submit, id: int):
    if id not in question_testcase.info.keys():
        raise HTTPException(status_code=404, detail="Question test case not found")

    print_msg = ""
    try:
        usertest = Tester(code = submit.code, question_id = id)
        passed, print_msg, msg = usertest.exectuteTest()
    except IndentationError as e:
        passed = False
        msg = "Indentation error: \n"+str(e)
    except Exception as e:
        passed = False
        print(e)
        msg = str(e)
    print("msg to client: ", msg)
    return SolutionResponse(passed=passed, print_msg=print_msg, msg=msg)


# TODO: compile C++ 
@app.post("/fast/C++/{id}")
async def root(submit: Submit, id: int):
    pass


# TODO: compile Java
@app.post("/fast/Java/{id}")
async def root(submit: Submit, id: int):
    pass