
# this class discrube default position just only function


class Default_position:

    def __init__(self):
        pass


    def stand_default_position(self,window,value,sec_value):
            if int(window.get()) < int(value) or int(window.get()) > int(sec_value):
                window.delete(0, 'end')
                window.insert(0,'{}'.format(value))
                self.master.after(500,self.stand_default_position(window,value,sec_value))


    def stand_min_interval(self,interv):
        interv.set(1)








# in w_v meaning is window variable(all 4 :2window and 2limit for each )
    def stand_default_loop_position(self,window1,first_w_v1,first_w_v2,):
        if int(window1.get()) < int(first_w_v1) or int(window1.get()) > int(first_w_v2):
            window1.set(first_w_v2)

            self.master.after(500,self.stand_default_loop_position(window1,first_w_v1,first_w_v2,))




    def speedlimit_starter(self,window):
        if int(window.get()) < 1:
                window.set(50)
        if int(window.get())  > int(100):
                window.set(100)
                self.master.after(500,self.speedlimit_starter(window))



    def no_more_bigger_interval(self):
        pass
