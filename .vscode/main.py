#This function gets existing username and password from filename.
def getUserData(filename):
    user_data = open(filename, 'r')
    username = []
    password = []
    for line in user_data:
        uname, pword = line.split("\t")
        pword.strip("\n") 
        username.append(uname)
        password.append(pword)        
    return [username, password]
    user_data.close()
#This function checks if the inputted username exists. If it doesn't exist the function returns False    
def exists(username, filename):
    check_exists = username in getUserData(filename)[0]  
    if check_exists == True:
        return True
    else:
        return False
    filename.close()
#This function checks if a user exists by sending it to the function 'exists'
#if a user doesn't exist it allows the user to create a new username and password
def createUser(username, password, filename):
    exists_user = exists(username, filename)
    if exists_user == False:
        create_user = open(filename, 'a')
        create_user.write(username + "\t")
        create_user.write(password + "\n")
        return True
    else:
        return False
    user_data.close()

#This function allows existing users to login, and checks if the appropriate username matches wit the correct password
#If the username and password does not match the function returns false
def login(username, password, filename): 
    exists_user = exists(username, filename)
    #password = password in getUserData(filename)[1]
    if exists_user == True:
        check_username = getUserData(filename)[0].index(username)
        check_password = getUserData(filename)[1][check_username]
        if check_password.strip("\n")==password:
            return True
        else:
            return False
    else:
        return None
    filename.close()    

    
# Testing
def main():

    database = "database.txt"
    while True:
        ans = input("Press [q] to quit, [l] to login, [c] to create an account: ")
        if ans == "q":
            # Break if the user quits
            break
        elif ans == "l":
            # Login if the user types in "l"
            uname = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if login(uname, password, database):
                print("Login sucessful!\n")
            else:
                print("Sorry, login unsucessful :(\n")
        elif ans == "c":
            # Create an account if the user types in c
            uname = input("Please create a username: ")
            password = input("Please create a password: ")
            # Check if username exists
            if createUser(uname, password, database):
                    print("Account creation sucessful for user,",uname,"\n")
            else:
                    print("Sorry,",uname,"is already taken!\n")
        else:
            print("Please enter a valid character")
main()
