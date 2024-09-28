#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Extra_13
# 204111 sec 003

def main():
    print(sand_towers([9, 12, 6]))

def sand_towers(heights):
    max_height = max(heights)  # The tallest tower height
    num_towers = len(heights)
    
    # Build each row from top to bottom
    for row in range(max_height):
        line = []
        for h in heights:
            current_level = max_height - row  # Determine the current level for this row
            if current_level <= h:
                # Calculate the width of the tower at this height
                tower_width = 2 * (current_level - 1) + 1
                # Create the structure with spaces, slashes, and carets
                side_space = ' ' * (h - current_level)
                carets = '^' * tower_width
                tower = side_space + '/' + carets + '\\' + side_space
            else:
                # If this tower doesn't reach this row, it's just empty space
                tower = ' ' * (2 * h + 2)
            line.append(tower)
        print('   '.join(line))  # Join towers with spaces between them
    
    # Finally, print the ground
    ground = ' '.join([':' * (2 * h + 2) for h in heights])
    return ground

# Example usage:

if __name__ == '__main__':
    main()
