employee = [{"Name":"Ron Swanson",
             "age":55,
             "department":"Management",
             "phone":"555-1234",
             "salary":" ,000"},
           {"Name":"Leslie Knope",
           "department":"Middle Management",
           "phone":"555-4321"},
           {"Name":"Andy Dwyer",
           "department":"shoe shining",
           "phone":"555-1122"},
           {"Name":"April Ludgate",
           "department":"Administration",
           "phone":"555-3345"}]

for i in employee:
    name = i["Name"]
    dept = i["department"]
    fon = i["phone"]
    print(f"{name} in {dept} can be reached at {fon}.")
    
