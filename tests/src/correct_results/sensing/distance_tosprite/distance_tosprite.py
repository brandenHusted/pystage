# distance_tosprite (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable')

# Create and initialize sprite 'sprite1'
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(-167)
sprite1.set_y(-50)
sprite1.go_to_back_layer()
sprite1.go_forward(2)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

# Create and initialize sprite 'casey'
casey = stage.add_a_sprite(None)
casey.set_name("Casey")
casey.set_x(96)
casey.set_y(-17)
casey.go_to_back_layer()
casey.go_forward(1)
casey.add_costume('casey_a', center_x=75, center_y=62)
casey.add_costume('casey_b', center_x=60, center_y=74)
casey.add_costume('casey_c', center_x=57, center_y=72)
casey.add_costume('casey_d', center_x=71, center_y=74)
casey.add_sound('basketball_bounce')

def when_key_pressed_1(self):
    self.glide_to_random_position(1.0)
    self.say(self.distance_to_sprite("NO TRANSLATION: sensing_distancetomenu"))

casey.when_key_pressed("space", when_key_pressed_1)

stage.play()
