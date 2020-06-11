from class_method import Date
class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        #返回年龄
        return 2018 - self.__birthday.year


if __name__ == "__main__":
    user = User(Date(1990,2,1))
    print(user._User__birthday) # python会给双下划线属性变形_classname__paramname
    print(user.get_age())


