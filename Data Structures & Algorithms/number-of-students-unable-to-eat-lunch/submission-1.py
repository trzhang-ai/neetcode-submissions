class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        trials = 0
        while True:
            student = students.pop(0)
            sandwich = sandwiches.pop(0)
            if student != sandwich:
                students.append(student)
                sandwiches = [sandwich] + sandwiches
            else:
                trials = 0
            trials += 1
            if trials > len(students):
                break
        return len(students)