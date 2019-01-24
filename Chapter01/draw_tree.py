#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *   # turtle 기능을 읽어 들임

def tree(length):
    # 나무를 그리는 함수
    if length > 5:
        forward(length)
        right(20)
        tree(length-15)
        left(40)
        tree(length-15)
        right(20)
        backward(length)

color("green")   # 커서의 색상을 녹색으로 만든다
left(90)         # 왼쪽으로 90도 회전시켜 위를 향하게 한다
backward(150)    # 아래쪽으로 내리기
tree(120)        # 나무를 그리는 함수 호출

input('type to exit')  # 그리기 종료 후 입력 대기
