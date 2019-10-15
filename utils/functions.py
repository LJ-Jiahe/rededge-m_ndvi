

def sort_key(content_name):
    content_name_split = content_name.split('.')[0].split('_')
    return int(content_name_split[1]) * 10 + int(content_name_split[2])

def ndvi(images):
    red_image = images["red"].float()
    near_ir_image = images["near_ir"].float()
    ndvi_value = (near_ir_image - red_image) / (near_ir_image + red_image)
    return ndvi_value
