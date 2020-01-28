from person import Person
from counter import Counter
from age import Age

# クラスオブジェクトのインスタンスを生成する
print("1.インスタンスメソッドを持つクラス")
person = Person("taro")
print("name:" + person.getname())

person.setname("jiro")
print("name:" + person.getname())

print("2.クラスメソッドを持つクラス")
cnt = Counter()
print("カウンター:" + str(cnt.getcounter()))
cnt.countup()
print("カウンター:" + str(cnt.counter))
cnt2 = Counter()
print("カウンター:" + str(cnt2.getcounter()))

print("3.propertyクラス")
age = Age(10)
# print("age=" + str(age.getage()))
# print("age=" + str(age.age))