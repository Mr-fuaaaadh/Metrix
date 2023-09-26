first_multiple_input = input().rstrip().split()
print(first_multiple_input)
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

print(matrix)
Answer = ''
InputValue = 0
# connecting string
while InputValue < m:
    for x in matrix:
        Answer = Answer + x[InputValue]
    InputValue = InputValue + 1
# Removing special characters
chars = '~`!@#$%^&*()-_=+[{]}\|;:"<,.>/?' + "'"
for Chara in chars:
    Answer = Answer.replace(Chara, " ")
# Replacing two white space into One white space 
OutPut = Answer.replace("  ", " ")
print(OutPut)
