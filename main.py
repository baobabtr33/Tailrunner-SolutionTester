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
async def root(submit: Submit):
    try:
        usertest = Tester(code = submit.code, questionId = id)
        passed, msg = usertest.exectuteTest()
    except IndentationError as e:
        passed = False
        msg = "Indentation error: \n"+str(e)
    print(passed,msg)
    return SolutionResponse(passed=passed, msg=msg)