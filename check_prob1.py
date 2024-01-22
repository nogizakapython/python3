class Student():
    def __init__(self,name,test_score):
        self.__name = name
        self.__test_score = test_score

    #name属性のゲッター
    @property
    def name(self):
        return self.__name

    #test_score属性のゲッター
    @property
    def test_score(self):
        return self.__test_score

    #test_score属性のセッター
    @test_score.setter
    def test_score(self,value):
        if type(value) is not int:
            raise TypeError("test_score must be int")
        self.__test_score = value


Student1 = Student("Taro",50)
print(Student1.name)
