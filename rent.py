user_list=[]
houses=[]
tenant_request=[]
tenant_response=[]
tenant_history=[]

class user():
    def __init__(self,user_id,user_name,mail_id,password,role):
        self.user_id=user_id
        self.user_name=user_name
        self.mail_id=mail_id
        self.password=password
        self.role=role
        
    def hard_code(self):
        user_list.append(self)
            
    def validation(self,mail_id,password):
        for i in user_list:
            if i.mail_id==mail_id and i.password==password:
                return i
            
class house_listing():
    def __init__(self,house_id,monthly_rent,location,BHK,size,max_members,amenties,owner_id):
        self.house_id=house_id
        self.monthly_rent=monthly_rent
        self.location=location
        self.BHK=BHK
        self.size=size
        self.max_members=max_members
        self.amenties=amenties
        self.owner_id=owner_id

    def hard_code(self):
        houses.append(self)

class show_details():
    def show_house(self):
        if houses==[]:
            print('sorry there is no available houses')
        else:
            print('___________________Available houses__________________________')
            for i in houses:
                print('house_id :',i.house_id)
                print('monthly_rent:',i.monthly_rent)
                print('location :',i.location)
                print('BHK :',i.BHK)
                print('size :',i.size)
                print('max_members :',i.max_members)
                print('amenties :',i.amenties)
                print('---------------------------------------------------------------')
            
class tenant(user):
    
    def __init(self,user_id,user_name,mail_id,password,role):
        super().__init__(self,user_id,user_name,mail_id,password,role)
    def welcome(self):
        print("good to see you tenant",self.user_name)
    def choose_house(self):
        while True:
            print('enter your choise')
            print('1.show available list of houses\n2.place a request\n3.see the response for your request\n4.show the history\n5.logout')
            choise=int(input('enter your choise:'))
            if choise==1:
                h1=show_details()
                h1.show_house()
                
            elif choise==2:
                id=input('enter the house id for which you want to place request')
                for i in houses:
                    if i.house_id==id:
                        detail={'request_id':len(tenant_request),'house_id':i.house_id,'owner_id':i.owner_id,'tenant_name':self.user_name,'tenant_id':self.user_id,'request_status':'null','requested_date':'20-05-2023'}
                        tenant_request.append(detail)
                        #tenant_history.append(detail)
                        print('your request placed succesfully')
                        
            elif choise==3:
                cost=0
                for i in tenant_response:
                    if i.tenant_id==self.user_id:
                        if i.request_status=='accepted':
                            for k in houses:
                                if k.house_id==i.house_id:
                                    cost=k.monthly_rent
                            print('your response has been accepted by the owner')
                            print('***************** your advance amount ',cost,'************************')
                            print()
                            print('____________________available payment methods___________________')
                            print('1.card\n2.cash\n3.online payment')
                            n=int(input('enter your choise:'))
                            
                            if n==1:
                                card_no=input('enter your card no:')
                                cvv_no=input('enter your cvv number:')
                                card_holder_name=input('enter card_holder_name: ')
                                print('please conform the three digit OTP which we sent to your mail')
                                print()
                                print('___________________________your payment succesfully done___________________________')
                                
                            elif n==2:
                                print('___________________________your payment succesfully done___________________________')

                            elif n==3:
                                print('please scan the QR code and pay the amount')
                                print('___________________________your payment succesfully done___________________________')
                                
                        elif i.request_status=='rejected':
                            print('sorry your request has been rejected by the owner')
                        elif i.request_status=='null':
                            print('the owner yet not seen your request')
                            
            elif choise==4:
                temp=tenant_history[::]
                if temp==[]:
                    print('your history is empty')
                else:
                    while True:
                        i=temp.pop() #stack
                        if i['tenant_id']==self.user_id:
                            print('request_id:',i['request_id'],'\nhouse_id:',i['house_id'],'\nowner_name:',self.user_name,'\ntenant_id:',i['tenant_id'],'\nrequest_status:',i['request_status'],'\nrequested_date:',i['requested_date'],'\nresponse_date:',i['response_date'])
                            break                
            elif choise==5:
                print('succesfully logedout')
                break
                    
                         
class owner(user):
    def __init(self,user_id,user_name,mail_id,password,role):
        super().__init__(self,user_id,user_name,mail_id,password,role)
        
    def welcome(self):
        print("good to see you owner",self.user_name)
        
    def choise_request(self):
        in_process=True
        while in_process:
            print('------------available choise------------------')
            print('1.show available list of houses\n2.add/delete a new house\n3.accept/reject the request of tenant\n4.show the hisory\n5.logout')
            choise=int(input('enter your choise from the abouve list: '))
            
            if choise==1:
                h2=show_details()
                h2.show_house()
                
            elif choise==2:
                print('10.add the house \n11.delete the house')
                ad=int(input('enter your choise:'))
                if ad==10:
                    print('please enter your house details to the approval process')
                    self.house_id=len(houses)+1
                    self.owner_id=len(user_list)+1
                    self.location=input('enter your house location:')
                    self.BHK=input('enter your BHK details:')
                    self.size=input('house square feet details:')
                    self.max_members=input('maximum how many members are allowed:')
                    self.amenties=input('enter your house amenties:')
                    houses.append(self)
                    print("------------your house has been succefully added---------------------")
                    print()
                    
                elif ad==11:
                    del_house_id=input('enter the house_id you want to delete: ')
                    for i in houses:
                        if i.house_id==del_house_id:
                            houses.remove(i)
                            print(del_house_id,' has been removed succesfully ')
                else:
                    print('enter the valid choise')
                
            elif choise==3:                
                for i in tenant_request:
                    if i.owner_id==self.user_id:
                        print('you got an request from',i.tenant_id)
                        state=input('do you want to accept the request Y/N :')
                        if state=='Y':
                            i.request_status='accepted'
                            for j in houses:
                                if j.house_id==i.house_id:
                                    houses.remove(j)
                            print('request is succesfully accepted')
                        elif state=='N':
                            i.request_status='rejected'
                            print('request is rejected')
                        details={'request_id':i.request_id,'house_id':i.house_id,'owner_id':i.owner_id,'owner_name':self.user_name,'tenant_id':i.tenant_id,'request_status':i.request_status,'requested_date':i.requested_date,'response_date':i.response_date}
                        tenant_response.append(details)
                        tenant_request.remove(i)
                        tenant_history.append(details)
                        
            elif choise==4:
                temp=tenant_history[::]
                if temp==[]:
                    print('your history is empty')
                else:
                    while True:
                        i=temp.pop() #stack
                        if i['owner_id']==self.user_id:
                            print('request_id:',i['request_id'],'\nhouse_id:',i['house_id'],'\nowner_name:',self.user_name,'\ntenant_id:',i['tenant_id'],'\nrequest_status:',i['request_status'],'\nrequested_date:',i['requested_date'],'\nresponse_date:',i['response_date'])
                            break
                    
            elif choise==5:
                print('your succesfully loged out')
                in_process=False


class admin(user):
    def __init(self,user_id,user_name,mail_id,password,role):
        super().__init__(user_id,user_name,mail_id,password,role)
    def welcome(self):
        print("good to see you admin",self.user_name)

        
class tenant_request_hard():
    def __init__(self,request_id,house_id,owner_id,tenant_id,request_status,requested_date,response_date):
        self.request_id=request_id
        self.house_id=house_id
        self.owner_id=owner_id
        self.tenant_id=tenant_id
        self.request_status=request_status
        self.requested_date=requested_date
        self.response_date=response_date
        tenant_request.append(self)
        
class tenant_response_hard():
    def __init__(self,request_id,house_id,owner_id,tenant_id,request_status,requested_date,response_date):
        self.request_id=request_id
        self.house_id=house_id
        self.owner_id=owner_id
        self.tenant_id=tenant_id
        self.request_status=request_status
        self.requested_date=requested_date
        self.response_date=response_date
        tenant_response.append(self)
        
class tenant_history_hard():
    def __init__(self,request_id,house_id,owner_name,tenant_id,request_status,requested_date,response_date):
        tenant_history.append({'request_id':request_id,'house_id':house_id,'owner_name':owner_name,'tenant_id':tenant_id,'request_status':request_status,'requested_date':requested_date,'response_date':response_date})

        
if __name__ == "__main__":
    
    from datetime import datetime
    import time
    date_time=datetime.now()
    now=list(str(date_time).split(" "))
    
    app=user('@t1','birundha','brut@gmail.com','bru@18','tenant')
    app.hard_code()
    app=user('@o1','bru','bruo@gmail.com','bru@18','owner')
    app.hard_code()
    ha1=house_listing('@h1','2000','chennai','1BHK','167 square feet',3,'fridge','@o1')
    ha1.hard_code()
    ha1=house_listing('@h2','5000','chennai','3BHK','300 square feet',6,'fridge','@o2')
    ha1.hard_code()
    ha2=tenant_request_hard('@r1','@h1','@o1','@t1','null',now[0],now[0])
    ha3=tenant_response_hard('@r1','@h1','@o1','@t1','accepted',now[0],now[0])
    ha4=tenant_history_hard('@r1','@h1','bru','@t1','accepted',now[0],now[0])

    valid=app.validation('bruo@gmail.com','bru@18')
    if valid:
        print("succesfully loged in")
        if valid.role=='admin':
            main=admin(valid.user_id,valid.user_name,valid.mail_id,valid.password,valid.role)
            main.welcome()
            main.view_response()
        elif valid.role=='owner':
            main=owner(valid.user_id,valid.user_name,valid.mail_id,valid.password,valid.role)
            main.welcome()
            main.choise_request()
        elif valid.role=='tenant':
            main=tenant(valid.user_id,valid.user_name,valid.mail_id,valid.password,valid.role)
            main.welcome()
            main.choose_house()    
        else:
            print("enter valid mail_id/password")
