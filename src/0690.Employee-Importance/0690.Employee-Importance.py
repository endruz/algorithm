from types import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution1:
    """
    深度优先搜索
    """
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashmap = {employee.id: employee for employee in employees}
        self.importance = 0

        def func(id):
            employee = hashmap[id]
            self.importance += employee.importance
            for i in employee.subordinates:
                func(i)

        func(id)
        return self.importance


class Solution2:
    """
    广度优先搜索
    """
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashmap = {employee.id: employee for employee in employees}
        importance = 0
        employee_list = [id]

        while employee_list:
            curid = employee_list.pop(0)
            importance += hashmap[curid].importance
            employee_list.extend(hashmap[curid].subordinates)
        return importance
