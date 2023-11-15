from scales import Scales

balanca = Scales(d_out=3, pd_sck=2)
balanca.tare()
while(1):
    balanca.measure_weight()
    balanca.measure_force()

    
    print('{:.3f} kg ---- {:.3f} N '.format(balanca.weight, balanca.force))
    

    #print('{:.1f}'.format(28.899))