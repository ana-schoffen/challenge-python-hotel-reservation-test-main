from src.__init__ import Hotel

Lakewood = Hotel(110, 90, 80, 80, 3)
Bridgewood = Hotel(160, 60, 110, 50, 4)
Ridgewood = Hotel(220, 160, 100, 40, 5)


def get_cheapest_hotel(number):  # DO NOT change the function's name
    totalLake = 0
    totalBridge = 0
    totalRidge = 0
    client = number.split()
    if(client[0] == "Regular:"):
        cont = 0
        for x in range(1, 4):

            if(client[x][10:11] == "s"):
                cont += 1
                totalLake = totalLake + Lakewood.weekend
                totalBridge = totalBridge + Bridgewood.weekend
                totalRidge = totalRidge + Ridgewood.weekend
        totalLake = totalLake + Lakewood.weekDay * (3-cont)
        totalBridge = totalBridge + Bridgewood.weekDay * (3-cont)
        totalRidge = totalRidge + Ridgewood.weekDay * (3-cont)
    else:
        cont = 0
        for x in range(1, 4):
            t = client[x].rfind("(")
            if(client[x][t+1:t+2] == "s"):
                cont += 1
                totalLake = totalLake + Lakewood.weekendP
                totalBridge = totalBridge + Bridgewood.weekendP
                totalRidge = totalRidge + Ridgewood.weekendP
        totalLake = totalLake + Lakewood.weekDayP * (3-cont)
        totalBridge = totalBridge + Bridgewood.weekDayP * (3-cont)
        totalRidge = totalRidge + Ridgewood.weekDayP * (3-cont)

    if(totalLake < totalBridge and totalLake < totalRidge):
        cheapest_hotel = "Lakewood"
    elif(totalBridge < totalLake and totalBridge < totalRidge):
        cheapest_hotel = "Bridgewood"
    elif(totalRidge < totalLake and totalRidge < totalBridge):
        cheapest_hotel = "Ridgewood"
    elif(totalLake == totalBridge and totalLake < totalRidge):
        cheapest_hotel = "Bridgewood"
    elif(totalLake == totalRidge and totalLake < totalBridge):
        cheapest_hotel = "Ridgewood"
    elif(totalBridge == totalRidge and totalBridge < totalLake):
        cheapest_hotel = "Ridgewood"
    elif(totalLake == totalBridge and totalLake == totalRidge):
        cheapest_hotel = "Ridgewood"

    return cheapest_hotel
