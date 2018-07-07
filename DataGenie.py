def main():
      import sys
      import random
      import time
      from faker import Faker
      import names
      import gender_guesser.detector as gender
      fake = Faker()
      print("\n>>Created by SOD<<")

      userdefined_file_name=input("\nEnter your desired file name \t")
      
      file_txt=userdefined_file_name + ".txt"

      firstname_txt=userdefined_file_name +'Firstname' ".txt"

      middlename_txt=userdefined_file_name +'MiddleName' ".txt"

      lastname_txt=userdefined_file_name +'Lastname' ".txt"

      fullname_txt=userdefined_file_name+ 'Fullname'  ".txt"

      firstname_lastname_txt=userdefined_file_name +'Firstname_Lastname' ".txt"

      firstname_middlename_lastname_txt=userdefined_file_name +'Firstname_MiddleName_Lastname' ".txt"
      
      title_txt=userdefined_file_name +'Title' ".txt"

      old_stdout = sys.stdout

      gender_detector = gender.Detector()


      def process_completed_time():
            #sys.stdout.close()
            sys.stdout = old_stdout
            print("\n Generation is completed at " +time.ctime() +" \n Have a look at your file :) ")
            #time.sleep(150)
            file_generate_decision=input("\nDo  you want to generate another file\nReply with Y or N\t")
            if(file_generate_decision=='Y' or file_generate_decision=='y'):
                  main()
            else:
                  exit(0)

      def wordsinglecount():
            string= input("\nEnter Some sample name for Data Generation: \n Eg: Sanjay \n (or) \n Manoj Tiwari \n (or) \n Mary Elizabeth Smith \t")
            word = 1
            for i in string:
                  if(i==' '):
                        word=word+1
            if(word==3):
                  title_decision=input("\nDo  you want to include Title at the beginning? \n Eg: Ms. Mary Elizabeth Smith \n Reply with Y or N \t")
                  if(title_decision=='Y' or title_decision== 'y'):
                        firstname_middlename_lastname_title_single_file()
                  elif(title_decision=='N' or title_decision=='n'):
                        firstname_middlename_lastname_single_file()
                  else:
                        print("Sorry you haven't selected any options:( \n So going back<<<")
                        wordsinglecount()
            elif(word==2):
                  title_decision=input("\nDo  you want to include Title at the beginning? \n Eg: Mr. Manoj Tiwari \n Reply with Y or N \t")
                  if(title_decision=='Y' or title_decision== 'y'):
                        firstname_lastname_title_single_file()
                  elif(title_decision=='N' or title_decision=='n'):
                        firstname_lastname_single_file()
                  else:
                        print("Sorry you haven't selected any options:( \n So going back<<<")
                        wordsinglecount()
            elif(word==1):
                  title_decision=input("\nDo  you want to include Title at the beginning? \n Eg: Mr. Anush\n Reply with Y or N \t")
                  if(title_decision=='Y' or title_decision== 'y'):
                        firstname_title_single_file()
                  elif(title_decision=='N' or title_decision=='n'):
                        firstname_single_file()
                  else:
                        print("Sorry you haven't selected any options:( \n So going back<<<")
                        wordsinglecount()
                  firstname_title_single_file()

      def wordsplitcount():
            string= input("\nEnter Some sample name for Data Generation: \n Eg: Sanjay \n (or) \n Manoj Tiwari \n (or) \n Mary Elizabeth Smith \t")
            word = 1
            for i in string:
                  if(i==' '):
                        word=word+1
            if(word==3):
                  firstname_middlename_lastname_split_files()
            elif(word==2):
                  firstname_lastname_split_files()
            elif(word==1):
                  firstname_split_files()

      def firstname_title_single_file():
            try:
                  firstname_textfile_creation=open(firstname_txt,"w")
                  userdefined_count=int(input("\n Enter the Number of Names (First Name) you want to generate\n in a single file \n Sample Output:Mr. Sanjay \t"))
                  print("\n Your process is started at "+time.ctime())
                  for _ in range(userdefined_count):
                        sys.stdout=firstname_textfile_creation
                        a= names.get_first_name()
                        gen=(gender_detector.get_gender(a))
                        print('Mr.'+" "+a if (gen=='male' or gen=='mostly_male') else 'Miss.'+" "+a)
                  firstname_textfile_creation.close()
            finally:
                  process_completed_time()

      def firstname_single_file():
            try:
                  firstname_textfile_creation=open(firstname_txt,"w")
                  userdefined_count=int(input("\n Enter the Number of Names (First Name) you want to generate\n in a single file \n Sample Output: Sanjay \t"))
                  print("\n Your process is started at "+time.ctime())
                  for _ in range(userdefined_count):
                        sys.stdout=firstname_textfile_creation
                        a= names.get_first_name()
                        print(a)
                  firstname_textfile_creation.close()
            finally:
                  process_completed_time()

      def firstname_lastname_title_single_file():
                  try:
                        firstname_lastname_textfile_creation=open(firstname_lastname_txt,"w")
                        userdefined_count=int(input("\n Enter the Number of Names (First Name / Last Name) you want to generate\n in a single file \n Sample Output:Mr. Manoj Tiwari \t"))
                        print("\n Your process is started at "+time.ctime())
                        for _ in range(userdefined_count):
                              sys.stdout=firstname_lastname_textfile_creation
                              a= names.get_first_name()
                              b= names.get_last_name()
                              gen=(gender_detector.get_gender(a))
                              print('Mr.'+" "+a+" "+b if (gen=='male' or gen=='mostly_male') else 'Miss.'+" "+a+" "+b)
                        firstname_lastname_textfile_creation.close()
                  finally:
                        process_completed_time()

      def firstname_middlename_lastname_single_file():
                  try:
                        firstname_middlename_lastname_textfile_creation=open(firstname_middlename_lastname_txt,"w")
                        userdefined_count=int(input("\nEnter the Number of Names (First Name / Middle Name / Last Name) \n you want to generate in single file  \n Sample Output: Ms. Mary Elizabeth Smith \t"))
                        print("\nYour process is started at "+time.ctime())
                        female_list=['Miss.','Mrs.']
                        for _ in range(userdefined_count):
                              sys.stdout=firstname_middlename_lastname_textfile_creation
                              a= names.get_first_name()
                              b= names.get_last_name()
                              gen=(gender_detector.get_gender(a))
                              print(a+" "+fake.first_name_male()+" "+b if (gen=='male' or gen=='mostly_male') else a+" "+fake.first_name_female()+" "+b)

                              
                        firstname_middlename_lastname_textfile_creation.close()
                  finally:
                        process_completed_time()
                  
      def firstname_middlename_lastname_title_single_file():
                  try:
                        firstname_middlename_lastname_textfile_creation=open(firstname_middlename_lastname_txt,"w")
                        userdefined_count=int(input("\nEnter the Number of Names (First Name / Middle Name / Last Name) \n you want to generate in single file  \n Sample Output: Ms. Mary Elizabeth Smith \t"))
                        print("\nYour process is started at "+time.ctime())
                        female_list=['Miss.','Mrs.']
                        for _ in range(userdefined_count):
                              sys.stdout=firstname_middlename_lastname_textfile_creation
                              a= names.get_first_name()
                              b= names.get_last_name()
                              gen=(gender_detector.get_gender(a))
                              print("Mr. "+a+" "+fake.first_name_male()+" "+b if (gen=='male' or gen=='mostly_male') else fake.random_element(female_list)+a+" "+fake.first_name_female()+" "+b)
                              

                              
                        firstname_middlename_lastname_textfile_creation.close()
                  finally:
                        process_completed_time()

                        

                        
      def firstname_lastname_single_file():
                  try:
                        firstname_lastname_textfile_creation=open(firstname_lastname_txt,"w")
                        userdefined_count=int(input("\n Enter the Number of Names (First Name / Last Name) you want to generate\n in a single file \n Sample Output:Manoj Tiwari \t"))
                        print("\n Your process is started at "+time.ctime())
                        for _ in range(userdefined_count):
                              sys.stdout=firstname_lastname_textfile_creation
                              a= names.get_first_name()
                              b= names.get_last_name()
                              print(a+" "+b)
                        firstname_lastname_textfile_creation.close()
                  finally:
                        process_completed_time()


      def firstname_lastname_split_files():
                  try:
                        choice_m=(input("What do you want to generate names in Lowercase or UpperCase, Reply with your choice(Number)  \n 1.Lower  \n 2.Upper\n"))
                        if choice_m=='1':
                              firstname_textfile_creation=open(firstname_txt,"w")
                              lastname_textfile_creation=open(lastname_txt,"w")
                              title_textfile_creation=open(title_txt,"w")
                              userdefined_count=int(input("\n ETA 1L data: 20 min including title \n Enter the Number of Names (First Name / Last Name) you want to generate \n Sample Output:Mr. Manoj Tiwari \t"))
                              print("\nYour process is started at "+time.ctime())
                              female_list=['Miss.','Mrs.']
                              for _ in range(userdefined_count):
                                    sys.stdout=firstname_textfile_creation
                                    a= names.get_first_name()
                                    b= names.get_last_name()
                                    print(a)
                                    sys.stdout=title_textfile_creation
                                    gen=(gender_detector.get_gender(a))
                                    if gen=='male' or gen=='mostly_male':
                                        print('Mr.')
                                    else:
                                        print(fake.random_element(female_list))
                                    sys.stdout=lastname_textfile_creation
                                    print(b)
                                    
                                    
                              firstname_textfile_creation.close()
                              title_textfile_creation.close()
                              lastname_textfile_creation.close()
                        if choice_m=='2':
                              firstname_textfile_creation=open(firstname_txt,"w")
                              lastname_textfile_creation=open(lastname_txt,"w")
                              title_textfile_creation=open(title_txt,"w")
                              userdefined_count=int(input("\nETA 1L data: 20 min including title \n Enter the Number of Names (First Name / Last Name) you want to generate \n Sample Output:Mr. MANOJ TIWARI \t"))
                              print("\nYour process is started at "+time.ctime())
                              female_list=['Miss.','Mrs.']
                              for _ in range(userdefined_count):
                                    sys.stdout=firstname_textfile_creation
                                    a= names.get_first_name()
                                    b= names.get_last_name()
                                    print(a.upper())
                                    sys.stdout=title_textfile_creation
                                    gen=(gender_detector.get_gender(a))
                                    if gen=='male' or gen=='mostly_male':
                                        print('Mr.')
                                    else:
                                        print(fake.random_element(female_list))
                                    sys.stdout=lastname_textfile_creation
                                    print(b.upper())
                                    
                                    
                              firstname_textfile_creation.close()
                              title_textfile_creation.close()
                              lastname_textfile_creation.close()
                              
                  finally:
                        process_completed_time()
      def firstname_middlename_lastname_split_files():
                  try:
                        firstname_textfile_creation=open(firstname_txt,"w")
                        middlename_textfile_creation=open(middlename_txt,"w")
                        lastname_textfile_creation=open(lastname_txt,"w")
                        fullname_textfile_creation=open(fullname_txt,"w")
                        title_textfile_creation=open(title_txt,"w")
                        userdefined_count=int(input("\nEnter the Number of Names (First Name / Middle Name / Last Name) you want to generate \n Sample Output: Ms. Mary Elizabeth Smith \t"))
                        print("\nYour process is started at "+time.ctime())
                        female_list=['Miss.','Mrs.']
                        for _ in range(userdefined_count):
                              sys.stdout=firstname_textfile_creation
                              a= names.get_first_name()
                              b= names.get_last_name()
                              c=fake.first_name_male()
                              d=fake.first_name_female()
                              print(a)
                              sys.stdout=title_textfile_creation
                              gen=(gender_detector.get_gender(a))
                              if gen=='male' or gen=='mostly_male':
                                  print('Mr.')
                              else:
                                  print(fake.random_element(female_list))
                              sys.stdout=lastname_textfile_creation
                              print(b)
                              sys.stdout=middlename_textfile_creation
                              if gen=='male' or gen=='mostly_male':
                                    print(c)
                              else:
                                    print(d)
                                  
                              sys.stdout=fullname_textfile_creation
                              #print("Mr. "+a+" "+fake.first_name_male()+" "+b if (gen=='male' or gen=='mostly_male') else "Ms. "+a+" "+fake.first_name_female()+" "+b)
                              print(a+' '+c+' '+b if (gen=='male' or gen=='mostly_male') else a+" "+d+" "+b)
                              
                        firstname_textfile_creation.close()
                        title_textfile_creation.close()
                        lastname_textfile_creation.close()
                        fullname_textfile_creation.close()
                        middlename_textfile_creation.close()
                  finally:
                        process_completed_time()

      def firstname_split_files():
                  try:
                        firstname_textfile_creation=open(firstname_txt,"w")
                        title_textfile_creation=open(title_txt,"w")
                        userdefined_count=int(input("Enter the Number of Names (First Name) you want to generate \n Sample Output: Mr. Sanjay \t"))
                        print("Your process is started at "+time.ctime())
                        female_list=['Miss.','Mrs.']
                        for _ in range(userdefined_count):
                              sys.stdout=firstname_textfile_creation
                              a= names.get_first_name()
                              print(a)
                              sys.stdout=title_textfile_creation
                              gen=(gender_detector.get_gender(a))
                              if gen=='male' or gen=='mostly_male':
                                  print('Mr.')
                              else:
                                  print(fake.random_element(female_list))
                              
              
                        firstname_textfile_creation.close()
                        title_textfile_creation.close()
                  finally:
                        process_completed_time()


      choice_m=(input("What do you want to generate, Reply with your choice(Number)  \n 1.Address \n 2.Phone Number \n 3.Company Names \n 4.Credit Card Number \n 5.Email ID's \n 6.Job Titles \n 7.Name \n 8.Range \n 9. Random Number \t"))
      if choice_m=='1':
            if choice_m=='1':
                  choice_m=(input("\n Do you want to generate \n 1.Address Line 1 \n 2.Address Line 2 \n 3.Address Line 3 \n 4.City \n 5.Postcode  \n 6.Full UK address \n 7.Full Address"))
                  if choice_m=='1':
                        try:
                              textfile_creation=open(file_txt,"w")
                              userdefined_count=int(input("Enter the Number of Address Line 1 you want to generate \t"))
                              print("Your process is started at "+time.ctime())                        
                              building_suffix=['Tower','Building','Hall',' ']
                              for _ in range(userdefined_count):
                                    sys.stdout=textfile_creation
                                    print(fake.building_number()+","+fake.city()+" "+fake.random_element(building_suffix))
                              textfile_creation.close()
                        finally:
                              process_completed_time()
                        
                  elif choice_m=='2':
                        try:
                              
                              textfile_creation=open(file_txt,"w")
                              userdefined_count=int(input("Enter the Number of Address Line 2 you want to generate \t"))
                              print("Your process is started at "+time.ctime())                        
                              street_suffix=[' Street',' ']
                              for _ in range(userdefined_count):
                                    
                                    sys.stdout=textfile_creation
                                    print(fake.street_name()+fake.random_element(street_suffix))
                              textfile_creation.close()
                        finally:
                              process_completed_time()

                  elif choice_m=='3':
                        try:
                              textfile_creation=open(file_txt,"w")
                              userdefined_count=int(input("Enter the Number of Address Line 3 you want to generate \t"))
                              print("Your process is started at "+time.ctime())                        
            
                              for _ in range(userdefined_count):
                                    sys.stdout=textfile_creation
                                    print(fake.state())
                              textfile_creation.close()
                        finally:
                              process_completed_time()

                  elif choice_m=='4':
                        
                        try:
                              textfile_creation=open(file_txt,"w")
                              userdefined_count=int(input("Enter the Number of City you want to generate \t"))
                              print("Your process is started at "+time.ctime())                        
            
                              for _ in range(userdefined_count):
                                    sys.stdout=textfile_creation
                                    print(fake.city())
                              textfile_creation.close()
                        finally:
                        
                              process_completed_time()

                  elif choice_m=='5':
                        try:
                              textfile_creation=open(file_txt,"w")
                              print("\n ETA for 1Lakh Data Generation is 4 Seconds")
                              userdefined_count=int(input("Enter the Number of Post code you want to generate \t"))
                              print("Your process is started at "+time.ctime())
                              for _ in range(userdefined_count):
                                    sys.stdout=textfile_creation
                                    print(fake.random_uppercase_letter()+fake.random_uppercase_letter()+str (fake.random_number(digits=3,fix_len=True))+' '+str (fake.random_number(digits=1,fix_len=True))+fake.random_uppercase_letter()+fake.random_uppercase_letter())
                              textfile_creation.close()
                        finally:
                              process_completed_time()

                  elif choice_m=='6':
                        try:
                              textfile_creation=open(file_txt,"w")
                              userdefined_count=int(input("Enter the Number of address you want to generate \t"))
                              print("Your process is started at "+time.ctime())
                              postalcode_list=['SY3','G41','G51','G31','G21','B44','SW1A','EC2M','N1','EC1A','EC4Y','EH12','EC2N','B70','B33','AB10','WC1A','B23','B65','B34','SW15','AB41','E8','AB21','E20','B71','B20','B68','B32','N14','N6','B42','AB56','AB25','E7','AB43','B46','B31','B69','B43','B62','B94','B66','B35','B79','W2','AB45','AB38','AB55','PO4 9BY','NE9 6HX','EX34 8LH','SM4 5RF','SE4 2BH','GL51 3ND','PR1 8JB','TW11 9BQ','GL7 2DG','TS15 9XE','PO21 3AE','SM1 4PL','GL53 9EQ','L21 2PA','GU28 0DS','WS14 0QH','YO31 1HZ','NN14 6EP','SY6 6DU','TN7 4AE','SW1A 1AA','SY3 7FA','BN1 2NW','CF24 3DG','BA1 2FJ','W1T 1JY','EH10 4BF','B3 2EW','SW1A 1BA','WIS 2HX','SWIA OAA','SW1E 5DU','SE1 2AA']
                              building_suffix=['Tower','Building','Hall',' ']
                              for _ in range(userdefined_count):
                                    sys.stdout=textfile_creation
                                    print(fake.building_number()+","+fake.city()+" "+fake.random_element(building_suffix)+","+fake.street_name()+" Street"+", London"+", "+fake.random_element(postalcode_list))
                              textfile_creation.close()
                        finally:
                              
                              process_completed_time()

                  elif choice_m=='7':
                        try:
                              textfile_creation=open(file_txt,"w")
                              userdefined_count=int(input("Enter the Number of address you want to generate \t"))
                              print("Your process is started at "+time.ctime())
                              for _ in range(userdefined_count):
                                    sys.stdout=textfile_creation
                                    print(fake.address())
                              textfile_creation.close()
                        finally:
                              
                              process_completed_time()
                  
                  

      elif choice_m=='2':
                  try:
                        textfile_creation=open(file_txt,"w")
                        userdefined_count=int(input("Enter the Number of Phone numbers you want to generate \t"))
                        print("Your process is started at "+time.ctime())
                        for _ in range(userdefined_count):
                              sys.stdout=textfile_creation
                              print("0"+str(fake.random_number(digits=3,fix_len=True))+str(fake.random_number(digits=3,fix_len=True))+str(fake.random_number(digits=4,fix_len=True)))
                        textfile_creation.close()
                  finally:
                        process_completed_time()

      elif choice_m=='3':
                  try:
                        textfile_creation=open(file_txt,"w")
                        userdefined_count=int(input("Enter the Number of Company names you want to generate \t"))
                        print("Your process is started at "+time.ctime())
                        for _ in range(userdefined_count):
                              sys.stdout=textfile_creation
                              print(fake.company())
                        textfile_creation.close()
                  finally:
                        process_completed_time()
                        
      elif choice_m=='4':
                  try:
                        textfile_creation=open(file_txt,"w")
                        userdefined_count=int(input("Enter the Number of Credit Numbers you want to generate \t"))
                        print("Your process is started at "+time.ctime())
                        for _ in range(userdefined_count):
                              sys.stdout=textfile_creation
                              print((fake.credit_card_number()+fake.credit_card_number())[0:16])
                        textfile_creation.close()
                  finally:
                        process_completed_time()
                        
      elif choice_m=='5':
            choice_m=(input("What do you want to generate, Reply with your choice(Number)  \n 1.Username+Company E-Mail ID \n 2.Username+Personal E-Mail ID \n 3.E-mail ID Domains Alone \n 4.Custom  Email Domain (Recommended for Large Data Creation)\n"))
            if choice_m=='1':
                  try:
                        textfile_creation=open(file_txt,"w")
                        userdefined_count=int(input("Enter the Number of Username+Company E-Mail ID  you want to generate \t"))
                        print("Your process is started at "+time.ctime())
                        for _ in range(userdefined_count):
                              sys.stdout=textfile_creation
                              print(fake.company_email())
                        textfile_creation.close()
                  finally:
                        process_completed_time()
            elif choice_m=='2':
                  try:
                        textfile_creation=open(file_txt,"w")
                        userdefined_count=int(input("Enter the Number of Username+Personal E-Mail ID  you want to generate \t"))
                        print("Your process is started at "+time.ctime())
                        for _ in range(userdefined_count):
                              sys.stdout=textfile_creation
                              print(fake.free_email())
                        textfile_creation.close()
                  finally:
                        process_completed_time()
            elif choice_m=='3':
                  try:
                        f=open(file_txt,"w")
                        userdefined_count=int(input("Enter the Number of E-mail ID Domains you want to generate \t"))
                        print("Your process is started at "+time.ctime())
                        for _ in range(userdefined_count):
                              sys.stdout=f
                              print('@'+fake.domain_name())
                        f.close()
                  finally:
                        process_completed_time()
            elif choice_m=='4':
                  try:
                        f=open(file_txt,"w")
                        userdefined_count=int(input("Enter the Number of Customised E-mail ID you want to generate \t"))
                        random_len=int(input("Enter how many digits of Random Number you need after the name \n Eg: If you enter '2' \n  Output:sasikumar34@GMAIL.com \t"))
                        custom_domain=input("Enter custom domain with @(symbol) \n Eg: @yahoo.com \n Output:sasikumar34@yahoo.com \t")
                        print("Your process is started at "+time.ctime())
                        for _ in range(userdefined_count):
                              sys.stdout=f
                              print(fake.first_name()+fake.last_name()+str(fake.random_number(digits=random_len,fix_len=True))+custom_domain)
                        f.close()
                  finally:
                        process_completed_time()
      elif choice_m=='6':
                  try:
                        textfile_creation=open(file_txt,"w")
                        userdefined_count=int(input("Enter the Number of Job Titles you want to generate \t"))
                        print("Your process is started at "+time.ctime())
                        for _ in range(userdefined_count):
                              sys.stdout=textfile_creation
                              print(fake.job())
                        textfile_creation.close()

                  finally:
                        process_completed_time()
                        

      elif choice_m=='7':
            choice=input("Do you need splitup in files?? \n Eg: (if Yes) then your output will be in this format \nFirstName.txt, MiddleName.txt, LastName.txt, Title \n Reply with Y or N \t")
            if(choice=='y' or choice=='Y'):
                  wordsplitcount()
            else:
                  wordsinglecount()
                        
      elif choice_m=='8':
                        r1=int(input("Enter the start value \t"))
                        r2=int(input("Enter the end value \t"))
                        r3=r2-r1
                        print("Total count =", r3)
                        choice=input("Do you want to include any number at the starting, reply with Y/N \t")
                        if choice=='Y'or choice=='y':
                              try:
                                    textfile_creation=open(file_txt,"w")
                                    front=input("Enter the number you want to insert in the front \t")
                                    for a in range(r1,r2):
                                          sys.stdout=textfile_creation
                                          print(front,a,sep="")
                                    textfile_creation.close()
                              finally:
                                    process_completed_time()
                        if choice=='N'or choice=='n':
                              try:
                                    textfile_creation=open(file_txt,"w")
                                    for a in range(r1,r2):
                                          sys.stdout=textfile_creation
                                          print(a,end="\n")
                                    textfile_creation.close()
                              finally:
                                    process_completed_time()

      elif choice_m=='9':
            try:
                  textfile_creation=open(file_txt,"w")
                  userdefined_count=int(input("Enter the Number of Random numbers you want to generate \t"))
                  strnlngth_count=int(input("Enter the String length you want to generate \t"))
                  print("Your process is started at "+time.ctime())
                  for _ in range(userdefined_count):
                        sys.stdout=textfile_creation
                        print(str(fake.random_number(digits=strnlngth_count,fix_len=True)))
                  textfile_creation.close()
            finally:
                  process_completed_time()


      else:
                              print("Sorry you haven't selected any options:( \nSo going back <<")
                              main()

main()

