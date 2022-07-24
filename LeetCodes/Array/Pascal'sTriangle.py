"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class generate(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        else:
            res = [[1]]
            for id_row in range(1, numRows):
                pre_row = res[-1]
                cur_row = [1]
                for id in range(1, len(pre_row)):
                    cur_row.append(pre_row[id - 1] + pre_row[id])
                cur_row.append(1)
                res.append(cur_row)
            return res

res = generate().generate(5)
print(res)