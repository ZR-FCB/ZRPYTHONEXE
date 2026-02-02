class Student: 
    def __init__(self, name,student_id, enrollment_year, **kwargs):
        self.name = name
        self.student_id = student_id
        self.enrollment_year = enrollment_year
        self._post_init()
        
        for key, value in kwargs.items():
            setattr(self, key, value)      
    
    def calculate_gpa(self, grades):
        if len(grades) == None: 
            return print("the list can't be umpty")
        else:
               return sum(grades)/len(grades) 
                

            
    def _post_init(self):
        self.graduation_year = self.enrollment_year + 4

    def __str__(self):
        return f"Student : {self.name} (ID:{self.student_id})"



# Create a student
s = Student("Maria", "S999", 2023, major="Biology", dorm="West Hall")

# Test 1: Access attributes
print(f"Name: {s.name}")
print(f"Major: {s.major}")
print(f"Dorm: {s.dorm}")

# Test 2: Graduation year
print(f"Graduates in: {s.graduation_year}")  # Should be 2027

# Test 3: GPA calculation
grades = [88, 92, 79, 95]
print(f"GPA: {s.calculate_gpa(grades)}")  # Should be ~88.5

# Test 4: String representation
print(s)  # Should print: Student: Maria (ID: S999)