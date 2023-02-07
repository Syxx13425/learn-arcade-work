import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
fish = arcade.load_texture("fish.png")
def draw_star(x, y, scale):
    """function to draw a triangle at the specified location"""
    # base triangle is 2 pixels wide and 2 pixels high. The coordinates x and y mark the center.
    point_list = [(x - scale, y - scale), (x + scale, y - scale), (x, y + scale)] # list of tuples
    star_list = [(x, y + 4 * scale),
    (x - 1 * scale, y),
    (x - 4 * scale, y),
    (x - 1 * scale, y - 1.5 * scale),
    (x - 3.5 * scale, y - 5 * scale),
    (x , y - 2.5 * scale),
    (x + 3.5 * scale, y - 5 * scale),
    (x + 1 * scale, y - 1.5 * scale),
    (x + 4 * scale, y),
    (x + 1 * scale, y)]
    arcade.draw_polygon_filled(star_list, arcade.csscolor.WHITE_SMOKE) # draw a polygon by specifying the points


def draw_fish(x, y, s):
    arcade.draw_scaled_texture_rectangle(x,y , fish, s, 0)






def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    # drawing the night sky
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()

    # drawing the on land fish tank
    arcade.draw_arc_filled(300, 0, 600, 400, arcade.color.OCEAN_BOAT_BLUE, 20, 160)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 100, 0, arcade.csscolor.GREEN)
    arcade.draw_arc_filled(600, 600, 200, 200, arcade.color.WHITE_SMOKE, 100, 270)
    # create 50 triangles randomly placed on the screen
    draw_star(400,300,1)
    draw_star(100, 400,1)
    draw_star(288,347,2)
    draw_star(237,578,3)
    draw_star(189,460,5)
    draw_star(100,470,3)
    draw_star(450,345,2)
    draw_star(510,450,3)
    draw_star(290,560,5)
    draw_star(519,360,4)
    draw_fish(333, 187, .06)
    draw_fish(227, 170, .09)
    draw_fish(190, 130, .05)
    draw_fish(400, 120, .1)
    arcade.finish_render()
    arcade.run()

main()