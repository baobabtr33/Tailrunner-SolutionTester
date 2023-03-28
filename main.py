from fastapi import FastAPI
from pydantic import BaseModel
from tester import Tester

class Submit(BaseModel):
    code: str

class SolutionResponse(BaseModel):
    passed: bool
    msg: str

app = FastAPI()

@app.post("/Python/{id}")
async def root(submit: Submit, id: int):
    try:
        usertest = Tester(code = submit.code, questionId = id)
        passed, msg = usertest.exectuteTest()
    except IndentationError as e:
        passed = False
        msg = "Indentation error: \n"+str(e)
    except Exception as e:
        passed = False
        msg = str(e)
    print(msg)
    return SolutionResponse(passed=passed, msg=msg)

# TODO: compile C++ 
@app.post("/C++/{id}")
async def root(submit: Submit, id: int):
    pass

# TODO: compile Java
@app.post("/Java/{id}")
async def root(submit: Submit, id: int):
    pass