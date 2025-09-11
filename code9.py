velocidade = 61
local_carro = 102

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RENGE = 1

velocidade_car_pass_r1 = velocidade == RADAR_1
passou_radar_1 = local_carro >= ( LOCAL_1 - RADAR_RENGE) and local_carro <= (LOCAL_1 + RADAR_RENGE)
carro_multado = passou_radar_1 and velocidade_car_pass_r1

if velocidade_car_pass_r1:
    print('Velocidade dentro do permitido')

if passou_radar_1 :
     print('Carro pasou')

if carro_multado :
     print('Velocidade excedeu o permitido carro será multado!!!')
