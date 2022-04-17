from flask import request ,jsonify,Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import  create_access_token,jwt_required,get_jwt_identity,jwt_manager
from stackover.models import Users,new_lists



auth = Blueprint('auth', __name__, url_prefix='/auth')
#Opening a cursor to perform database operations


auth.route('/', methods= ['POST'])
def register():
  
  if request.method == "POST":
        name = request.json["name"]
        email = request.json["email"]
        address = request.json["address"]
        password = request.json["password"]
      
        
        
        
        #checking if email exists
        for new_list in new_lists:
              if new_list['email'] == email:
                      return jsonify({'error':'Email  already exists!'})
        
    
          
         #checking if name exists
      
        for new_list in new_lists:
              if new_list['name'] == name:
                     
                      return jsonify({'error':'name already in use!'})      
          
      
        #creating a hashed password in the database
        hashed_password = generate_password_hash(password,method="sha256")
        
        #inserting values
        #Users.add()
        return jsonify({'name':name,'email':email,'address':address,'password':hashed_password})
  return jsonify({'error':'provide the right data'}) 









# auth.route('/login', methods= ['POST','GET'])

# def login():
      
#           email = request.json['email']
#           password = request.json['password']
          
#           #checking if cst_email exits
#           cur.execute('SELECT * FROM customers WHERE cst_email = %(cst_email)s',{'cst_email':email})
#           customers = cur.fetchone()
#           if customers:
#                 #checking if cst_password matches the sha password in database
#                 password_check = check_password_hash(customers['cst_password'],password)
#                 print(password_check)
#                 if password_check:
#                       # creating access tokens
#                       access_token = create_access_token(identity=customers['cst_id'], fresh=True)
                      
#                       print(access_token)
                    
                      
                    
#                       flash('You have logged in successfully!','success')
                  
                
#                       return jsonify({'message':" You logged in successfully!",'access_token':access_token,'cst_email':customers['cst_email'],'cst_id':customers['cst_id']})
                
                
#           return jsonify({'error':'customers doesnt exists'})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
















