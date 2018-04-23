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


    def time_finder(self):
        # find difference between oldvalues keys and new ,return time execute inter
        pass

    def interval_devider(min_interval,interval_servo,angle_1,angle_2):
        round(interval_servo)
        pass


    def switcher(self,f,s):
        return f,s



    def generateNumber(self,num,over,shag,values):
        model = {}
        for i in range(num,over,shag):
            model['{}'.format(i)] = values

        return model






    def create_intervals(self):
        my_randoms=[random.randrange(1,101,1) for _ in range (5)]
        return my_randoms


    def find_minimal_interval(self):
        my_intervals = self.create_intervals()
        min_interval = min(my_intervals)
        return min_interval


    def create_min_keys(self):
        min_interval = self.find_minimal_interval()
        # create time scale with keys  and position
        # time_execute = [self.generateNumber(oldvalues.key,new_values.key,interval)]
        time_execute = self.generateNumber(0,15,min_interval,self.default_begin)

        return time_execute


    def create_some_servo_angles(self):
        servo_angle = self.generateNumber(0,10,5,self.servo_angles_defaults)

        return servo_angle


    def division_angles(self,interval_servo,angle_1,angle_2):
        # division angle depend on minimal interval
#         add ordered dict
            min_interval = round(self.find_minimal_interval())
            division_angle = min_interval/interval_servo
            first_angle_for_execute  = division_angle/angle_1
            second_angle_for_execute  = division_angle/angle_2
            return first_angle_for_execute,second_angle_for_execute





    def comprassion(self,positon,number):
        # servo_scale meaning is scale for comprasion with  default scale in minimal interval
        # he obtain values from servo scale and changed yourself.if servo angle doesn't have position between

        time_execute = self.create_min_keys()
        servo_scale = self.create_some_servo_angles()
        for key in time_execute.keys():
            if key in servo_scale.keys():
                # division_angles()
                time_execute[key][positon] = self.division_angles(4,number,number)


                print('time_execute is '+str(time_execute))
                print('servo_scale is '+str(servo_scale))









    def create_execute(self):
        min_interval = self.create_min_keys()
        servo_angle = self.create_some_servo_angles()
        execute = self.comprassion(0,99)
        execute = self.comprassion(2,100)
        execute = self.comprassion(4,120)
        execute = self.comprassion(6,130)
        execute = self.comprassion(8,190)
        execute = self.comprassion(10,220)
        execute = self.comprassion(12,320)
        execute = self.comprassion(14,50)
        execute = self.comprassion(16,999)
        print(execute)
        return execute

    def use_execute(self):
        execute = create_execute()
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
            self.sql_servo_2 = value[0]
            self.sql_servo_3 = value[0]
            self.sql_servo_4 = value[0]
            self.sql_servo_5 = value[0]
            self.sql_servo_6 = value[0]
            self.sql_servo_7 = value[0]
            self.sql_servo_8 = value[0]
            self.sql_servo_9 = value[0]





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
# caca.writing()
# compiling()















caca = EXAMPLER()

caca.create_execute()
























############################################################################################################################################
