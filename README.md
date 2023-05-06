# Tailrunner Code Tester
[Tailrunner 바로가기](http://tailrunner.run)

Tailrunner 프로젝트에서 유저가 보낸 알고리즘 풀이를 평가합니다.

FastAPI를 통해 백엔드를 구현하였으며, exec 함수를 통해 유저 코드를 컴파일 합니다.
현재는 Python 언어의 코드만을 실행가능합니다.

악성코드에 대비하고 Seccomp를 활욯하기 위해서 코드를 실행하기 위해 Docker를 도입하였습니다.


## ⏰ 테스트
src/test에 test 코드가 있습니다.
```
$ pytest
```
