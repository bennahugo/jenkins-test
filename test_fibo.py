from nose.tools import *
import fibonacci 

def test_recursive_base():
	assert fibonacci.fibo(1) == 1
def test_recursive_el_2():
	assert fibonacci.fibo(2) == 1
def test_recursive_el_3():
	assert fibonacci.fibo(3) == 2
def test_recursive_el_4():
	assert fibonacci.fibo(4) == 3
def test_recursive_el_5():
	assert fibonacci.fibo(5) == 5
def test_recursive_el_10():
	assert fibonacci.fibo(10) == 55
def test_fail():
	assert false, "fall on your ass"
@raises(ValueError)
def test_value_error():
	fibonacci.fibo(-1)
