
new_lists = [] 
questions = [] 
class Users:
    #Defining the model attributes
    def __init__(self, name,email,address,password):
        self.name = name
        self.email = email
        self.address = address
        self.password= password
    
    def json_data(self):
        return self.__dict__
        
     
        
    
     
# Function to  add a new student   
    
    def add(self, name,email,address,password):
        new_student = Users(name,email,address,password)
        new_lists.append( new_student.json_data())
        
        
  
class Question:
        #Defining the model attributes
    def __init__(self,question_id, user_name,title,body):
        self.question_id = question_id
        self.user_name = user_name
        self.title = title
        self.body = body
        
    
    def json_data(self):
        return self.__dict__
        
     
        
    
     
# Function to  add a new question   
    
    def add(self,question_id, user_name,title,body):
        new_question = Question(question_id,user_name,title,body)
        questions.append( new_question.json_data())
           