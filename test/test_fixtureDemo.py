import pytest


''' It´s possible declare a fixture in level class. So it is not necessary to declare fixture in each method.
   for it method will call the fixture. 
   
   -> For execution before a class (once and not for each method) it is necessary to put a scope on fixture.   '''

@pytest.mark.usefixtures("setup_class_scope")
class TestExample:

    def test_fixtureDemo(self):
        print("-->>> I will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("-->>> I will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("-->>> I will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("-->>> I will execute steps in fixtureDemo3 method")


