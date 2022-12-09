class Map:
    def __init__(self, input) -> None:
        self.matrix = []
        for row in input.strip().split():
            self.matrix.append([int(x) for x in row])
            
    @property
    def corners_trees(self):
        return (len(self.matrix[0]) * 2) + (len(self.matrix) - 2) * 2
    
    @property
    def visible_trees(self):
        inside_visibles_tree = 0
        for row_num in range(0, len(self.matrix)):
            if row_num == 0 or row_num == len(self.matrix) - 1:
                continue
            for col_num in range(0, len(self.matrix[row_num])):
                if col_num == 0 or col_num == len(self.matrix[row_num]) - 1:
                    continue
                if self.is_visible(row_num, col_num):
                    inside_visibles_tree += 1
        return self.corners_trees + inside_visibles_tree
    
    @property
    def max_score(self):
        max_score = 0
        for row in range(0, len(self.matrix)):
            for col in range(0, len(self.matrix[row])):
                max_score = max(max_score, Tree((row, col), self.matrix).score)
        return max_score
    
    def is_visible(self, row, col):
        return Tree([row, col], self.matrix).visible


class Tree:
    def __init__(self, position, matrix) -> None:
        self.position = position
        self.matrix = matrix
        self._score = None
        self.num_trees = {
            'left': 1,
            'rigth': 1,
            'top': 1,
            'bottom': 1
        }
    
    @property
    def lenght(self):
        row, col = self.position
        return self.matrix[row][col]
    
    @property
    def score(self):
        import math
        if self._score is None:
            self.visible
            self._score = math.prod(list(self.num_trees.values()))
        return self._score
    
    @property
    def visible(self):
        visibility = []
        row, col = self.position
        tree = self.lenght
        items_left = reversed([self.matrix[row][x] for x in range(0, col)])
        num_trees = 0
        for i in items_left:
            num_trees += 1
            if i >= tree:
                break
        else:
            visibility.append('left')
        self.num_trees['left'] = num_trees
        items_right = [self.matrix[row][x] for x in range(col + 1, len(self.matrix[row]))]
        num_trees = 0
        for i in items_right:
            num_trees += 1
            if i >= tree:
                break
        else:
            visibility.append('right')
        self.num_trees['right'] = num_trees
        items_top = reversed([self.matrix[x][col] for x in range(0, row)])
        num_trees = 0
        for i in items_top:
            num_trees += 1
            if i >= tree:
                break
        else:
            visibility.append('top')
        self.num_trees['top'] = num_trees
        items_bottom = [self.matrix[x][col] for x in range(row + 1, len(self.matrix))]
        num_trees = 0
        for i in items_bottom:
            num_trees += 1
            if i >= tree:
                break
        else:
            visibility.append('bottom')
        self.num_trees['bottom'] = num_trees
        return visibility
