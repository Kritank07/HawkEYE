from src.database.config import supabase
import bcrypt

def hash_pass(pwd): # to save the password in hashform in the databse if teacher registers
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed): # if teacher logins then it checks wether he/she has entered a correct password
    return bcrypt.checkpw(pwd.encode(), hashed.encode())
    

def check_teacher_exists(username): 
    # check for uique username, return false is usernmae already exists
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0 # retur true if username is unique else false because len will be 1

def create_teacher(username, password, name):
    data = {"username" : username, "password" : hash_pass(password), "name" : name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data[0]

        if check_pass(password, teacher["password"]):
            return teacher

    return None

def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data

def create_student(new_name, face_embedding = None, voice_embedding = None):
    data = {'name' : new_name, 'face_embedding' : face_embedding, 'voice_embedding' : voice_embedding}
    response = supabase.table('students').insert(data).execute()
    return response.data

def create_subject(sub_code, sub_name, sub_section, teacher_id):
    data = {"subject_code" : sub_code, "name" : sub_name, "section" : sub_section, "teacher_id" : teacher_id}
    response = supabase.table("subjects").insert(data).execute()

    return response.data

def get_teacher_subjects(teacher_id):
    response = supabase.table("subjects").select('*, subject_students(count), attendance_logs(timestamp)').eq("teacher_id", teacher_id).execute()
    subjects = response.data

    for sub in subjects:
        sub['total_students'] = sub.get("subject_students", [{}])[0].get('count', 0) if sub.get("subject_students") else 0

        attendence = sub.get("attendance_logs", [])
        unique_sessions  = len({log['timestamp'] for log in attendence})
        sub['total_classes'] = unique_sessions

        sub.pop('subject_students', None)
        sub.pop('attendance_logs', None)

    return subjects