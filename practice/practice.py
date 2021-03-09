from random import *

class Unit : 
    def __init__(self,name,hp,speed) : 
        self.name = name
        self.hp = hp
        self.speed = speed 
        print(f"{name} 유닛이 생성되었습니다.")
    def move(self,location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다 [속도 : {self.speed}]")
    def damaged(self,damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다. ")
        if self.hp<= 0 :
            print(f"{self.name} : 파괴되었습니다.")

class AttackUnit(Unit) : 
    def __init__(self,name,hp,speed, damage) : 
        Unit.__init__(self,name,hp,speed)
        self.damage= damage
    def attack(self,location) :
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}] ")

#마린
class Marin(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
    
    def stimpact(self):
        if self.hp >10 :
            self.hp -=10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else :
            print(f"{self.name} : 채력이 부족하여 스팀팩을 사용하지 않습니다.")

#탱크
class Tank(AttackUnit):
    seize_developed=False 
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode= False 
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return 
        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage*=2
            self.seize_mode = True
        else : 
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.damage/=2
            self.seize_mode = False 

#레이스

class Flyable : 
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    def fly(self,name,location) :
        print(f"{name} : {location} 방향으로 날아갑니다.[속도 {self.flying_speed}]")

class flyableAttack(AttackUnit, Flyable):
    def __init__(self,name,hp,damage,flying_speed) :
        AttackUnit.__init__(self, name,hp,0,damage)
        Flyable.__init__(self,flying_speed)

    def move(self,location):
        print("[공중유닛이동]")
        self.fly(self.name, location)

class Wraith(flyableAttack):
    def __init__(self):
        flyableAttack.__init__(self,"레이스",80,20,5)

    def clocking(self):
        if self.clocked==True:
            print(f"{self.name} : 클로킹 모드 해제합니다.")
            self.clocked == False
        else :
            print(f"{self.name} : 클로킹 모드를 합니다")
            self.clocked == True 

def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    print("player : GG MAn!")
    print("[player]님이 게임에서 퇴장하셨습니다.")

game_start()

m1= Marin()
m2 = Marin()
m3 = Marin()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units :
    unit.move("1시")


Tank.seize_developed=True
print("[알림] 탱크 시즈모드 개발이 완료 되었습니다.")

for unit in attack_units :
    if isinstance(unit,Marin):
        unit.stimpact()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()


for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,21))

game_start()