import time


class DoorController:

    def __init__(self, DoorOne, DoorTwo, ByPass, timer):
        self.DoorOne = DoorOne
        self.DoorTwo = DoorTwo
        self.ByPass = ByPass
        self.timer = timer

    def interlock(self):
        DoorOpen = False
        ByPassState = False
        
        		
		# Door will not open 
        if ((self.DoorOne == True) and (self.DoorTwo == False) and (self.ByPass == False)):
            DoorOpen = False
            ByPassState = False
            
		# Interlock Override 
        elif ((self.DoorOne == True) and (self.DoorTwo == False) and (self.ByPass == True)):
            DoorOpen = True
            ByPassState = False
            
		# Normal Door Open
        elif ((self.DoorOne == True) and (self.DoorTwo == True) and (self.ByPass == False)):
            DoorOpen = True
            ByPassState = False
            
        elif ((self.DoorOne == False) and (self.DoorTwo == False) and (self.ByPass == False)):
            DoorOpen = False
            ByPassState = False
		# Door will not open 
        else:
           	DoorOpen = False
        	ByPassState = False

        return DoorOpen, ByPassState
