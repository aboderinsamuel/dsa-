class Solution:
    def nthRowOfPascalTriangle(self, n):
        row = [1] #Set the first row of the Pascal's triangle
        for _ in range(n - 1): # Loop through each row
            new_row = [1] # Start the new row with 1
            for i in range(len(row) - 1): # Loop through each element in the current row
                new_row.append(row[i] + row[i + 1]) # Add the sum of the two adjacent elements to the new row
            new_row.append(1) # End the new row with 1
            row = new_row # Update the current row with the new row
        return row
solution = Solution()
n = 6
output = solution.nthRowOfPascalTriangle(n)
print(output)