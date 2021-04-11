soil_constant2 = 50

def updateRule4(neighbor_states, self_state, neighbor_heights, self_height):
    #print("neighbor states")
    #print(neighbor_states)
    #print("neighbor heights")
    #print(neighbor_heights)
    #print("self state")
    #print(self_state)
    #print("self_height")
    #print(self_height)

    self_water = float(str(self_state))
    global soil_constant2
    neighbor_water = []
    for item in neighbor_states:
        neighbor_water.append(float(str(item)))
    #print(soil_constant2)
    self_water = self_water*(1 - soil_constant2/100)
    if soil_constant2>10:
        soil_constant2 = soil_constant2*4/5
    else:
        soil_constant2 = 3

    for item in range(len(neighbor_states)):
        height = neighbor_heights[item]

        if (   (int(height) + (int(neighbor_water[item])/1200) ) >
             (int(self_height) + ((self_water)/1200))
        ):#and (int(neighbor_water[item])-int(neighbor_water[item]) *.001 >=0)):
            addWater = (neighbor_water[item])*.001 *((int(height)+neighbor_water[item]/1200)-(int(self_height)+self_water/1200))
            self_water+= addWater

            #print("Water added = ")
            #print(addWater)
            #print("neighbor height")
            #print(height)
            #print("neighbor water")
            #print(int(neighbor_water[item]))


        elif ((int(self_height) + ((self_water)/1200)) >
               (int(height) + (int(neighbor_water[item])/1200))
        ):#and (self_water-self_water*.001)>=0):
            subtractWater = self_water*.001 * ((int(self_height)+(self_water/1200))-(int(height)+(neighbor_water[item]/1200)))
            self_water -= subtractWater
            #print("Water subtracted = ")
            #print(subtractWater)
            #print("neighbor height")
            #print(height)
            #print("neighbor water")
            #print(int(neighbor_water[item]))


    if self_water>300:
        self_water=300
    if self_water<0:
        self_water = 0

    #print("FINAL WATER LEVEL")
    #print(self_water)

    return self_water