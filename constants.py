import numpy as np

# Define cost of moving around the map
cost_regular = 1.0
cost_diagonal = 1.7

# Create the cost dictionary
COSTS = {
    "up": cost_regular,
    "down": cost_regular,
    "left": cost_regular,
    "right": cost_regular,
    "up left": cost_diagonal,
    "up right": cost_diagonal,
    "down left": cost_diagonal,
    "down right": cost_diagonal,
}

# Define the map
MAP = """
#########################################
#                                       #
# #### ########### ########### ######  ##
# #   #           #           #      #  #
# #   # ######### # ######### # #### #  #
# #                 #                 # #
# ###### ##### ### # ### ##### ###### # #
#        #   # #   #   # #   #        # #
# ######## # # # ##### # # # ######## # #
# #       # # # #     # # # #       # # #
# # ##### # # ### ### # # ### ##### # # #
# #   #   # #   # #   # #   #   #   # # #
# ### # ##### ### ##### ### ##### # ### #
#     #       #   #   #   #       #     #
####### ### # ##### # ##### # ### #######
#         # #       #       # #         #
# ### ### # ##### # # ##### # ### ### ###
#   #   # #   #   # # #   # #   #   #   #
##### ### ### ### ### ### ### ### ### ###
#       #   #           #   #       #   #
# ####### # ##### ### ##### # ### # ### #
# #       #     # # #   #   #   # #   # #
# ### ##### ### ### ### ### # # ##### # #
#     #   # #   #   #   #   # #     # # #
### ##### # ##### ### ### ### ### # # ###
# #       #       #     #   #   # # #   #
# # # ##### ########### ### ### ### ### #
#   #               #       #           #
#########################################
"""

MAP = [list(x) for x in MAP.split("\n") if x]

# Map dimensions
M = len(MAP)
N = len(MAP[0])
W = 25

# Colors for map rendering
mau_den = np.zeros((W, W, 3), np.uint8) + (100, 100, 100)
mau_trang = np.zeros((W, W, 3), np.uint8) + (255, 255, 255)
