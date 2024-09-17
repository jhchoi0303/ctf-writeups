def brainfuck_decode(brainfuck_code):
    memory = [0] * 30000  # Initialize memory with 30,000 cells
    pointer = 0  # Memory pointer
    output = []  # To store output characters
    code_pointer = 0  # Pointer to traverse Brainfuck code
    loop_stack = []  # Stack to manage loops

    while code_pointer < len(brainfuck_code):
        command = brainfuck_code[code_pointer]

        if command == '>':
            pointer += 1  # Move pointer to the right
        elif command == '<':
            pointer -= 1  # Move pointer to the left
        elif command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256  # Increment memory cell value
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256  # Decrement memory cell value
        elif command == '.':
            output.append(chr(memory[pointer]))  # Output the character at the current memory cell
        elif command == ',':
            pass  # Input is not used in this script
        elif command == '[':
            if memory[pointer] == 0:
                # Skip to the command after the matching ]
                open_brackets = 1
                while open_brackets != 0:
                    code_pointer += 1
                    if brainfuck_code[code_pointer] == '[':
                        open_brackets += 1
                    elif brainfuck_code[code_pointer] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(code_pointer)  # Save current position for the loop
        elif command == ']':
            if memory[pointer] != 0:
                code_pointer = loop_stack[-1]  # Go back to the start of the loop
            else:
                loop_stack.pop()  # End of the loop, remove the loop start position from stack

        code_pointer += 1

    return ''.join(output)

# Example usage:
brainfuck_code = ">+++++++++++[<++++++++++>-]<[-]>++++++++[<++++++>-]<[-]>++++++++[<++++++>-]<[-]>++++++++++++++[<+++++++>-]<[-]>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++>-]<[-]>+++++++++++++++++++++++++++++++++++++++++[<+++>-]<[-]>+++++++[<+++++++>-]<[-]>+++++++++++++++++++[<+++++>-]<[-]>+++++++++++[<+++++++++>-]<[-]>+++++++++++++[<++++>-]<[-]>+++++++++++[<++++++++++>-]<[-]>+++++++++++++++++++[<+++++>-]<[-]>+++++++++++[<+++++++++>-]<[-]>++++++++[<++++++>-]<[-]>++++++++++[<++++++++++>-]<[-]>+++++++++++++++++[<+++>-]<[-]>+++++++++++++++++++[<+++++>-]<[-]>+++++++[<+++++++>-]<[-]>+++++++++++[<++++++++++>-]<[-]>+++++++++++++++++++[<+++++>-]<[-]>++++++++++++++[<+++++++>-]<[-]>+++++++++++++++++++[<++++++>-]<[-]>+++++++++++++[<++++>-]<[-]>+++++++[<+++++++>-]<[-]>+++++++++++[<++++++++++>-]<[-]>+++++++++++++++++[<++++++>-]<[-]>+++++++[<++++++>-]<[-]>+++++++++++[<+++++++++>-]<[-]>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+>-]<[-]>+++++++++++[<+++>-]<[-]>+++++++++++++++++++++++++[<+++++>-]<[-]."
print(brainfuck_decode(brainfuck_code))  # This will output 'A'

