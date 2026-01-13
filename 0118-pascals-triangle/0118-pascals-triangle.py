class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle: list[list[int]] = []
        for i in range(numRows):
            # Create the current row with all 1's
            row = [1] * (i+1)
            for c in range(1, i): # From the second element to the -2 element
                row[c] = triangle[i-1][c-1] + triangle[i-1][c]
            triangle.append(row)
        return triangle
