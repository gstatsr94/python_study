#!/usr/bin/env python

class StrDict(dict):
    """ 딕셔너리형을 상속해서 클래스를 만든다
    """
    def __init__(self):
        pass

    def __setitem__(self, key, value):
        """ 특수 메쏘드를 재정의(오버라이드)
            key가 문자열이 아니면 예외를 발생
        """
        if not isinstance(key, str):
            # 키가 문자열이 아닌 경우에는 예외를 발생
            raise ValueError("Key must be string.")
            # 슈퍼클래스의 특수 메쏘드를 호출해서 키와 값을 설정
        dict.__setitem__(self, key, value)
