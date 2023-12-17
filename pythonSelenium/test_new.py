import pytest


@pytest.mark.usefixtures("setup")
class Test_python:
    def test_c1(self):
        print("this is first method")

    def test_c2(self):
        print("this is secound method")

    def test_c3(self):
        print("this is third method")


########### usefixture will use fixture which we are created in other testcase ####
######### (data) calling from conftest.py file data method and printing all element#####
@pytest.mark.usefixtures("data")
class Test_dtone1:
    def test_tc2(self, data):
        print(data)

######### (name) calling from conftest.py file name method and printing all element#####
@pytest.mark.usefixtures("name")
class Test_dtone2:
    def test_tc3(self, name):
        print(name)


######### fatching particular index value from list############
@pytest.mark.usefixtures("name")
class Test_Dtone3:
    def test_tc1(self, name):
        print(name[0])
