import math

RES = WIDTH, LENGTH = 1600, 900
HALF_WIDTH = WIDTH//2
HALF_LENGTH = LENGTH//2
FPS = 120

PLAYER_POSITION = 2, 4
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.05
PLAYER_ROTATION_SPEED = 0.1
PLAYER_SIZE_SCALE = 500

MOUSE_SENSITIVITY = 0.002
MOUSE_MAX_REL = 40              #ruch myszki w jednym cyklu pętli gry nie będzie większy niż 40 jednostek (pikseli)
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30)

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

TILESIZE = 64 # to zmienna, która określa rozmiar pojedynczego kafelka (tile) na mapie w grze