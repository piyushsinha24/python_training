p1={'name':'Virat Kohli', 'role':'bat', 'runs':112, 'fours':10, 'sixes':0,
'balls':119, 'field':0}
p2={'name':'du Plessis', 'role':'bat', 'runs':120, 'fours':11, 'sixes':2,
'balls':112, 'field':0}
p3={'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10,
'runs':71, 'field':1}
p4={'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10,
'runs':45, 'field':0}
p5={'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34,
'field':0}
import assign3
point1=assign3.batting(**p1)
point2=assign3.batting(**p2)
point3=assign3.bowling(**p3)
point4=assign3.bowling(**p4)
point5=assign3.bowling(**p5)
result1={'name':'Virat Kohli','batscore':point1}
result2={'name':'du Plessis','batscore':point2}
result3={'name':'Bhuvneshwar Kumar','bowlscore':point3}
result4={'name':'Yuzvendra Chahal','bowlscore':point4}
result5={'name':'Kuldeep Yadav','bowlscore':point5}
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)



