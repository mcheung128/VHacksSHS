Hours = 0
Minutes = 0


def hour_tracker():
    global Hours
    global Minutes
    while Hours < 50:
        today1 = int(input('How many hours did you drive today?'))
        while today1 >= 24:
            print("That's bullshit")
            today1 = int(input('How many hours did you drive today?'))
        Hours += today1
        today2 = int(input('How many minutes did you drive today?'))
        Minutes += today2
        if Minutes >= 60:
            Hours += 1
            Minutes -= 60
        print('Today you drove ' + str(today1) + ' hours, and ' + str(today2) + ' minutes.')
    print("In total, you drove " + str(Hours) + ' hours, and ' + str(Minutes) + " minutes.")



hour_tracker()
