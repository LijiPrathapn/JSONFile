import json
myjsonfile=open('C:\\Users\\lijin\\PycharmProjects\\JSONFile\\Jsondata\\details.json','r')
jsondata=myjsonfile.read()
obj=json.loads(jsondata)
print("1.The Value of Username",str(obj['username']))
print("2.The Value of session id are: ",str(obj['sessionId']))

a=str(obj['sessionId'])
print("3.The last value of SessionId is : ",a[-3:-1])

list=obj['students']

for j in range(len(list)):
    if j==1:
        print("\n","7.Marks of Second Student ",list[j].get("marks"))
        my=' The Contact Value of second student',list[1]['contact']
        print("8.a The Contact Value of first student", list[0]['contact'])
        print("8.b The Contact Value of second student", list[1]['contact'])
        print("9.The Second contact value of second student",my[1][1])

    elif j==0:
        print("4 The Address of first student",list[j].get("address"))
        new = list[j].get("address")
        print("5 The Cities of Second Students ")
        for value in new:
            print(value['city'])

        print("6.The Second state value of first student:")
        for valuea in new:
            print(valuea['state'][1],end="")




















