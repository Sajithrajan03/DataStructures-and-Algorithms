def is_safe(person, invited, enemies):
    return not any(enemy in invited for enemy in enemies[person])

def invite_friends(friends, enemies):
    sorted_friends = sorted(friends, key=lambda x: len(enemies[x]), reverse=True)

    invited = set()

    for person in sorted_friends:
        if is_safe(person, invited, enemies):
            invited.add(person)

    return invited

# Example Usage
friends = ['Sajith', 'Ananya', 'Praveen', 'Karthick']
enemies = {
    'Sajith': {'Ananya', 'Praveen'},
    'Ananya': {'Sajith', 'Karthick'},
    'Praveen': {'Sajith', 'Karthick'},
    'Karthick': {'Ananya', 'Praveen'}
}

invited_friends = invite_friends(friends, enemies)
print("Invited Friends:", invited_friends)
