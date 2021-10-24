import math

DEBUG = False

def p(msg):
  global DEBUG
  if (DEBUG):
    print(msg)


def distance(x1, y1, x2, y2):
  return math.sqrt((x2-x1)**2+(y2-y1)**2)