age = int(input("შეიყვანეთ ასაკი: "))
is_student = input("სტუდენტი ხარ? (დიახ/არა): ") == "დიახ"
if age < 18:
    if is_student:
        print("20% discount")
    else:
        print("10% discount")
else:
    print("Regular price")