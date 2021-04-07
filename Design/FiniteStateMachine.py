# Design a FSM

class FiniteStateMachine:
    def __init__(self):
        self.previous_state = 0

    def fsm(self, inputs):
        print(inputs)
        n = len(inputs)

        for i in inputs:
            self.grantingSystem(i)

    def grantingSystem(self, request):
        print(request)
        if request == "000":
            print("The machine is in idle mode")
            return
        if request == "001":
            print("Request 3 has been granted")
            self.previous_state = 3
            return
        if request == "010":
            print("Request 2 has been granted")
            self.previous_state = 2
            return
        if request == "011":
            if self.previous_state != 2:
                print("Request 2 has been granted")
                self.previous_state = 2
                return
            if self.previous_state != 3:
                print("Request 3 has been granted")
                self.previous_state = 3
                return
        if request == "100":
            print("Request 1 has been granted")
            self.previous_state = 1
            return
        if request == "101":
            if self.previous_state != 1:
                print("Request 1 has been granted")
                self.previous_state = 1
                return
            if self.previous_state != 3:
                print("Request 3 has been granted")
                self.previous_state = 3
                return
        if request == "110":
            if self.previous_state != 1:
                print("Request 1 has been granted")
                self.previous_state = 1
                return
            if self.previous_state != 2:
                print("Request 2 has been granted")
                self.previous_state = 2
                return
        if request == "111":
            if self.previous_state != 1:
                print("Request 1 has been granted")
                self.previous_state = 1
                return
            if self.previous_state != 2:
                print("Request 2 has been granted")
                self.previous_state = 2
                return
            if self.previous_state != 3:
                print("Request 3 has been granted")
                self.previous_state = 3
                return


myFsm = FiniteStateMachine()
myFsm.fsm(["000", "001", "010", "011", "100", "101", "110", "111", ])
