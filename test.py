from payment import calculate as cal

def test(a,b):
    c = cal(a,b)

    test_c = a+b+1

    assert c == test_c


test(10,20)