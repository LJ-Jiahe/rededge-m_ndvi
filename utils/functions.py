import torch

def sort_key(content_name):
    content_name_split = content_name.split('.')[0].split('_')
    return int(content_name_split[1]) * 10 + int(content_name_split[2])

def ndvi(images, eps=1e-10):
    red_image = images["red"].float()
    red_image = red_image / 2**15
    # print(torch.max(red_image))
    near_ir_image = images["near_ir"].float() / 2**15
    ndvi_value = (near_ir_image - red_image) / (near_ir_image + red_image + eps)
    return ndvi_value
