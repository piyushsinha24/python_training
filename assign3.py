def batting(name,role,runs,fours,sixes,balls,field):
    run=runs
    four=fours
    six=sixes
    ball=balls
    fielding=field
    points=0
    sr=float(run)/float(ball)*100
    points=run/2
    if run>=50 and run<100:
        points=points+5
    if run>=100:
        points=points+10
    if sr>=80.0 and sr<=100.0:
        points=points+2
    if sr>100:
        points=points+4
    points=points+1*four+2*six+10*field
    return(points)

def bowling(name,role,wkts,overs,runs,field):
    wickets=wkts
    over=overs
    run=runs
    fielding=field
    economy=float(run)/float(over)
    points=0
    points=10*wkts
    if wkts>=3:
        points=points+5
    if wkts>=5:
        points=points+10
    if economy>=3.5 and economy<=4.5:
        points=points+4
    if economy>=2 and economy<=3.5:
        points=points+7
    if economy<2:
        points=points+10
    points=points+10*fielding
    return(points)

        
    
