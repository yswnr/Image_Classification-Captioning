#Imports
from PIL import Image

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self.flip_type = flip_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        '''
        if self.flip_type=='horizontal':
           flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif self.flip_type=='vertical':
           flipped_image = image.transpose(Image.FlIP_TOP_BOTTOM)
        elif self.flip_type=='anticlockwise':
           flipped_image = image.transpose(Image.TRANSPOSE)
        elif self.flip_type=='clockwise':
           flipped_image=image.transpose(Image.TRANSVERSE)
        return flipped_image            
