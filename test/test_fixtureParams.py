import pytest


'''
  cross_params is a fixture in class conftest. 
  
'''

def test_fixture_with_params(cross_params):
    print(cross_params[1])