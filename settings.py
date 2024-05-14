import math

RES = WIDTH, LENGTH = 1600, 900
HALF_WIDTH = WIDTH//2
HALF_LENGTH = LENGTH//2
FPS = 70

PLAYER_POSITION = 1.5, 2
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.04
PLAYER_ROTATION_SPEED = 0.03

FOV = math.pi/3
HALF_POV = FOV/2
NUM_RAYS = WIDTH//2
HALF_NUM_RAYS = NUM_RAYS/2
DELTA_ANGLE = FOV/NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH/math.tan(HALF_POV)
SCALE = WIDTH//NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE//2
