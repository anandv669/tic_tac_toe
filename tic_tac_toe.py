user1symbol=input("Choose your symbol between 'x' or 'o'\n>")

while not user1symbol == "x" and not user1symbol == "o":
      user1symbol=input("choose your symbol between 'x' or 'o'only \n>")

if user1symbol == "x":
   user2symbol = "o"
   print("\n\n\n\n         The game has been started\n\nyour opponent is o\n\nchoose the number where you want to place your 'x' or 'o'\n\nFirst goes 'x'\n\n")

elif user1symbol == "o":
     user2symbol = "x" 
     print("\n\n\n\n         The game has been started\n\nyour opponent is x\n\nchoose the number where you want to place your 'x' or 'o'\n\nFirst goes 'x'\n\n")

# print("1 | 2 | 3\n=========\n4 | 5 | 6\n=========\n7 | 8 | 9")

# O="oplace"
# X="xplace"
x="user1"
o="user2"
pos1="1"
pos2="2"
pos3="3"
pos4="4"
pos5="5"
pos6="6"
pos7="7"
pos8="8"
pos9="9"


  

  



def tictactoe():
     #x is winner
     if pos1=="x" and pos2=="x" and pos3=="x" :   
        x="wins"
        print("x is winner")
     elif pos4=="x" and pos5=="x" and pos6=="x" :   
        x="wins"
        print("x is winner")
     elif pos7=="x" and pos8=="x" and pos9=="x" :   
        x="wins"
        print("x is winner")
     elif pos1=="x" and pos5=="x" and pos9=="x" :   
        x="wins"
        print("x is winner")
     elif pos3=="x" and pos5=="x" and pos7=="x" :   
        x="wins"  
        print("x is winner")
     elif pos1=="x" and pos4=="x" and pos7=="x" :   
        x="wins"
     elif pos2=="x" and pos5=="x" and pos8=="x" :   
        x="wins"
        print("x is winner")
     elif pos3=="x" and pos6=="x" and pos9=="x" :   
        x="wins"
        print("x is winner")
       #o is winner
     elif pos1=="o" and pos2=="o" and pos3=="o" :   
        o="wins"
        print("o is winner")
     elif pos4=="o" and pos5=="o" and pos6=="o" :   
        o="wins"
        print("o is winner")
     elif pos7=="o" and pos8=="o" and pos9=="o" :   
        o="wins"
        print("o is winner")
     elif pos1=="o" and pos5=="o" and pos9=="o" :   
        o="wins"
        print("o is winner")
     elif pos3=="o" and pos5=="o" and pos7=="o" :   
        o="wins"
        print("o is winner")
     elif pos1=="o" and pos4=="o" and pos7=="o" :   
        o="wins"
        print("o is winner")
     elif pos2=="o" and pos5=="o" and pos8=="o" :   
        o="wins"
        print("o is winner")
     elif pos3=="o" and pos6=="o" and pos9=="o" :   
        o="wins"
        print("o is winner")
       



print(f"{pos1} | {pos2} | {pos3}\n=========\n{pos4} | {pos5} | {pos6}\n=========\n{pos7} | {pos8} | {pos9}")


x1=input('->')
while x1 not in ["1","2","3","4","5","6","7","8","9"]:
      x1=input("invalid option ->")
    
# if x1 == ["1","2","3","4","5","6","7","8","9"]:
#    [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9]="x"
if x1 == "1":
  pos1="x"
elif x1=="2":
  pos2="x"
elif x1=="3":
  pos3="x" 
elif x1=="4":
  pos4="x" 
elif x1=="5":
  pos5="x" 
elif x1=="6":
  pos6="x" 
elif x1=="7":
  pos7="x" 
elif x1=="8":
  pos8="x" 
elif x1=="9":
  pos9="x" 

print(f"{pos1} | {pos2} | {pos3}\n=========\n{pos4} | {pos5} | {pos6}\n=========\n{pos7} | {pos8} | {pos9}")

o1=input('->')
while o1 not in ["1","2","3","4","5","6","7","8","9"] or o1 == x1:
      o1=input("invalid option ->")

if o1 == "1":
  pos1="o"
elif o1=="2":
  pos2="o"
elif o1=="3":
  pos3="o" 
elif o1=="4":
  pos4="o" 
elif o1=="5":
  pos5="o" 
elif o1=="6":
  pos6="o" 
elif o1=="7":
  pos7="o" 
elif o1=="8":
  pos8="o" 
elif o1=="9":
  pos9="o" 


print(f"{pos1} | {pos2} | {pos3}\n=========\n{pos4} | {pos5} | {pos6}\n=========\n{pos7} | {pos8} | {pos9}")


x2=input('->')
while x2 not in ["1","2","3","4","5","6","7","8","9"] or x2 in [o1,x1]:
      x2=input("invalid option ->")

if x2 == "1":
  pos1="x"
elif x2=="2":
  pos2="x"
elif x2=="3":
  pos3="x" 
elif x2=="4":
  pos4="x" 
elif x2=="5":
  pos5="x" 
elif x2=="6":
  pos6="x" 
elif x2=="7":
  pos7="x" 
elif x2=="8":
  pos8="x" 
elif x2=="9":
  pos9="x" 

print(f"{pos1} | {pos2} | {pos3}\n=========\n{pos4} | {pos5} | {pos6}\n=========\n{pos7} | {pos8} | {pos9}")

o2=input('->')
while o2 not in ["1","2","3","4","5","6","7","8","9"] or o2 in [o1,x1,x2]:
      o2=input("invalid option ->")

if o2 == "1":
  pos1="o"
elif o2=="2":
  pos2="o"
elif o2=="3":
  pos3="o" 
elif o2=="4":
  pos4="o" 
elif o2=="5":
  pos5="o" 
elif o2=="6":
  pos6="o" 
elif o2=="7":
  pos7="o" 
elif o2=="8":
  pos8="o" 
elif o2=="9":
  pos9="o" 

print(f"{pos1} | {pos2} | {pos3}\n=========\n{pos4} | {pos5} | {pos6}\n=========\n{pos7} | {pos8} | {pos9}")



x3=input('->')
while x3 not in ["1","2","3","4","5","6","7","8","9"] or x3 in [o1,x1,o2,x2]:
      x3=input("invalid option ->")

if x3 == "1":
  pos1="x"
elif x3=="2":
  pos2="x"
elif x3=="3":
  pos3="x" 
elif x3=="4":
  pos4="x" 
elif x3=="5":
  pos5="x" 
elif x3=="6":
  pos6="x" 
elif x3=="7":
  pos7="x" 
elif x3=="8":
  pos8="x" 
elif x3=="9":
  pos9="x" 

print(f"{pos1} | {pos2} | {pos3}\n=========\n{pos4} | {pos5} | {pos6}\n=========\n{pos7} | {pos8} | {pos9}")





if pos1=="x" and pos2=="x" and pos3=="x" :   
  x="wins"
  print("x is winner")
elif pos4=="x" and pos5=="x" and pos6=="x" :   
  x="wins"
  print("x is winner")
elif pos7=="x" and pos8=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
elif pos1=="x" and pos5=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
elif pos3=="x" and pos5=="x" and pos7=="x" :   
  x="wins"  
  print("x is winner")
elif pos1=="x" and pos4=="x" and pos7=="x" :   
  x="wins"
elif pos2=="x" and pos5=="x" and pos8=="x" :   
  x="wins"
  print("x is winner")
elif pos3=="x" and pos6=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
 #o is winner
elif pos1=="o" and pos2=="o" and pos3=="o" :   
  o="wins"
  print("o is winner")
elif pos4=="o" and pos5=="o" and pos6=="o" :   
  o="wins"
  print("o is winner")
elif pos7=="o" and pos8=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")
elif pos1=="o" and pos5=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")
elif pos3=="o" and pos5=="o" and pos7=="o" :   
  o="wins"
  print("o is winner")
elif pos1=="o" and pos4=="o" and pos7=="o" :   
  o="wins"
  print("o is winner")
elif pos2=="o" and pos5=="o" and pos8=="o" :   
  o="wins"
  print("o is winner")
elif pos3=="o" and pos6=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")



       
o3=input('->')
while o3 not in ["1","2","3","4","5","6","7","8","9"] or o3 in [o1,x1,x2,o2,x3]:
      o3=input("invalid option ->")

if o3 == "1":
  pos1="o"
elif o3=="2":
  pos2="o"
elif o3=="3":
  pos3="o" 
elif o3=="4":
  pos4="o" 
elif o3=="5":
  pos5="o" 
elif o3=="6":
  pos6="o" 
elif o3=="7":
  pos7="o" 
elif o3=="8":
  pos8="o" 
elif o3=="9":
  pos9="o" 

print(f"{pos1} | {pos2} | {pos3}\n=========\n{pos4} | {pos5} | {pos6}\n=========\n{pos7} | {pos8} | {pos9}")






if pos1=="x" and pos2=="x" and pos3=="x" :   
  x="wins"
  print("x is winner")
elif pos4=="x" and pos5=="x" and pos6=="x" :   
  x="wins"
  print("x is winner")
elif pos7=="x" and pos8=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
elif pos1=="x" and pos5=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
elif pos3=="x" and pos5=="x" and pos7=="x" :   
  x="wins"  
  print("x is winner")
elif pos1=="x" and pos4=="x" and pos7=="x" :   
  x="wins"
elif pos2=="x" and pos5=="x" and pos8=="x" :   
  x="wins"
  print("x is winner")
elif pos3=="x" and pos6=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
 #o is winner
elif pos1=="o" and pos2=="o" and pos3=="o" :   
  o="wins"
  print("o is winner")
elif pos4=="o" and pos5=="o" and pos6=="o" :   
  o="wins"
  print("o is winner")
elif pos7=="o" and pos8=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")
elif pos1=="o" and pos5=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")
elif pos3=="o" and pos5=="o" and pos7=="o" :   
  o="wins"
  print("o is winner")
elif pos1=="o" and pos4=="o" and pos7=="o" :   
  o="wins"
  print("o is winner")
elif pos2=="o" and pos5=="o" and pos8=="o" :   
  o="wins"
  print("o is winner")
elif pos3=="o" and pos6=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")



       
x4=input('->')
while x4 not in ["1","2","3","4","5","6","7","8","9"] or x4 in [o1,x1,o2,x2,x3,o3]:
      x4=input("invalid option ->")

if x4 == "1":
  pos1="x"
elif x4=="2":
  pos2="x"
elif x4=="3":
  pos3="x" 
elif x4=="4":
  pos4="x" 
elif x4=="5":
  pos5="x" 
elif x4=="6":
  pos6="x" 
elif x4=="7":
  pos7="x" 
elif x4=="8":
  pos8="x" 
elif x4=="9":
  pos9="x" 

print(f"{pos1} | {pos2} | {pos3}\n=========\n{pos4} | {pos5} | {pos6}\n=========\n{pos7} | {pos8} | {pos9}")





if pos1=="x" and pos2=="x" and pos3=="x" :   
  x="wins"
  print("x is winner")
elif pos4=="x" and pos5=="x" and pos6=="x" :   
  x="wins"
  print("x is winner")
elif pos7=="x" and pos8=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
elif pos1=="x" and pos5=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
elif pos3=="x" and pos5=="x" and pos7=="x" :   
  x="wins"  
  print("x is winner")
elif pos1=="x" and pos4=="x" and pos7=="x" :   
  x="wins"
elif pos2=="x" and pos5=="x" and pos8=="x" :   
  x="wins"
  print("x is winner")
elif pos3=="x" and pos6=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
 #o is winner
elif pos1=="o" and pos2=="o" and pos3=="o" :   
  o="wins"
  print("o is winner")
elif pos4=="o" and pos5=="o" and pos6=="o" :   
  o="wins"
  print("o is winner")
elif pos7=="o" and pos8=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")
elif pos1=="o" and pos5=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")
elif pos3=="o" and pos5=="o" and pos7=="o" :   
  o="wins"
  print("o is winner")
elif pos1=="o" and pos4=="o" and pos7=="o" :   
  o="wins"
  print("o is winner")
elif pos2=="o" and pos5=="o" and pos8=="o" :   
  o="wins"
  print("o is winner")
elif pos3=="o" and pos6=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")



       

o4=input('->')
while o4 not in ["1","2","3","4","5","6","7","8","9"] or o4 in [o1,x1,x2,o2,x3,o3,x4]:
      o4=input("invalid option ->")

if o4 == "1":
  pos1="o"
elif o4=="2":
  pos2="o"
elif o4=="3":
  pos3="o" 
elif o4=="4":
  pos4="o" 
elif o4=="5":
  pos5="o" 
elif o4=="6":
  pos6="o" 
elif o4=="7":
  pos7="o" 
elif o4=="8":
  pos8="o" 
elif o4=="9":
  pos9="o" 

print(f"{pos1} | {pos2} | {pos3}\n=========\n{pos4} | {pos5} | {pos6}\n=========\n{pos7} | {pos8} | {pos9}")






if pos1=="x" and pos2=="x" and pos3=="x" :   
  x="wins"
  print("x is winner")
elif pos4=="x" and pos5=="x" and pos6=="x" :   
  x="wins"
  print("x is winner")
elif pos7=="x" and pos8=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
elif pos1=="x" and pos5=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
elif pos3=="x" and pos5=="x" and pos7=="x" :   
  x="wins"  
  print("x is winner")
elif pos1=="x" and pos4=="x" and pos7=="x" :   
  x="wins"
elif pos2=="x" and pos5=="x" and pos8=="x" :   
  x="wins"
  print("x is winner")
elif pos3=="x" and pos6=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
 #o is winner
elif pos1=="o" and pos2=="o" and pos3=="o" :   
  o="wins"
  print("o is winner")
elif pos4=="o" and pos5=="o" and pos6=="o" :   
  o="wins"
  print("o is winner")
elif pos7=="o" and pos8=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")
elif pos1=="o" and pos5=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")
elif pos3=="o" and pos5=="o" and pos7=="o" :   
  o="wins"
  print("o is winner")
elif pos1=="o" and pos4=="o" and pos7=="o" :   
  o="wins"
  print("o is winner")
elif pos2=="o" and pos5=="o" and pos8=="o" :   
  o="wins"
  print("o is winner")
elif pos3=="o" and pos6=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")



       

x5=input('->')
while x5 not in ["1","2","3","4","5","6","7","8","9"] or x5 in [o1,x1,o2,x2,x3,o3,x4,o4]:
      x5=input("invalid option ->")

if x5 == "1":
  pos1="x"
elif x5=="2":
  pos2="x"
elif x5=="3":
  pos3="x" 
elif x5=="4":
  pos4="x" 
elif x5=="5":
  pos5="x" 
elif x5=="6":
  pos6="x" 
elif x5=="7":
  pos7="x" 
elif x5=="8":
  pos8="x" 
elif x5=="9":
  pos9="x" 

print(f"{pos1} | {pos2} | {pos3}\n=========\n{pos4} | {pos5} | {pos6}\n=========\n{pos7} | {pos8} | {pos9}")





if pos1=="x" and pos2=="x" and pos3=="x" :   
  x="wins"
  print("x is winner")
elif pos4=="x" and pos5=="x" and pos6=="x" :   
  x="wins"
  print("x is winner")
elif pos7=="x" and pos8=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
elif pos1=="x" and pos5=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
elif pos3=="x" and pos5=="x" and pos7=="x" :   
  x="wins"  
  print("x is winner")
elif pos1=="x" and pos4=="x" and pos7=="x" :   
  x="wins"
elif pos2=="x" and pos5=="x" and pos8=="x" :   
  x="wins"
  print("x is winner")
elif pos3=="x" and pos6=="x" and pos9=="x" :   
  x="wins"
  print("x is winner")
 #o is winner
elif pos1=="o" and pos2=="o" and pos3=="o" :   
  o="wins"
  print("o is winner")
elif pos4=="o" and pos5=="o" and pos6=="o" :   
  o="wins"
  print("o is winner")
elif pos7=="o" and pos8=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")
elif pos1=="o" and pos5=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")
elif pos3=="o" and pos5=="o" and pos7=="o" :   
  o="wins"
  print("o is winner")
elif pos1=="o" and pos4=="o" and pos7=="o" :   
  o="wins"
  print("o is winner")
elif pos2=="o" and pos5=="o" and pos8=="o" :   
  o="wins"
  print("o is winner")
elif pos3=="o" and pos6=="o" and pos9=="o" :   
  o="wins"
  print("o is winner")



       