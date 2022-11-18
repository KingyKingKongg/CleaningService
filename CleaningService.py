###KingAlyson CMIS102/6382 Sep/27/2022
###Week 7 Assignment

#This program will determine the cost of yard service or house cleaning or both
#The program also offers a senior discount


import string,datetime


#Define all variables
house = 0
yard = 0

bedroom_price = 80
bedroom = 0
bedroom_total = 0

kitchen_price = 65
kitchen = 0
kitchen_total = 0

bathroom_price = 60
bathroom = 0
bathroom_total = 0

addWin = 0 #dust_window
addBase = 0 #
add_on_window = "None"
add_on_ExtraRoom = "None"



year = ""
month = ""
day = ""
senior_dis = ""
senior_dis_num = 1



shrub_count = 0
user_input_service = ""
lenear_foot = 0
yard_sqft = 0

edging_price = 0
mowing_price = 0
shrub_price = 0
all_service = 0

user_input_sizeLegnth = 0
user_input_sizeWidth = 0

#Inputs the current year for later use
x = datetime.datetime.now()
yearint = int(x.strftime('%Y'))

#Invalid characters
invalid = list(string.ascii_lowercase) + list(string.digits) + list(string.punctuation)
invalid2 = list(string.ascii_letters) + list(string.punctuation)


#Months with Month number and the amount of days the month has
monthcode = {"Jan": ["Jan",31], "Feb": ["Feb",28], "Mar": ["March",31], "Apr": ["Apr",30], "May": ["May",31], "Jun": ["Jun",30],
            "Jul": ["Jul",31], "Aug": ["Aug",31], "Sep": ["Sep",30], "Oct": ["Oct",31], "Nov": ["Nov",30], "Dec": ["Dec",31]}






def Today_date_discount(): #discount and date of cleaning
    global yearint, month, day, monthcode,senior_dis,senior_dis_num

    print("\nPlease choose a date for your services\n")

    
    while True:
        mon = input("\nEnter the Month(first 3 letters): ") #Asks for three letter month
        if mon in string.digits or mon in string.punctuation or len(mon) != 3: #makes sure there is not numbers or punctuation
            print("Please enter first 3 letters of a Month (ie: Mar)")

        else: 
            mon = mon.capitalize() #capitalize the first letter

            try: #possible error to occur if letters do not match the dictionary key
                month = monthcode.get(mon)[0] #pulls the three letters from the dictionary and the first element of the list value
                break

            except:
                print("Please enter first 3 letters of a Month (ie: Mar)\n")



    while True:
        
        day = input("Enter the Day: ") #enter the day and check if its a letter or punctuation
        if day in string.ascii_letters or day in string.punctuation or len(day) > 2:
            print("Please enter number again") 

        day = int(day) #convert to a int

        try: #Checks that your day is not more than the month example, Feb only has 28 days, if you enter 31 it will loop
            if day > 0 and day <= monthcode.get(mon)[1]:
                break

        except: 
            print(f"\nMonth/Day mismatch.\n{mon} has {monthcode.get(mon)[1]} days\nNumbers less than ten should be ONE digit\ninstead of 04, write 4\n\n::")

 
    while True:
        #Senior Discount
        #enter your birth year
        senior_dis = input("\nOur services offer a 15% senior discount\nPlease enter your birth year to see if you qulify (ie: 1993): ")
        
        #checks that it is a digit, not punctuation and the len is 4
        if senior_dis in string.ascii_letters or senior_dis in string.punctuation or len(senior_dis) != 4:
            print("\nPlease enter a 4 digit year (ie: 1993)\n")

        else: #Checks the user age by subtracking the current year
            senior_dis = int(senior_dis)
            user_age = yearint - senior_dis
            
            #Age limits
            if user_age >= 55:
                print("\nYou qualify for the Senior Discount, 15% off your total price")
                senior_dis_num = .15
                senior_dis = "15% off"
                break
            else:
                print("\nYou do not qualify for the Senior Discount")
                senior_dis = "N/A"
                break


#HouseService

def House_Service(): #Will return total cost for house cleaning
    global room_amount, bedroom, bedroom_price, bedroom_total,kitchen,kitchen_price,kitchen_total,typeClean_string, typeClean_price
    global bathroom, bathroom_price, bathroom_total, addWin, addBase,sqFt_input,add_on_ExtraRoom,add_on_window,num_of_rooms,room_type,rooms,rm_price,rm_type



    print("\n\t\tAlyson's Cleaning Service\n")

    #Gets total for House cleaning by adding sqfeet, room Number, room Type, Basement/Window, Cleaning type
    def HouseCleaningTool(num_of_rooms, room_type,winBaseTot,clean_type):
        global room_amount_price #used to change the value of the variables

        
        overallPrice = winBaseTot + clean_type + room_type + num_of_rooms

        return overallPrice


    rooms = eval(input("How many rooms are you getting cleaning?: "))
    
    while True:
        print("\nWhich room are you getting cleaned?") 
        rm_type_list = ["1) Bedroom - $20", "2) Bathroom - $15", "3) Kitchen - $5", "4) Custom - $30"]
        for r in rm_type_list:
            print(r)

        rm_type = eval(input("\n")) 

        if rm_type == 1:
            rm_type = "Bedroom"
            rm_price = 20
            break
        

        elif rm_type == 2:
            rm_type = "Bathroom"
            rm_price = 15
            break
        

        elif rm_type == 3:
            rm_type = "Kitchen"
            rm_price = 5
            break 
        

        elif rm_type == 4:

            rm_type = "Custom"
            rm_price = 25
            break

                

        else:
            print("**Invalid input")
        




    ##Ask heavy or light cleaning
    while True:
        ask_heavy_light = input("\nIs this a heavy or light cleaning(type H or L): ")
        ask_heavy_light = ask_heavy_light.upper()

        if ask_heavy_light == "H":
            
            typeClean_price = 450
            typeClean_string = "Heavy Cleaing"
            break

        elif ask_heavy_light == "L":
            typeClean_price = 250
            typeClean_string = "Light Cleaning"
            break 


        else:
            print("Invalid input, please typ H or L")




    #asks for add ons 

    add_on_window = input("\nWould you like to add window cleaning for $30 more? (Y/N): ")
    add_on_window = add_on_window.upper() #function to make input uppercase

    add_on_ExtraRoom = input("Would you like to add basement or attic cleaning for $150 more?(Y/N): ")
    add_on_ExtraRoom = add_on_ExtraRoom.upper()

    #changes the varibles to add to the total later
    if add_on_window == "Y" and add_on_ExtraRoom == "Y":
        addWin = 30
        addBase = 150
        add_on_window = "$30 charge" 
        add_on_ExtraRoom = "$150 charge"

    elif add_on_window == "Y":
        addWin = 30
        add_on_window = "$30 Charge"

    elif add_on_ExtraRoom == "Y":
        addBase = 150
        add_on_ExtraRoom = "$150 Charge"

    

    window_baseTotal = addWin + addBase




    #returns the calculations made from user input, the Room_Type function is placed within this function to get a total amount

    Overall_Price = HouseCleaningTool(rooms,rm_price,window_baseTotal,typeClean_price)

    return Overall_Price


#Yard Service

def Yard_Service():
    global shrub_count, user_input_service,lenear_foot, invalid,yard_sqft, edging_price,mowing_price
    global lenear_foot,edging_price,mowing_price,yard_sqft,shrub_price, overall, shrub_count, all_service, overall_yard
    global user_input_sizeLegnth, user_input_sizeWidth


    ##Gets total price for yard work 
    def YardWorkTool(service):
        global lenear_foot,edging_price,mowing_price,yard_sqft,shrub_price, overall, shrub_count, all_service, overall_yard
        
        if service == 'E':
            edging_price = round((lenear_foot * 10),2) #10 per ln sqft
            return edging_price

        elif service == 'M':

            mowing_price = round((yard_sqft * 1), 2) #dollar per sqft
            return mowing_price

        elif service == 'S':

            shrub_price = round((shrub_count * 12), 2) #12 per shrub
            return shrub_price

        elif service == 'ALL':

            edging_price = round((lenear_foot * 10),2) #10 per ln sqft
            mowing_price = round((yard_sqft * 1), 2) #dollar per sqft
            shrub_price = round((shrub_count * 12), 2) #12 per shrub

            all_service = edging_price + mowing_price + shrub_price 
            
            return all_service

    print("\tRequst for Yard Work")

    while True:
        print("--"*20) 
        
        #get length and width
        user_input_sizeLegnth = input("""\n\nWhat is the length of your yard in feet: """)
        
        if user_input_sizeLegnth not in string.ascii_letters and user_input_sizeLegnth not in string.punctuation:
            user_input_sizeLegnth = float(user_input_sizeLegnth)
            break 

        else:
            print("Please enter a number")  


    while True:
        user_input_sizeWidth = input("""\nWhat is the width of your yard in feet: """)
        
        if user_input_sizeWidth not in string.ascii_letters and user_input_sizeWidth not in string.punctuation:
            user_input_sizeWidth = float(user_input_sizeWidth)
            break 

        else:
            print("Please enter a number") 

    
    #calculate lenear_foot
    lenear_foot = (user_input_sizeLegnth * 2) + (user_input_sizeWidth * 2) 
    lenear_foot /= 12

    #calculate yeard square foot
    yard_sqft = user_input_sizeLegnth * user_input_sizeWidth




    while True:
        #ask for the yard service
        user_input_service = input("""\nWhich service are you requesting?
        Type 'M' for Mowing (price per square foot)
        Type 'E' for Edging (price per linear footage)
        Type 'S' for Shrub Pruning (price per shrub)
        Type 'All' for All three
        : """)

        user_input_service = user_input_service.upper()
        valid_list = ['M', 'E', 'S', 'ALL']

        if user_input_service not in invalid and user_input_service in valid_list: #checks for invalid characters

            if user_input_service == 'S' or user_input_service == "ALL": #specific to the shrubs
                while True:
                    input_shrubs = input("\nHow many shrubs do you have?: ")
                    input_shrubs = input_shrubs.upper()

                    if input_shrubs not in invalid2: #not a letter and not a number
                        input_shrubs = float(input_shrubs)
                        shrub_count = input_shrubs
                        break


                    else:
                        print("Invalid Input")



        
            YardWorkTool(user_input_service)
            break

        else:
            print("Please enter 'M', 'E', 'S' or All")

    return YardWorkTool(user_input_service)



#Main Function

print("\n\t\tAlyson's House and Yard Service\n")


def Request_Service():
    while True:
        ask_user = input("What service are you requesting?\nType 'H' for House Cleaning\nType 'Y' Yard work\nType 'B' for Both\n: ")
        ask_user = ask_user.upper()

        if ask_user in invalid:
            print("Please enter Y, H or B")

        else:
            

            if ask_user == "H":
                print("--"*20)

                #Run the date and discount
                Today_date_discount()

                print("--"*20)

                #Run house service
                house = House_Service()

                if senior_dis == "15% off":
                    discount = house * .15
                    house -= discount
                

                #Display Results
                print("**" * 15)
                print("\tServices Breakdown Overview")
                print("**" * 15)

                print(f"\nDate of service {month}/{day}/{yearint}\n")

                print(f"""House Cleaning Review\n
                Cleaning Type: {typeClean_string} --- ${typeClean_price}

                Room Amount: ${rooms}
                Rooms Type: {rm_type}

                Rooms Price: ${rm_price}

                Window Cleaning: {add_on_window}
                Basement/Attic Cleaning: {add_on_ExtraRoom}
                
                Senior Discount: {senior_dis}\nTotal Price For House Cleaning ${house}

                """)

                break

            elif ask_user == "Y":
                print("--"*20)

                Today_date_discount()

                print("--"*20)

                yard = Yard_Service()

                if senior_dis == "15% off":
                    discount = yard * .15
                    yard -= discount

                print("**" * 15)
                print("\tServices Breakdown Overview")
                print("**" * 15)

                print(f"\nDate of service {month}/{day}/{yearint}\n")

                print(f"""Yard Service Review\n
                Your yard size {user_input_sizeLegnth} ft legnth x {user_input_sizeWidth} ft width\n
                {round(lenear_foot)} Linear Feet
                \tEdging price ${edging_price}
                {yard_sqft} Square Feet
                \tMowing Price ${mowing_price}
                {shrub_count} Shrubs\tShrub Price ${shrub_price}

                Senior Discount: {senior_dis}\nYour total for yard work service is ${yard}

                """)


                break


            elif ask_user == "B":
                print("--"*20)

                Today_date_discount()

                print("--"*20)

                house = House_Service()
                print("--"*20)
            
                yard = Yard_Service()

                bServ = yard + house

                if senior_dis == "15% off":
                    discount = bServ * .15
                    bServ -= discount


                print("**" * 15)
                print("\tServices Breakdown Overview")
                print("**" * 15)

                print(f"\nDate of service {month}/{day}/{yearint}\n")

                print(f"""House Cleaning Review\n
                Cleaning Type: {typeClean_string} --- ${typeClean_price}

                Room Amount: ${rooms}
                Rooms Type: {rm_type}

                Rooms Price: ${rm_price}


                Window Cleaning: {add_on_window}

                Basement/Attic Cleaning: {add_on_ExtraRoom}\nTotal Price For House Cleaning ${house}

                """)

                print(f"""Yard Service Review\n
                Your yard size {user_input_sizeLegnth} ft legnth x {user_input_sizeWidth} ft width\n
                {round(lenear_foot)} Linear Feet
                \tEdging price ${edging_price}
                {yard_sqft} Square Feet
                \tMowing Price ${mowing_price}
                {shrub_count} Shrubs\tShrub Price ${shrub_price}\nYour total for yard work service is ${yard}


                Senior Discount: {senior_dis}""")

                print(f"\nTotal price for all services: ${bServ}\n")

                break    


Request_Service()


