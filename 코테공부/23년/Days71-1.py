from math import gcd
def solution(w,h):

    w, h = max(w,h), min(w, h) # Width가 더 길게 설정 

    g = gcd(w,h) # 최대 공약수 -> 자를 때 패턴 반복수

    ww = w // g # 패턴마다 반복되는 사각형의 Width 
    hh = h // g # 패턴마다 반복되는 사각형의 Height

    # (ww* hh) > 패턴반복되는 사각형 수 
    # (ww - 1) * (hh - 1) > 패턴별 잘리는 사각형 수 
    cut = ( (ww * hh) - (ww - 1) * (hh - 1) )

    return w * h - cut * g