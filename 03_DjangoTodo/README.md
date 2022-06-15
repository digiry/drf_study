# Chapter3. Django로 Todo 목록 웹 서비스 만들기

Django 기본 기능에 Bootstrap CSS를 적용하여 웹 UI를 경험하는 Todo 웹 예제 입니다.

<br>

## 사전 조건

* Python 3.10.1
  * pyenv로 Python 환경을 구성
* 필수 패키지
  * `requirements.txt`로 설치

```bash
pyenv shell 3.10.1
virtualenv -p $(pyenv which python) .venv
pyenv shell --unset
source .venv/bin/activate
pip install -r requirements.txt
```
