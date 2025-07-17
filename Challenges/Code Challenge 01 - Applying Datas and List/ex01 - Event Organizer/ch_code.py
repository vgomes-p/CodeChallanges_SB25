#!/usr/bin/env python3
def update_event_list(event_list, subject, person):
	if subject not in event_list:
		event_list[subject] = []
	event_list[subject].append(person)

event = {}

nbr_members = int(input().strip())

for _ in range(nbr_members):
	add_mbr = input()
	name, subject = add_mbr.split(", ")
	update_event_list(event_list=event, subject=subject, person=name)

for subject, people in event.items():
	print(f"{subject}: {', '.join(people)}")