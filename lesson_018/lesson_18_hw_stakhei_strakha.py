'''
Класс Tomato:
1. Создайте класс Tomato
2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
3. Создайте метод __init__(), внутри которого будут определены два динамических protected свойства: 1)
_index - передается параметром и 2) _state - принимает первое значение из словаря states
4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
Класс TomatoBush
1. Создайте класс TomatoBush
2. Рапределите метод __init__(), который будет принимать в качестве параметра количество томатов и на его
основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри
динамического свойства tomatoes.
3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап
созревания
4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
Класс Gardener
1. Создайте класс Gardener
2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name -
передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является
protected
3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться
более зрелым
4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
Если нет - метод печатает предупреждение.
5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.

'''
class Tomato:
    states = {0: 'stad_start', 1: 'stad_1', 2: 'stad_2', 3: 'stad_final'}

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    # def grow(self):
    #    x = self.states.index(self._state)
    #    self._state = self.states[x+1]
    def grow(self):
        for k in iter(self.states.keys()):
            if self._state == self.states[k] and self._state != self.states[3]:
                self._state = self.states[k + 1]
                break

    def is_ripe(self):
        if self._state == self.states[3]:
            return True
        else:
            return False

    def status(self):
        return self._state
'''
Класс TomatoBush
1. Создайте класс TomatoBush
2. Рапределите метод __init__(), который будет принимать в качестве параметра количество томатов и на его 
основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри 
динамического свойства tomatoes.
3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап 
созревания
4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая 
'''
class TomatoBush:

    def __init__(self, count_tom):
        self.lst_tom = [Tomato(i) for i in range(count_tom)]

    def grow_all(self):
        for tomato_1 in range(len(self.lst_tom)):
            self.lst_tom[tomato_1].grow()

    def all_are_ripe(self):
        count_check = len(self.lst_tom)
        for tomato_1 in range(len(self.lst_tom)):
            if self.lst_tom[tomato_1].is_ripe():
                count_check -= 1
        if count_check == 0:
            return True
        else:
            return False

    def give_away_all(self):
        self.lst_tom.clear()


'''
Класс Gardener
1. Создайте класс Gardener
2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name - 
передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является 
protected
3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться 
более зрелым
4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай. 
Если нет - метод печатает предупреждение.
5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству. 
'''
class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран')
        else:
            print('томаты не созрели, собирать рано!!!')

    def knowledge_base(self):
        print('справка по садоводству.')



