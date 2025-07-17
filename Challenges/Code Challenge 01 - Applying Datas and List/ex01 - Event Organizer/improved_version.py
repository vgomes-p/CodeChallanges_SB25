#!/usr/bin/env python3
import os
import time as tm

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def update_event_list(event_list, subject, person):
	if subject not in event_list:
		event_list[subject] = []
	event_list[subject].append(person)

event = {}

nbr_members = int(input("How many register are you making?\n>>> ").strip())

print("Please, informe the name of the member who will attend the event followed by the event\n[eg.: name, event]")
for _ in range(nbr_members):
	add_mbr = input(">>> ")
	name, subject = add_mbr.split(", ")
	update_event_list(event_list=event, subject=subject, person=name)

tm.sleep(2)
clear()
print("These are the list of events updated:\n-------------------------------------")
for subject, people in event.items():
	print(f"{subject}: {', '.join(people)}")