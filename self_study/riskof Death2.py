def death_risk ( risk_param ) :
    """
    Estimating the risk of death from coronavirus.
    """
    risk = list ( )
    for i in range (3) :
        if risk_param [ i ] == 'Y' :
            risk.append (True)
        else :
            risk.append (False)

    if risk [ 0 ] or risk [ 1 ] or risk [ 2 ] :
        print ("\nThere is a risk of death !!!")
    else :
        print ("\nThere is not a risk of death.")


age = input ("Are you a cigarette addict older than 75 years old? (Y/N):").upper ( )
chronic = input ("Do you have a severe chronic disease? (Y/N):").upper ( )
immune = input ("Is your immune system too weak? (Y/N):").upper ( )
risk_param = [ age , chronic , immune ]
death_risk (risk_param)
