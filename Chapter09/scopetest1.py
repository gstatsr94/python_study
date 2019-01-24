#!/usr/bin/env python

a = 1                  # 모듈 스코프에 변수를 정의
b = 2

def foo():
    b = 10             # 지역 스코프에서 변수에 대입
    print(a, b)        # a, b라는 2가지 변수를 표시

foo()                  # 함수 foo()를 호출

print(a, b)            # a, b라는 2가지 변수를 표시
