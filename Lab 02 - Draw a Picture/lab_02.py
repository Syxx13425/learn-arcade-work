import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def draw_fish(x,y,s):
    pass
def draw_stars(x,y,s):
    pass

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
# drawing the water
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
arcade.draw_arc_filled(300,0,600,400,arcade.color.OCEAN_BOAT_BLUE,20,160)
arcade.draw_lrtb_rectangle_filled(0,SCREEN_WIDTH,100,0,arcade.csscolor.GREEN)

arcade.finish_render()
arcade.run()