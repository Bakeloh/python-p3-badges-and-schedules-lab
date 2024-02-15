def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badge_message = f"Hello, my name is {name}."
        badges.append(badge_message)
    return badges

def assign_rooms(names):
    speaker = []
    for i, name in enumerate(names, start=1):
        room_assignment = f"Hello, {name}! You'll be assigned to room {i}!"
        speaker.append(room_assignment)
    return speaker

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)

# Example usage:
printer(["Arel", "Carol"])
