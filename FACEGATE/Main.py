def student_grade():

    student = int(input(f"Enter number of student: "))
    subject = int(input(f"Enter number of subject offered: "))

    print("Saving >>>>>>>>>>>>>>>>>>>>>>")
    print("Saved Succesfully")

    scores = [[0] * subject for _ in range(student)]

    for count in range(student):
        print(f"Student{count + 1}")

    for index in range(student):
        while True:
            input_scores = int(input(f"Enter score for subject {count + 1}: "))
            if input_scores >= 0 and input_scores <= 100:
                break
            else:
                print("Invalid score input.")

        scores[index][count] = input_scores
        print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Saved Successfully")

    total = []

    for count in range(student):
        total_sum = sum(scores[count])
        total.append(total_sum)

    studentPosition = [1] * student

    for count in range(student):
        for index in range(student):
            if total[index] > total[count]:
                studentPosition[count] += 1

    print("=================== STUDENT GRADE ===================")

    for count in range(student):
        average = total[count] / subject

        print("Student{count + 1}")

        for index in range(subject):
            print(f"Subject {index + 1}: {scores[count][index]}")

        print("Total:", total[count])
        print("Average:", average)
        print("Position:", studentPosition[count])
student_grade()

