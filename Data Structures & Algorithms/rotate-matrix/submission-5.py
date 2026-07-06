
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i, j = 0,0 
        counter = 0
        length_counter = len(matrix)
        while True:
            a = matrix[i][j]
            new_i = j
            new_j = len(matrix) - i - 1
            counter += 1
            print(i,j)
            while new_i != i or new_j != j:
                print(new_i,new_j)
                counter += 1
                b = matrix[new_i][new_j]
                matrix[new_i][new_j] = a
                a = b
                temp = new_j
                new_j = len(matrix) - new_i - 1
                new_i = temp
                
            print("penis", counter)
            matrix[i][j] = a
            if counter == len(matrix) ** 2:
                return
            elif j == length_counter - 2:
                print(i,j, "asdf")
                t = i
                i = i + 1
                j = t + 1
                length_counter -= 1
            else:
                j = j + 1
            
