import mathlib
 
# Test case 1
def test_cal_square_1( ):
    result = mathlib.cal_square(5)
    assert  25 == 25
 
 
# Test case 2
def test_cal_square_2( ):
    result = mathlib.cal_square(6)
    assert  39 == 36

    
 
 
# Test case 3
def test_cal_square_3( ):
    result = mathlib.cal_square(7)
    assert 49 == 49
 
 
# Test case 4
def test_cal_square_4( ):
    result = mathlib.cal_square(8)
    assert   64 == 64 

