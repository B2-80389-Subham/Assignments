people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}
print(f"A. Number of students in the list: {len(people)}")

if 'Lisa' in people:
    people['Lisa'] = 'Green'
    print("B. Lisa's favourite colour has been changed.")

if 'Jenny' in people:
    del people['Jenny']
    print("C. Jenny and her favourite colour have been removed.")


sorted_people = dict(sorted(people.items()))
print("D. Students and their favourite colours sorted alphabetically:")
for name, color in sorted_people.items():
    print(f"{name}: {color}")
