import svgwrite
import random

def generate_sudoku_solution():
    base = 3
    side = base * base

    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side + 1

    def shuffle(s):
        return random.sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    board = [[nums[pattern(r, c) - 1] for c in cols] for r in rows]

    return board

def remove_numbers(board, difficulty_level):
    # Remove numbers based on difficulty level
    levels = {'Easy': 30, 'Medium': 40, 'Hard': 50}
    num_to_remove = levels.get(difficulty_level, 40)

    puzzle = [row.copy() for row in board]
    for _ in range(num_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0

    return puzzle

def create_svg_file(matrix, filename):
    dwg = svgwrite.Drawing(filename, profile='tiny')
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='white'))

    for i in range(9):
        for j in range(9):
            if matrix[i][j] != 0:
                dwg.add(dwg.text(str(matrix[i][j]), insert=(j * 40 + 15, i * 40 + 25), font_size="20px", fill="black"))

    dwg.save()

def main():
    solution = generate_sudoku_solution()
    difficulty_level = 'Medium'  # Change the difficulty level as needed
    puzzle = remove_numbers(solution, difficulty_level)

    create_svg_file(puzzle, 'sudoku_puzzle.svg')
    create_svg_file(solution, 'sudoku_solution.svg')

if __name__ == "__main__":
    main()
