Data = {'Hours': 0,
        'Minutes': 0,
        'Night_hours': 0}


def hour_tracker():
    global Data
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current = str(current_time)
    while Data["Hours"] < 50 and Data["Night_hours"] < 10:
        today1 = int(input('How many hours did you drive today?'))
        today2 = int(input('How many minutes did you drive today?'))
        while today1 >= 24:
            print("That's bullshit")
            today1 = int(input('How many hours did you drive today?'))
        if int(current[:2]) >= 20 or int(current[:2]) <= 6:
            Data["Night_hours"] += today1
            Data["Minutes"] += today2
            if Data["Minutes"] >= 60:
                Data["Night_hours"] += 1
                Data["Minutes"] -= 60
            print('Today you drove ' + str(today1) + ' night hours, and ' + str(today2) + ' minutes.')
        else:
            Data["Hours"] += today1
            Data["Minutes"] += today2
            if Data["Minutes"] >= 60:
                Data["Hours"] += 1
                Data["Minutes"] -= 60
            print('Today you drove ' + str(today1) + ' hours, and ' + str(today2) + ' minutes.')

    print(Data)
    print('In all, you drove ' + str(Data['Hours']) + ' hours and ' + str(Data['Minutes']) + ' Minutes with ' + str(Data['Night_hours']) + ' night hours.')

hour_tracker()
