#!/usr/bin/env python

import sys
from icalendar import Calendar

DATE_FORMAT="%c"

def cat_ics(ics):
  cal = Calendar.from_ical(ics)
  for component in cal.walk():
    if component.name == "VEVENT":
      print(component)
      print("Title:     {}".format(component.get("summary")))
      print("From:      {}".format(component.get("dtstart").dt.strftime(DATE_FORMAT)))
      print("To:        {}".format(component.get("dtend").dt.strftime(DATE_FORMAT)))
      organizer = component.get("organizer")
      print("Organizer: {} <{}>".format(organizer.params["CN"], organizer))
      print("Description:\n{}".format(component.get("description")))

if __name__ == "__main__":
  ics = "".join(sys.stdin.readlines())
  cat_ics(ics)
