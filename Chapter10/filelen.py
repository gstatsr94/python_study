#!/usr/bin/env python

import sys                    # sys 모듈을 임포트

for fn in sys.argv[1:]:       # 스크립트의 인수를 꺼냄
    try:
        f = open(fn)
    except FileNotFoundError:
        print("{}(이)라는 파일이 존재하지 않습니다.".format(fn))
    else:
        try:
            print(fn, len(f.read())) # 파일명과 크기를 표시
        finally:
            f.close()                # 파일을 닫음
