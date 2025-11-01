def script():
    items = [{'name': 'Sweeta', 'username': 'sweeta', 'country':'India' , 'hobby': 'Music'  , 'affliation':'Student' , 'DNA_seq':'AGCTGCGT'}, 
             {'name': 'Adarsh' , 'username':'Adarsh', 'country':'America' , 'hobby': 'Football', 'affliation':'Student' , 'DNA_seq': 'AGCCCTGG'}, 
             {'name': 'Richard', 'username': 'Richard Agyekum', 'country':'Nigeria' , 'hobby': 'cricket' , 'affliation': 'admin' , 'DNA_seq':'ACCCTCG'}, 
             {'name': 'Karen', 'username':'Karen', 'country':'UAE' , 'hobby':"Book reading"  , 'affliation':'student' , 'DNA_seq':'ACCCTCG'},
             {'name': 'Tanishka', 'username':'tanishka kumar', 'country': 'Ireland' , 'hobby':'Music'  , 'affliation':'student' , 'DNA_seq':'ACCTCGG'}]
    for members in items:
        print(f"name:{members['name']}, slackusername: {members['username']}, country: {members['country']}, hobby: {members['hobby']}, affliation of the member: {members['affliation']}, sequence: {members['DNA_seq']}")
script()
              