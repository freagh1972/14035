class PopupAudio:

    def __init__(self, monitor_tag, window, level, sound):
        self.monitor_tag = monitor_tag
        self.window = window
        self.level = level
        self.sound = sound

    def mute_sound(self):
    	monitor = system.tag.readBlocking([self.monitor_tag])[0].value
    
        if monitor == True:
			print('step_1')
			window = system.nav.openWindow(self.window)
			mute = system.tag.readBlocking([self.level])[0].value
			
			print('Step_2')
			print(type(mute))	
            
            
			while mute == 1.0:
				print('Step_3')
				mute = system.tag.readBlocking([self.level])[0].value	
				system.util.playSoundClip(self.sound,mute,1)
				if mute == 0.0:
					break
            		
				elif mute == 0:
					system.tag.writeBlocking([self.level],[1])
			
			system.tag.writeBlocking([self.level],[1])
            		
            		            		

            		            		

					 		 	

				

