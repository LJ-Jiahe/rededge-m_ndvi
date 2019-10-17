from torchvision import transforms

data_dir = "data/"
transform=transforms.ToTensor()
colormap = 'RdYlGn'
ndvi_image_dir_colored = "ndvi_colored/"
ndvi_image_dir_grayscale = "ndvi_grayscale/"

image_extension = ".png"

image_range = slice(0, 12)
video_name = 'ndvi.avi'