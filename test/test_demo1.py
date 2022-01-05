import pytest

# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense


'''
    Is possible to execute a test by command line.
    -> py.test    will execute all tests file inside of a package according to first rule name file.
'''

''' 
    -> py.test -v   will execute with more information
    
    -> py.test -v -s   will execute with console.logs
    
    -> py.test nameoffile will execute only specified file 
    
    -> py.test -k stardard_name_of_methods -v -s  will execute only tests that have same standard. Example:
        * def test_credit_bank_user()
        * def test_credit_bank_create()
        py.test -k credit_bank -v -s 
     PS: same way you can put a mark as the example:
        @pytest.mark.smoke and execute only these marked tests by command:  py.test -m smoke -v -s  
    
    -> using @pytest.mark.skip will skip the test with this decorator
    
    -> using @pytest.mark.xfail will execute the test but will not reported (if fails: xfails, succes: xpass)
    
    -> fixture is helpful to execute a method before another one, or create objects, instances, open browser, 
        variables etc and uses another methods 
        
    -> It is possible to save tests in html file. First run pip install pytest-html 
        and execute tests with command: py.test --html=report.html -v -s 
'''




@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


#@pytest.mark.skip
def test_credit_bank_user():
    print("test only key name test")


def test_credit_bank_create():
    print("test only with key name test")


@pytest.mark.xfail
def test_credit_bank_create():
    a = 3
    b = 7
    assert a + b == 10, f"Will not be reported because xfail decorator"



