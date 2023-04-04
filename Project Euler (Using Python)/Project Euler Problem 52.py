x=1

while True:
        _2x=2*x
        _3x=3*x
        _4x=4*x
        _5x=5*x
        _6x=6*x
        d2=str(_2x)
        d3=str(_3x)
        d4=str(_4x)
        d5=str(_5x)
        d6=str(_6x)
        set2=set(d2)
        set3=set(d3)
        set4=set(d4)
        set5=set(d5)
        set6=set(d6)
        if set2==set3 and set3==set4 and set4==set5 and set5==set6:
                print(x)
                break
        x=x+1
