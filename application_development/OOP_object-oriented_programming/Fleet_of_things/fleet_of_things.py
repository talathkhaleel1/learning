from fleet import Fleet # from which folder(s), basically the path has to be mentioned and
# then import which Class
from thing import Thing

fleet = Fleet()
fleet.add("Get milk")
fleet.add("Remove the obstacles")

fleet = Thing("Stand up")
fleet.complete()
fleet = Thing("Eat lunch")
fleet.complete()




print(fleet)