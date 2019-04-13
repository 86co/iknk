cells=[0 for _ in range(129)]
rule=30

cells[64]=1

exit=0

string=""
for cell in cells:
    string+="■" if cell==1 else " "
enter=input(string)

if enter=="exit": exit=1
if enter.isdigit():
    if 0<=int(enter)<256: rule=int(enter)

while not exit:
    cells_=[]
    cells_[:]=cells[:]
    for i, cell_ in enumerate(cells_):
        if i==len(cells_)-1: 
            u=4*cells_[i-1]+2*cell_+cells_[0]
        else:
            u=4*cells_[i-1]+2*cell_+cells_[i+1]
        cells[i]=(rule//(2**u))%2
    
    string=""
    for cell in cells:
        string+="■" if cell==1 else " "
    enter=input(string)
    if enter=="exit": exit=1
    if enter.isdigit():
        if 0<=int(enter)<256: rule=int(enter)