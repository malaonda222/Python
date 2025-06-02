nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

jessa = nested_student_dict['class']['student']['name'] = "Jessa"
print(f"Dictionary after modifcation: {nested_student_dict}")