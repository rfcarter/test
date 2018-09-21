def matrix(size,fill_value):
    matrix=[]
    for _ in range(size):
        row=[]
        for _ in range(size):
            row.append(fill_value)
        matrix.append(row)
    return matrix

if __name__ == '__main__':
    print(matrix(3,'abc'))

