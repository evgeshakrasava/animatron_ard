from subprocess import call
import shutil
from sketchbooks.SW.run_servo import compiling
from random import randint
import random
from collections import  OrderedDict

class EXAMPLER:
    def __init__(self):
        i=10
        self.default_begin = [0,50, 0,50, 100,50, 100,50, 130,50, 30,50, 30,50, 30,50, 0,50]
        self.servo_angles_defaults = [90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50]
        self.sql_time = 1
        self.duration = 18000
        self.counter  = 0
        # variable for save default keys quantity
        self.key = 15


    def switcher(self,f,s):
        return f,s

    def generateNumber(self,num,over,shag,values):
        # generate model execute for compare with servo execute
        model = {}
        for i in range(num,over,shag):
            model['{}'.format(i)] = values

        return model






    def create_intervals(self):
        #obviously create list intervals of all servos
        my_randoms=[random.randrange(1,101,1) for _ in range (100)]
        return my_randoms


    def find_minimal_interval(self):
        # compare all intervals
        my_intervals = self.create_intervals()
        min_interval = min(my_intervals)
        return min_interval


    def create_min_keys(self):
        min_interval = self.find_minimal_interval()
        time_execute = self.generateNumber(0,5,1,self.default_begin)
        return time_execute


    def create_some_servo_angles(self):
        # generate servo execute list
        servo_angle = self.generateNumber(0,10,5,self.servo_angles_defaults)
        return servo_angle


    def call_just_one_angle(self,one_angle,another_angle):
        # return one value by counter
        # fix just one TODO
        self.counter +=1
        if self.counter == 1:
            self.counter+1
            return one_angle
        if self.counter == 2:
            self.counter = 0
            return another_angle



    def keys_finder(self):
        # first place for global values
        self.key = len(self.create_min_keys())
        print('HUEC'+(str(len(self.create_min_keys()))))
    def servo_key_finder(self):
        pass

    def divider_angle(self,basic_angle):
        min_interval = 0.2
        interval_servo = 0.6
        interval_div = int((interval_servo * 10) / (min_interval * 10))
        div_angle = 0
        interval = round(basic_angle / interval_div)
        some_execute = [div_angle]
        for _ in range(self.key):
            if div_angle >= basic_angle:
                interval *= -1
            div_angle += interval
            if div_angle <= 0:
                interval *= -1
            some_execute.append(div_angle)

        return some_execute

    def servo_on_min_interval(self,number,position):
        # want some loop with change execute on servos each event execute each iteration
        execute = self.create_min_keys()
        servo_execute = self.divider_angle(number)
        for key  in execute.keys():
            execute[key][position] = 
        return execute

    def create_execute(self):
        execute = self.servo_on_min_interval(0,99,1)
        execute = self.servo_on_min_interval(2,100,2)
        execute = self.servo_on_min_interval(4,120,3)
        execute = self.servo_on_min_interval(6,130,4)
        execute = self.servo_on_min_interval(8,190,5)
        execute = self.servo_on_min_interval(10,220,6)
        execute = self.servo_on_min_interval(12,320,7)
        execute = self.servo_on_min_interval(14,50,8)
        execute = self.servo_on_min_interval(16,999,9)

        return execute

    def big_while(self):

        scale = self.create_execute()
        print(scale)
        return scale

    def use_execute(self):
        execute = self.big_while()
        for key,value in execute.items():
            self.sql_speed1 = value[1]
            self.sql_speed2 = value[3]
            self.sql_speed3 = value[5]
            self.sql_speed4 = value[7]
            self.sql_speed5 = value[9]
            self.sql_speed6 = value[11]
            self.sql_speed7 = value[13]
            self.sql_speed8 = value[15]
            self.sql_speed9 = value[17]
            self.sql_servo_1 = value[0]
            self.sql_servo_2 = value[2]
            self.sql_servo_3 = value[4]
            self.sql_servo_4 = value[6]
            self.sql_servo_5 = value[8]
            self.sql_servo_6 = value[10]
            self.sql_servo_7 = value[12]
            self.sql_servo_8 = value[14]
            self.sql_servo_9 = value[16]





    def clear_strings(self):
        # clean by rubish
        f = open('template.h', 'r')
        o = open('VAL.h', 'w')
        print('writing1')
        while 1:
            line = f.readline()
            if not line: break
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.replace(',,', ',')
            line = line.replace("''", '0')
            line = line.replace('[][]', '[]')
            line = line.replace('{[]}', '{}')
            line = line.replace('{[', '{')
            line = line.replace(']}', '}')
            line = line.replace(')]};', '')
            o.write(line)
        o.close()



    def writing(self):
        with open('template.h', 'w') as file:
            file.writelines('int time_play={};\n'.format(self.duration))
            file.writelines('int speed_row[] = {')
            file.writelines(str(self.sql_speed1))
            file.writelines('};\n')
            file.writelines('int speed_row2[] = {')
            file.writelines(str(self.sql_speed2))
            file.writelines('};\n')
            file.writelines('int speed_row3[] = {')
            file.writelines(str(self.sql_speed3))
            file.writelines('};\n')
            file.writelines('int speed_row4[] = {')
            file.writelines(str(self.sql_speed4))
            file.writelines('};\n')
            file.writelines('int speed_row5[] = {')
            file.writelines(str(self.sql_speed5))
            file.writelines('};\n')
            file.writelines('int speed_row6[] = {')
            file.writelines(str(self.sql_speed6))
            file.writelines('};\n')
            file.writelines('int speed_row7[] = {')
            file.writelines(str(self.sql_speed7))
            file.writelines('};\n')
            file.writelines('int speed_row8[] = {')
            file.writelines(str(self.sql_speed8))
            file.writelines('};\n')
            file.writelines('int speed_row9[] = {')
            file.writelines(str(self.sql_speed9))
            file.writelines('};\n')
            file.writelines('int LEyeArray[][] = {')
            file.writelines(str(self.sql_servo_1))
            file.writelines('};\n')
            file.writelines('int REyeArray[] = {')
            file.writelines(str(self.sql_servo_2))
            file.writelines('};\n')
            file.writelines('int LArmArray[] = {')
            file.writelines(str(self.sql_servo_3))
            file.writelines('};\n')
            file.writelines('int RArmArray[] = {')
            file.writelines(str(self.sql_servo_4))
            file.writelines('};\n')
            file.writelines('int LhandArray[] = {')
            file.writelines(str(self.sql_servo_5))
            file.writelines('};\n')
            file.writelines('int RhandArray[] = {')
            file.writelines(str(self.sql_servo_6))
            file.writelines('};\n')
            file.writelines('int LLegArray[] = {')
            file.writelines(str(self.sql_servo_7))
            file.writelines('};\n')
            file.writelines('int RLegArray[] = {')
            file.writelines(str(self.sql_servo_8))
            file.writelines('};\n')
            file.writelines('int AssArray[] = {')
            file.writelines(str(self.sql_servo_9))
            file.writelines('};\n')
            file.writelines('unsigned long KeyArray[] = {')
            file.writelines(str(self.time))
            file.writelines('};\n')
        print('write to file')
        self.clear_strings()
        call('rm template.h', shell=True)
        shutil.move("/home/qbc/PycharmProjects/ard/VAL.h",
                    "/usr/share/arduino/hardware/arduino/cores/arduino/VAL.h")



caca =  EXAMPLER()
















caca = EXAMPLER()
print(caca.servo_on_min_interval(88,0))
