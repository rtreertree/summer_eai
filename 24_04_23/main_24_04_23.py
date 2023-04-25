student_ids, student_name = ["022207", "022204", "022191", "025939", "026046"], ["Year", "Mj", "DD", "MioJo", "Poon"]
print("Name\t ID")
for id ,name in zip(student_ids,student_name):
    print(id,"\t",name)

indexs = [0, -1, -4, 3]
print("Name\t ID")
for index in indexs:
    print(student_ids[index],"\t",student_name[index])
    
#OUTPUT
"""
Name     ID
022207   Year
022204   Mj
022191   DD
025939   MioJo
026046   Poon
"""