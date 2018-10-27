from PIL import Image
from common.res import *
from common.screen import *

image = Image.open(success_image_filename)
image.show()
image_scale = image.resize((100,100))
image_scale.show()
image_scale.save(base_res_url + "/base/new.png", "png")
