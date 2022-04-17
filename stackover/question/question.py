

from flask import (Blueprint)
from flask import request ,flash,session,g,jsonify
from werkzeug.security import check_password_hash, generate_password_hash


from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import  create_access_token,jwt_required,get_jwt_identity,jwt_manager
from stackover.models import Question, Users,new_lists
import string, random
    
questions=Blueprint('questions', __name__, url_prefix='/questions')
questions.route('/question', methods= ['POST','GET'])
def question():
  
  if request.method == "POST":
        question_id =  ''.join(random.choice(string.ascii_lowercase) for x in range(4))
        user_name = request.json["user_name"]
        title = request.json["title"]
        body = request.json["body"]
        
      
        
        
        
        #checking if title exists
        for question in questions:
              if question['title'] == title:
                      return jsonify({'error':'Title  already exists!'})
        
    
          
         #checking if body exists
      
        for question in questions:
              if question['body'] == body:
                     
                      return jsonify({'error':'body already in use!'})      
          
      
        
        
        #inserting values
        Question.add(question_id,user_name,title,body)
        
        return jsonify({'question_id':question_id,'user_name':user_name,'title':title,'body':body})
  return jsonify({'error':'provide the right data'}) 




