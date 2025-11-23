#Задача 3. Беспилотный автомобиль

"""Это творческая задача. Представьте, что вы проектируете беспилотный автомобиль. 
Вам необходимо продумать, какими свойствами он обладает и какие действия совершает. 
Создайте класс беспилотный автомобиль и сохраните его в виде программного модуля. 
Импортируете класс и инициализируйте новый объект."""

%%writefile cars.py

class AutonomousCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery_level = 100                         #Уровень заряда (%)
        self.location = (0, 0)                           #Текущие координаты
        self.sensors = ['lidar', 'radar', 'camera']      #Сенсоры
        self.obstacle_detected = False                   #Наличие препятствия
        self.route_plan = []                             #Маршрут
        self.energy_consumption_rate = 1.0               #Расход энергии (%)
        self.traffic_adaptability = 'normal'             #Поведение в трафике
        self.diagnostics_status = 'OK'                   #Статус диагностики

    def drive_to(self, destination):
        self.route_plan = [destination]
        print(f"{self.brand} {self.model} едет к {destination}.")
        self.battery_level -= self.energy_consumption_rate * 5
        self.detect_obstacles()

    def detect_obstacles(self):
        self.obstacle_detected = False
        print("Проверка на препятствия: всё чисто.")

    def charge(self):
        self.battery_level = 100
        print(f"{self.brand} {self.model} полностью заряжен.")

    def show_status(self):
        print(f"""
{self.brand} {self.model} — СТАТУС:
Заряд батареи: {self.battery_level}%
Координаты: {self.location}
Сенсоры: {', '.join(self.sensors)}
Препятствия: {'обнаружены' if self.obstacle_detected else 'нет'}
Маршрут: {self.route_plan}
Расход энергии: {self.energy_consumption_rate}
Поведение в трафике: {self.traffic_adaptability}
Диагностика: {self.diagnostics_status}
""")
