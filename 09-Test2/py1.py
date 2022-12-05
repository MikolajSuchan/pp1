def f(player1,player2):
    sum1=0
    sum2=0
    for i in player1:
        if i=="A" or i=="Q" or i=="K" or i=="J" or i=="T":
            sum1=sum1+10
        else:
            sum1=sum1+int(i)
    for j in player2:
        if j=="A" or j=="Q" or j=="K" or j=="J" or j=="T":
            sum2=sum2+10
        else:
            sum2=sum2+int(j)
    if sum1>sum2:
        return True
    else:
        return False