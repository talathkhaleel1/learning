
# queue = [
# 	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
# 	{ 'name': 'Mark', 'alcohol': 0, 'guns': 0 },
# 	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
# 	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
# 	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
# 	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
# 	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
# ]

# Queue of festivalgoers at entry
# no. of alcohol units
# no. of guns

# Create a security_check function that returns a list of festivalgoers \
# who can enter the festival (only the names)

# If guns are found, remove them and put them on the watchlist (only the names),\
# they can not enter the festival
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot)\
# and let them enter the festival

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Mark', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]


watchlist = []
security_alcohol_loot = 0

def security_check(queue):
    can_enter_the_festival = []
    security_alcohol_loot = 0
    for i in range(len(queue)):# unpack dictionary
        festivalgoer = queue[i]  # get the actual dictionary
        # for k,v in festivalgoers.items():
        if festivalgoer["guns"] > 0: # if value of guns is more than 0
            watchlist.append(festivalgoer["name"])# add that name from the dictionary to watchlist
        elif festivalgoer["alcohol"] >= 0: # if value of alcohol is more than 0
            security_alcohol_loot += festivalgoer["alcohol"] # to add the value of alcohol to the loot
            festivalgoer["alcohol"] = 0 # and set alcohol to 0
            can_enter_the_festival.append(festivalgoer["name"])  # add that name from the dictionary to this list
    return  can_enter_the_festival


print(security_check(queue))


# checking values for different keys is an independent check so always check with different if statements

#reference
# https://stackoverflow.com/questions/48243018/concatenate-string-to-the-end-of-all-elements-of-a-list-in-python