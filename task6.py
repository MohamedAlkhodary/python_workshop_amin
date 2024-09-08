# Dictionary from the provided question 6
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check if the person dictionary has the skills key, and print the middle skill
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]  # Find the middle skill
    print("Middle skill:", middle_skill)

# 2. Check if the person has the 'Python' skill and print the result
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

# 3. Classify the person based on their skills
if 'skills' in person:
    skills = person['skills']
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print("she is a front end developer")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("she is a backend developer")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("she is a fullstack developer")
    else:
        print("Unknown title")

# 4. Print personal information if the person is married and lives in Finland
if person.get('is_marred') and person.get('country') == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} lives in Finland. she is married.")