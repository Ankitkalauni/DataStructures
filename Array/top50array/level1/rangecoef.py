'''
Range and Coefficient of range of Array

Range = Max – Min
Coefficient of Range = (Max – Min) / (Max + Min)
'''                
def coeflist(arr):
    maxx = max(arr)
    minn = min(arr)
    
    rangeis = maxx-minn
    cof = (maxx-minn)/(maxx+minn)
    
    print('Range:', rangeis,'\n','Coefficient of Range:', cof)

