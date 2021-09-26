from DoorCon import DoorController

DoorOne = True					'system.tag.readBlocking(['[Cobb County Courts]Design/DuressButton'])[0].value
DoorTwo = False 				'system.tag.readBlocking(['[Cobb County Courts]Design/DuressButton'])[0].value
DoorThree = null
ByPass = system.tag.readBlocking(['[Cobb County Courts]Design/DuressButton'])[0].value
timer = 5


interlock(DoorOne, DoorTwo, ByPass, timer)