#拓展题
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
ele = tuple[-1]
# ele 是什么？
print(ele)
#猜对了哈哈哈，-1对应最后一个

#学生题
class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def average(self):
        if not self.score:
            return 0
        score_values=list(self.score.values())
        return sum(score_values)/len(score_values)

Student1=Student("Jack",18,{"Math":88,"English":90})
Student2=Student("John",20,{"Math":82,"English":94})
Student3=Student("Marry",19,{"Math":87,"English":91})

avg1=Student1.average()
avg2=Student2.average()
avg3=Student3.average()
avg=(avg1+avg2+avg3)/3
print(f"{Student1.name}'s average score:{avg1:.2f}")
print(f"{Student2.name}'s average score:{avg2:.2f}")
print(f"{Student3.name}'s average score:{avg3:.2f}")
print(f"Their average score is {avg:.2f}")

#动物题
class Animal:
    def make_sound(self):
        print("某种动物在叫")

class Dog(Animal):
    def make_sound(self):
        print("汪汪汪！")

class Cat(Animal):
    def make_sound(self):
        print("喵喵喵！")

dog=Dog()
cat=Cat()
dog.make_sound()
cat.make_sound()

#多态函数
def animal_sound(animal):
    animal.make_sound()

animal_sound(Cat())
animal_sound(Dog())

