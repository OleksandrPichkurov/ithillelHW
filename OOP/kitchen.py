class Devices:
    def __init__(self, brand, color, material):
        self.color = color
        self.material = material
        self.brand = brand
    

class Stove(Devices):

    def __init__(self, brand, color, material, burners, timer, price):
        Devices.__init__(self, brand, color, material)
        self.burners = burners
        self.timer = timer
        self.price = price

    def turn_burner(self, status):
        if status.upper() == 'ON':
            return 'Burner turn ON'
        else:
            return 'Burner turn OFF'

    def set_timer(self,h,m,s):
        time = 0
        finish = h+m+s
        while time < finish:
            print('still preparing')
            time += 1
        else:
            return 'Done'


class Teapot(Devices):

    def __init__(self, brand, color, material):
        Devices.__init__(self, brand, color, material)

    def stay_warm(self, btn_on_off, initial_temp, set_temp):
        power = 'ON'
        if btn_on_off.upper() == 'ON':
            while initial_temp < set_temp:
                initial_temp += 1 
            else:
                return power == 'OFF'
        else:
             return 'Stand by'


        

#s1 = Stove('LG', 'White', 'Steal', 4, True, 500)
#s2 = Stove('Apple', 'Black', 'Steal', 6, False, 1000)
#t1 = Teapot('Xiaomi', 'White', 'Plastic')
#t2 = Teapot('Xiaomi', 'Black', 'Plastic')
#print(s2.set_timer(1,1,1))
#print(s1.color, s1.brand)
#print(s1.turn_burner('ON'))
#print(s2.material, s2.timer)
#print(t1.color, t1.brand)
#print(t2.stay_warm('off', 4, 3))