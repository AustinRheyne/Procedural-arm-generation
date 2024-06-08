import math

import pygame

pygame.init()  # Start Pygame

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

arm_start = (screen.get_width()/2, screen.get_height()/2)
arm_section_1 = 150
arm_section_2 = 150

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the position of the mouse
    mouse_pos = pygame.mouse.get_pos()

    # Calculate the distance from the arm start to the mouse position
    dx = mouse_pos[0] - arm_start[0]
    dy = mouse_pos[1] - arm_start[1]
    arm_dist = math.sqrt(dx ** 2 + dy ** 2)

    # Limit the arm distance to the total length of both sections
    arm_dist = min(arm_dist, arm_section_1 + arm_section_2)

    # Use law of cosines to find the angle at the arm start (theta1)
    if arm_dist == 0:
        theta1 = 0
    else:
        cos_theta1 = (arm_section_1 ** 2 + arm_dist ** 2 - arm_section_2 ** 2) / (2 * arm_section_1 * arm_dist)
        cos_theta1 = max(min(cos_theta1, 1), -1)
        theta1 = math.acos(cos_theta1)

    # Angle to the mouse position from the arm start
    base_angle = math.atan2(dy, dx)

    # Calculate the end position of the first arm section
    end_pos_1 = (arm_start[0] + arm_section_1 * math.cos(base_angle + theta1),
                 arm_start[1] + arm_section_1 * math.sin(base_angle + theta1))

    # Use law of cosines to find the angle at the end of the first section (theta2)
    if arm_dist == 0:
        theta2 = 0
    else:
        cos_theta2 = (arm_dist ** 2 + arm_section_2 ** 2 - arm_section_1 ** 2) / (2 * arm_dist * arm_section_2)
        cos_theta2 = max(min(cos_theta2, 1), -1)
        theta2 = math.acos(cos_theta2)

    # Calculate the end position of the second arm section
    end_pos_2 = (end_pos_1[0] + arm_section_2 * math.cos(base_angle - theta2),
                 end_pos_1[1] + arm_section_2 * math.sin(base_angle - theta2))

    # Draw the arm sections
    pygame.draw.line(screen, (255, 0, 0), arm_start, end_pos_1, 5)
    pygame.draw.line(screen, (0, 255, 0), end_pos_1, end_pos_2, 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
