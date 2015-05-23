#THE ADVENTURE GAME

#the menu function

def menu(list, question):
  for entry in list:
    print 1 + list.index(entry),
    print ") " + entry

  print len(list) + 1, ") To open the door"

  return input(question) - 1

#Give the computer some basic information about the room:
items = ["por plant", "painting", "vase", "lampshade", "shoe"]

#The key is in the vase (or entry # 2 in the list above):
keylocation = 2

#You haven't found the key:
keyfound = 0

loop = 1

print "Last night you went to sleep in the comfort of your own home"

print "Now, you find yourself locked in a room. You don't know how"
print "you got there, or what time it is. In the room you can see"
print len(items), "things:"
for x in items:
  print x
print ""
print "The door is locked. Could there be a key somewhere?"

while loop == 1:
  choice = menu(items, "What do you want to inspect? ")
  if choice == len(items):
    if keyfound == 1:
      loop = 0
      print "You put in the key, turn it, and hear it click."
      print ""
    else:
      print "The door is locked, you need to find a key."
      print ""
  elif choice == keylocation:
    print "You found a small key in the", items[choice]
    print ""
    keyfound = 1
  elif choice <= len(items):
    print "You found nothing in the the", items[choice]
    print ""
  else:
    print "Is not a valid option"
    print ""

print "Light floods into the room as \
you open the door to your freedom."