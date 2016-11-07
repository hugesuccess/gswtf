import matplotlib.image as mp_image

filename= "imapges/rgb_tensor.jpeg"

input_image = mp_image.imread(filename)

print('input dim = {}'.format(input_image.ndim))
print('input shape = {}'.format(input_image.shape))
