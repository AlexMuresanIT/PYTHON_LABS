def cost_calatorie(destinatie,nopti):
    cost_hotel = 140*nopti
    sum = cost_hotel
    if destinatie == "Cluj":
        cost_tren = 183
    elif destinatie == "Timisoara":
        cost_tren = 220
    elif destinatie == "Bucuresti":
        cost_tren=222
    elif destinatie == "Iasi":
        cost_tren = 475

    sum = sum +cost_tren
    masina = 40*(nopti+1)
    sum = sum + masina
    masa = 600
    sum = sum+masa
    return sum

oras = input("In ce oras ai vrea sa calatoresti? ")
print("Costul total al excursiei este: ",cost_calatorie(oras,4))

