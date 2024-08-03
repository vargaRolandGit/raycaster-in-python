import math

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 30
MAP_SIZE = 8
TILE_SIZE = int((WINDOW_HEIGHT / 2) / MAP_SIZE)  
FOV = math.pi / 3
HALF_FOV = FOV / 2
CASTED_RAYS = int(1280 / 10)
STEP_ANGLE = FOV / CASTED_RAYS 
MAX_DEPTH = int(MAP_SIZE * TILE_SIZE)
SCALE = (WINDOW_WIDTH) / CASTED_RAYS

MAP = (
    '########'
    '# #    #'
    '# #  ###'
    '#      #'
    '#      #'
    '#  ##  #'
    '#   #  #'
    '########'
)