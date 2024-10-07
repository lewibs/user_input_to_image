from PIL import Image, ImageDraw, ImageFont
from env import scale, click_radius, min_mouse, max_mouse, line_thickness
from utils import lerp_color
import math

class Action:
    def __init__(self, value, x, y) -> None:
        self.value = value
        self.x = x
        self.y = y

    def draw(self):
        pass

class Click(Action):
    def draw(self, draw_object):
        center = (self.x*scale, self.y*scale) 
        radius = click_radius * scale
        bounding_box = [
            (center[0] - radius, center[1] - radius),
            (center[0] + radius, center[1] + radius)
        ]
        draw_object.ellipse(bounding_box, outline=self.value, fill=self.value,)

class Mouse(Action):
    def draw(self, draw_object):
            # Define the start and end points of the line
            end_x,end_y = map(float, self.value.split(","))
            start_x, start_y = self.x * scale, self.y * scale
            end_x, end_y = end_x * scale, end_y * scale


            start_point = (start_x, start_y)
            end_point = (end_x, end_y)
            distance = math.sqrt((end_point[0] - start_point[0])**2 + (end_point[1] - start_point[1])**2)
            max_distance = math.sqrt(scale**2+scale**2)
            t = distance/(max_distance/4)
            
            color = lerp_color(min_mouse, max_mouse, t)
            line_width = line_thickness
            
            print(color, t)
            # Draw the line
            draw_object.line([start_point, end_point], fill=color, width=line_width)