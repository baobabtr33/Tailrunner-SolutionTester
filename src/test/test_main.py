from fastapi.testclient import TestClient
from .answer import answer
from app.main import app

client = TestClient(app)

def test_process_user_code():
    response = client.post("/fast/Python/1", json={"code": answer[1]})
    assert response.status_code == 200
    assert response.json() == {"passed": True, "print_msg": "", "msg": "Correct, passed 5/5\n"}

def test_process_user_code_indentation_error():
    response = client.post("/fast/Python/1", json={"code": "class Solution:\n    def listSum(self, lst: List[int]) -> int:"})
    assert response.status_code == 200
    assert response.json() == {"passed": False, "print_msg": "", "msg": "Indentation error: \nexpected an indented block (<string>, line 2)"}

def test_process_user_code_unavailable_testcase():
    response = client.post("/fast/Python/0", json={"code": ""})
    assert response.status_code == 404
    assert response.json() ==  {'detail': 'Question test case not found'}

def test_process_user_code_limit_os_import():
    response = client.post("/fast/Python/1", json={"code": "import os"})
    assert response.status_code == 200
    assert response.json() ==  {'passed': False, 'msg': 'You cannot import library "os" for this platform', 'print_msg': ''}

def test_process_user_code_limit_sys_import():
    response = client.post("/fast/Python/1", json={"code": "import sys"})
    assert response.status_code == 200
    assert response.json() ==  {'passed': False, 'msg': 'You cannot import library "sys" for this platform', 'print_msg': ''}

def test_check_valid_testcase():
    for (id, code) in answer.items():
        response = client.post("/fast/Python/"+str(id), json={"code": code})
        assert response.status_code == 200
        assert response.json().get("passed") ==  True
