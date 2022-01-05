import pytest

'''
    The fixture here is called by specific method.  
'''

@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self, dataLoad):
        print(dataLoad)
        print(dataLoad[0])



