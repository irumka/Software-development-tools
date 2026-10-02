# geometric_lib

## общее описание решения

Библиотека функций для вычисления площади и периметра базовых геометрических фигур: круга, прямоугольника, квадрата и треугольника.
```Каждая фигура вынесена в отдельный модуль.```

--- 
## описание каждой функции с примерами вызова

### [circle.py](../circle.py)

```python
import math

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r
```

#### area(r):
- вычисление площади круга

функция принимает значение радиуса типа `int` или `float` и
возвращает площадь круга типа `float` по формуле `pi * r * r`

```python
# Пример вывода
area(3) # 28.274333882308138
```

#### perimeter(r):
- вычисление длины окружности круга

функция принимает значение радиуса типа `int` или `float` и
возвращает длину окружности типа `float` по формуле `2 * pi * r`

```python
# Пример вывода
perimeter(3) # 18.84955592153876
```

---

### [rectangle.py](../rectangle.py)

```python
def area(a, b):
    return a * b

def perimeter(a, b):
    return (a + b) * 2
```

#### area(a, b):
- вычисление площади прямоугольника

функция принимает значения двух сторон типа `int` или `float` и
возвращает площадь прямоугольника типа `float` по формуле `a * b`

```python
# Пример вывода
area(3, 4) # 12
```

#### perimeter(a, b):
- вычисление периметра прямоугольника

функция принимает значения двух сторон типа `int` или `float` и
возвращает периметр прямоугольника типа `float`  по формуле `(a + b) * 2`

```python
# Пример вывода
perimeter(3, 4) # 14
```

---

### [square.py](../square.py)

```python
def area(a):
    return a * a

def perimeter(a):
    return 4 * a
```

#### area(a):
- вычисление площади квадрата

функция принимает значение стороны типа `int` или `float` и
возвращает площадь квадрата типа `float` по формуле `a * a`

```python
# Пример вывода
area(5) # 25
```

#### perimeter(a):
- вычисление периметра квадрата

функция принимает значение стороны типа `int` или `float` и
возвращает периметр квадрата типа `float` по формуле `4 * a`

```python
# Пример вывода
perimeter(5) # 20
```

---

### [triangle.py](../triangle.py)

```python
def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c
```

#### area(a, h):
- вычисление площади треугольника

функция принимает значения основания и высоты типа `int` или `float` и
возвращает площадь треугольника типа `float` по формуле `a * h / 2`

```python
# Пример вывода
area(6, 4) # 12.0
```

#### perimeter(a, b, c):
- вычисление периметра треугольника

функция принимает значения трёх сторон типа `int` или `float` и
возвращает периметр треугольника типа `float` по формуле `a + b + c`

```python
# Пример вывода
perimeter(3, 4, 5) # 12
```

---

## коммиты проекта (без последнего)
- ```438b89a``` L-05: Add user agreement
- ```6adb962``` L-03: Docs added
- ```3049431``` (origin/feature) L-04: Add rectangle.py
- ```b5b0fae``` (origin/develop) L-04: Update docs for calculate.py
- ```d76db2a``` L-04: Add calculate.py
- ```51c40eb``` L-04: Doc updated for triangle
- ```d080c78``` L-04: Triangle added
- ```d078c8d``` (HEAD -> main, origin/main, origin/HEAD) L-03: Docs added
- ```8ba9aeb``` L-03: Circle and square added

