import pygame
import random
import sys
import asyncio

async def main(rows, columns, cell_size=30):
    # Initialize pygame
    pygame.init()

    
    # pygame.mixer.music.load("background.wav")
    # pygame.mixer.music.play(-1)

    # Grid dimensions
    width = columns * cell_size
    height = rows * cell_size

    # Colors
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)

    # Screen setup
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dynamic Grid Animation")

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Red strip position
    red_strip_start = 2  # Start after the green columns
    red_strip_width = 2  # Width of the red strip
    red_strip_pos = red_strip_start

    # Randomly place blue cells (excluding the green and red strip areas)
    blue_cells = []
    for _ in range((rows * (columns - red_strip_start - red_strip_width)) // 10):
        while True:
            random_row = random.randint(0, rows - 1)
            random_col = random.randint(red_strip_start, columns - 1)
            if random_col < red_strip_pos or random_col >= red_strip_pos + red_strip_width:
                blue_cells.append((random_row, random_col))
                break

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw the grid
        for row in range(rows):
            for col in range(columns):
                x = col * cell_size
                y = row * cell_size

                if col < red_strip_start:
                    # Green columns
                    color = GREEN
                elif red_strip_pos <= col < red_strip_pos + red_strip_width:
                    # Red strip
                    color = RED
                elif (row, col) in blue_cells:
                    # Blue cells
                    color = BLUE
                else:
                    # Default white background
                    color = WHITE

                pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
                pygame.draw.rect(screen, (0, 0, 0), (x, y, cell_size, cell_size), 1)  # Grid lines

        # Update red strip position
        red_strip_pos += 1
        if red_strip_pos + red_strip_width > columns:
            red_strip_pos = red_strip_start

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(5)

    pygame.quit()
    await asyncio.sleep(0)


if __name__ == "__main__":
    # Example usage: 10x10 grid
    rows = 20
    columns = 15
    asyncio.run(main(rows, columns))
