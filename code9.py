velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RENGE = 1

#confere se o carro excedeu a velocidade 
velo_passa_radar1= velocidade < RADAR_1
#confere se o carro estava no local do radar km 99 a km 101 
passou_car= local_carro >= (LOCAL_1 - RADAR_RENGE) and local_carro<= (LOCAL_1 + RADAR_RENGE)
#confere se carro foi multado 

if passou_car:
     print("Carro passou no radar 1")
     if velo_passa_radar1:
          print("Carro na velocidade correta")
     else:
          print("Carro multado")

