from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from Action import Mouse, Click
from env import scale

def convert_to_png(pil_image):
    # Create an in-memory byte buffer
    buffer = BytesIO()
    
    # Save the PIL image as PNG in the buffer
    pil_image.save(buffer, format="PNG")
    
    # Get the PNG data from the buffer
    png_data = buffer.getvalue()
    
    # Close the buffer
    buffer.close()
    
    return png_data

def convert(clickable_key=[], actions=[]):
    clickable_color_key = {}
    for [clickable, color] in clickable_key:
        clickable_color_key[clickable] = color if color else 0x888888
    
    # black to save space!
    img = Image.new('RGB', (scale, scale), color='black')
    d = ImageDraw.Draw(img)

    for action in actions:
        action_type, start, value = action
        x,y = map(float, start.split(","))
        
        if action_type == "mouse":
            action = Mouse(value, x, y)
        elif action_type == "click":
            action = Click(clickable_color_key[value], x, y)
        else:
            raise Exception("Not a valid type") # consider having a catch all type.
        
        action.draw(d)

    return convert_to_png(img)

def display_png(png_data):
    # Open the image from the PNG data buffer
    png_image = Image.open(BytesIO(png_data))
    png_image.show()

if __name__ == "__main__":
    img = convert(
        clickable_key=[
            ["text","red"],
            ["image","green"],
            ["link","blue"]
        ],
        # I dont like this i1,1nput. The thought was I can just do gradiant as a single dec but not sure.
        actions=[
            # All input should be type, start, value still figuring out best input
            ["mouse", "0.5,0.5","0.6,0.6"],
            ["mouse", "0.6,0.6","0.6,0.8"],
            ["click", "0.6,0.8", "text"],
            ["mouse", "0.6,0.8","1,1"],
            ["click", "1,1", "link"],
        ]
    )
    display_png(img)
