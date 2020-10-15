def death_risk ( risk_param ) :
    """
    Estimating the risk of death from coronavirus.
    """
    for i in range (3) :
        if risk_param [ i ] == 'Y' :
            risk_param [ i ] = 1
        else :
            risk_param [ i ] = 0

    # risk_const: verilen cevaplara göre, ölüm risk katsayıları. Kaynak:WHO
    risk_const = [ (0.01 , 0.85) ,
                   (0.01 , 0.4) ,
                   (0.01 , 0.25) ]
    risk = list ( )
    for i in risk_param :
        risk.append (risk_const [ risk_param.index (i) ] [ i ])

    death_prob = risk [ 0 ]
    for i in risk [ 1 : ] :
        death_prob += (1 - death_prob) * i
    print ('\nYour possibility to die from coronavirus: %s %.2f' % ('%' , death_prob * 100))


age = input ("Are you a cigarette addict older than 75 years old? (Y/N):").upper ( )
chronic = input ("Do you have a severe chronic disease? (Y/N):").upper ( )
immune = input ("Is your immune system too weak? (Y/N):").upper ( )
risk_param = [ age , chronic , immune ]
death_risk (risk_param)
