import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
SIZE = {"paddle": (40, 100), "ball": (30,30)}
SPEED = {"player": 500, "opponent": 450, "ball": 450}

POS = {"player": (WINDOW_WIDTH -50, WINDOW_HEIGHT/2), "opponent": (50, WINDOW_HEIGHT/2)}

COLORS = {
        "paddle": "#FFC0CB",
        "paddle shadow": "#FFC0CB",
        "ball": "#EE4B2B",
        "ball shadow": "#EE4B2B",
        "bg": "#5F9EA0",
        "bg detail": "#0096FF"
}
