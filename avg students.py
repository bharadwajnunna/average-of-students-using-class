#Use Classes: #Find the avg marks of each student.

class AvgMarks:
    print("Avg Marks of each student : ")
    def average(self,i,students):
        [print("{}\t\t{}\t-->{}".format(j['name'],sum(i)/len(i),sum(i)//len(i))) for j in students if i==j['marks']]

students=[{'name': "John",'rollno': 1234,'marks': [45, 67, 78]},
          {'name': "Michael",'rollno': 12345,'marks': [67, 67, 78]},
          {'name': "Alexis",'rollno': 1234456,'marks': [67, 55, 88]}
          ]
st=AvgMarks()
[st.average(i,students) for i in [i['marks'] for i in students]]    #using list comprehensive