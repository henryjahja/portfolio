some_list = [1,2,3,'1','2','3',{'x':7},(1,2,3),{1,2,3}]
print('Here is the list ', *some_list,'\nOr maybe this',*some_list, sep='\n')