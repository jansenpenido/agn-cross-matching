# Write your crossmatch function here.
import numpy as np


def angular_dist(r1_deg, d1_deg, r2_deg, d2_deg):

    # Convert coordinates from degrees to radians
    r1 = np.radians(r1_deg)
    d1 = np.radians(d1_deg)
    r2 = np.radians(r2_deg)
    d2 = np.radians(d2_deg)

    a = np.sin(np.abs(d1 - d2) / 2) ** 2
    b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1 - r2) / 2) ** 2

    d = 2 * np.arcsin(np.sqrt(a + b))

    return np.degrees(d)


def hms2dec(hours, minutes, seconds):
    result = 15 * (hours + minutes/60 + seconds/(60*60))
    return result


def dms2dec(degrees, arcminutes, arcseconds):
    if(degrees > 0):
        result = degrees + arcminutes/60 + arcseconds/(60*60)
    else:
        positive_degrees = degrees * -1
        result = -1 * (positive_degrees + arcminutes/60 + arcseconds/(60*60))

    return result


def import_bss():
    # Import file
    cat = np.loadtxt('data/bss.dat', usecols=range(1, 7))
    coordinates = []

    for index, row in enumerate(cat):
        ascention = hms2dec(row[0], row[1], row[2])
        declination = dms2dec(row[3], row[4], row[5])

        coordinates.append((index + 1, ascention, declination))

    return coordinates


def import_super():
    # Import file
    cat = np.loadtxt('data/super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
    coordinates = []

    for index, row in enumerate(cat):
        coordinates.append((index + 1, row[0], row[1]))

    # Add index column
    return coordinates


def find_closest(cat, target_ascention, target_declination):
    nearest_index = None
    nearest_distance = None
    curr_distance = 0

    for index, row in enumerate(cat):
        # Calculate angular distance between each catalog entry and the target
        curr_distance = angular_dist(row[1], row[2], target_ascention, target_declination)

    # Update nearest index and distance accordinly
    if  (nearest_distance == None) or (nearest_distance > curr_distance):
        nearestIndex = index
        nearest_distance = curr_distance

    # Return closest object index and distance
    return(nearest_index, nearest_distance)


# Run crossmatching
def crossmatch(bss_cat, super_cat, max_dist):
    matches = []
    no_matches = []

    # For each entry in the BSS catalog, find the closest match in the SUPER catalog
    for bbs_row in bss_cat:
        closest = find_closest(super_cat, bbs_row[1], bbs_row[2])

        if closest[1] < max_dist:
            matches.append((bbs_row[0], super_cat[closest[0]][0], closest[1]))
        else:
            no_matches.append(bbs_row[0])

    return(matches, no_matches)


if __name__ == '__main__':
    bss_cat = import_bss()
    super_cat = import_super()

    max_dist = 40/3600
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    print(matches[:3])
    print(no_matches[:3])
    print(len(no_matches))

    max_dist = 5/3600
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    print(matches[:3])
    print(no_matches[:3])
    print(len(no_matches))
