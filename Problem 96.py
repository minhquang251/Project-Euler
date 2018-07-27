import time
class Sudoku:
    def __init__(self, str_file):
        self.str_file = str_file
        self.lst = self.read_str()

    def read_str(self):
        lst = []
        for i in self.str_file:
            lst.append(int(i))
        return lst

    @staticmethod
    def generate_column(nth):
        variable = nth
        column = []
        for i in range(9):
            variable += 9
            if variable > 80:
                variable -= 81
            column.append(variable)
        return sorted(column)

    @staticmethod
    def generate_row(nth):
        if 0 <= nth <= 8:
            row = [i for i in range(0, 9)]
        elif 9 <= nth <= 17:
            row = [i for i in range(9, 18)]
        elif 18 <= nth <= 26:
            row = [i for i in range(18, 27)]
        elif 28 <= nth <= 35:
            row = [i for i in range(27, 36)]
        elif 36 <= nth <= 44:
            row = [i for i in range(36, 45)]
        elif 45 <= nth <= 53:
            row = [i for i in range(45, 54)]
        elif 54 <= nth <= 62:
            row = [i for i in range(54, 63)]
        elif 63 <= nth <= 71:
            row = [i for i in range(63, 72)]
        elif 72 <= nth <= 80:
            row = [i for i in range(72, 81)]
        else:
            row = []
        return sorted(row)

    def generate_block(self, nth):
        all_block = []
        for i in range(0, 7, 3):
            all_block.append(self.block_rule(i))
        for i in range(27, 34, 3):
            all_block.append(self.block_rule(i))
        for i in range(54, 61, 3):
            all_block.append(self.block_rule(i))
        for sub_block in all_block:
            if nth in sub_block:
                return sorted(sub_block)

    @staticmethod
    def block_rule(n):
        array = []
        for i in range(n, n + 3):
            array.append(i)
            array.append(i + 9)
            array.append(i + 18)
        return sorted(array)

    @staticmethod
    def full(array):
        for i in range(81):
            if array[i] == 0:
                return False
        return True

    @staticmethod
    def find_blank(array):
        blank_space = []
        for i in range(81):
            if array[i] == 0:
                blank_space.append(i)
        if len(blank_space) > 0:
            return blank_space, True
        else:
            return None, False

    def available_number(self, nth, array):
        row = self.generate_row(nth)
        column = self.generate_column(nth)
        block = self.generate_block(nth)
        unavailable = set()
        available = []
        for i in row:
            if array[i] != 0:
                unavailable.add(array[i])
        for i in block:
            if array[i] != 0:
                unavailable.add(array[i])
        for i in column:
            if array[i] != 0:
                unavailable.add(array[i])
        for i in range(1, 10):
            if i not in unavailable:
                available.append(i)
        if len(available) > 0:
            return sorted(available), True
        else:
            return None, False

    def solved(self, array):
        if self.full(array):
            return True
        square = -1
        if self.find_blank(array)[1]:
            available_blank = self.find_blank(array)[0]
            square = available_blank[0]
        if self.available_number(square, array)[1]:
            for i in self.available_number(square, array)[0]:
                array[square] = i
                if self.solved(array):
                    return True
                array[square] = 0
        return False

    def get_3_first_numbers(self):
        if self.solved(self.lst):
            return int(str(self.lst[0]) + str(self.lst[1]) + str(self.lst[2]))


def problem_96(txt_file):
    f = open(txt_file)
    content = f.read().splitlines()
    total = 0
    for i in range(0,len(content),10):
        string = ''
        for j in range(i+1,i+10):
            string += content[j]
        sudoku = Sudoku(string)
        total += sudoku.get_3_first_numbers()
    f.close()
    return total


start = time.time()
print(problem_96("Problem 96.txt"))
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))