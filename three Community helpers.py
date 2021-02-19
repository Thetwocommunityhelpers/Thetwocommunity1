
print("Welcome to the three community helpers!!!!!")
whoareyou=input("Are you a person who needs help or wants to give help?Only write either I am a person who wants aid or I am a person who wants to give aid to others :")
if whoareyou=="I am a person who wants aid":
    print("Food")
    print("Mask")
    print("Helper")
    print("Helper for Company")
    print("Education")
    opt=input("Which amenity would you like:")
   
    if opt=="Food":

        
        print("Here are a few food items that we have available:")
        print("Keep in mind that all the foods are veg because of Covid-19 and the bird flu")
        print("Italian")
        print("Indian")
        print("Chinese")
        food=input("Which cuisine would you like:")
        if food=="Italian":
            print("Here are a few food items that we have available for Italian:")
            print("Pizza")
            print("Pasta")
            
            itafood=input("Which type of italian would you like:")
            if itafood=="Pizza":
                print("Types of pizza avalible")
                print("1.Margherita pizza")
                print("2.Paneer pizza")
                print("3.Vegtable pizza")
                pizza1=input("Please enter the pizza you want(Type it exactly like it is said in the menu:")
                if pizza1=="Margherita pizza":
                    adre=input("Pls enter your adress so that we can deliver the pizza:")
                    print("Ok thank you your pizza will come in a sometime")
                if pizza1=="Paneer pizza":
                    adre=input("Pls enter your adress so that we can deliver the pizza:")
                    print("Ok thank you your pizza will come in a sometime")
                if pizza1=="Vegtable pizza":
                    adre=input("Pls enter your adress so that we can deliver the pizza:")
                    print("Ok thank you your pizza will come in a sometime")
            elif itafood=="Pasta":
                    
                    print("Types of pasta avalible")
                    print("1.Arrabbiata Pasta")
                    print("2.Pesto Pasta")
                    print("3.White sauce Pasta")
                    pasta1=input("Please enter the pasta you want(Type it exactly like it is said in the menu:")
                    if pasta1=="Arrabbiata Pasta":
                        adress=input("Pls enter your adress so that we can deliver the pasta")
                        print("Ok thank you your pasta will come in a sometime")
                    if pasta1=="Pesto Pasta":
                        adress=input("Pls enter your adress so that we can deliver the pasta")
                        print("Ok thank you your pasta will come in a sometime")
                    if pasta1=="White sauce Pasta":
                        adress=input("Pls enter your adress so that we can deliver the pasta")
                        print("Ok thank you your pasta will come in a sometime")
        if food=="Indian":
                
                
                print("Here are a few food items that we have available for Indian:")
                print("Garlic naan and moong dal")
                print("Cottage cheese/ Butter paneer sabji and roti")
                print("Rice and dal")
                print("Chole Bhature")
                print("Write exactly as it is said above")
                indifood=input("Enter the indian food you want:")
                
                if indifood=="Garlic naan and moong dal":
                    print("Great! your order has an been placed(keep in mind that only one garlic naan and moong dal has been ordered):")
                if indifood=="Cottage cheese/ Butter paneer sabji and roti":
                    
                    print("Great! your order has an been placed(keep in mind that only one Cottage cheese/ Butter paneer sabji and roti has been ordered:)")
                if indifood=="Rice and dal":
                    
                    print("Great! your order has an been placed(keep in mind that only one  Rice and dal has been ordered:)")
                if indifood=="Chole Bhature":
                    
                    print("Great! your order has an been placed(keep in mind that only one  has been ordered:)")
        
        if food=="Chinese":
                
                
                print("Here are a few food items that we have available for Chinese:")
                print("Dimsum")
                print("Lotus stem")
                print("Haka noodles")
                print("Fried rice")
                print("Spring rolls")
                print("Write exactly as it is said above")
                chinfood=input("Enter the Chinese food you want:")
                
                if chinfood=="Dimsum":
                    print("Vegtable Dimsum")
                    print("Mushroom Dimsum")
                    print("Paneer Dimsum")
                    print("Write exactly as it is said above")
                dimfood=input("Enter the Dimsum food you want:")
                if dimfood=="Vegtable Dimsum":
                    print("Great! your order has an been placed(keep in mind that only one plate of dimsum has been ordered")
                if dimfood=="Mushroom Dimsum":
                    print("Great! your order has an been placed(keep in mind that only one plate of dimsum has been ordered")
                if dimfood=="Paneer Dimsum":
                    print("Great! your order has an been placed(keep in mind that only one plate of dimsum has been ordered")
                if chinfood=="Lotus stem":
                    print("Great! your order has an been placed(keep in mind that only one plate of Lotus Stem has been ordered")
                if chinfood=="Haka noodles":
                    print("Great! your order has been placed(keep in mind that only one plate of Haka noodles has been ordered")
                if chinfood=="Spring rolls":
                    print=("Great! your order has been placed(keep in mind that only one plate of Spring rolls has been ordered")
    if opt=="Mask":
         
         
         print("Types of Masks")
         print("N95 Mask")
         print("Cotton Mask")
         print("Cloth Mask")
         print("Write exactly as it is said above")
         mask=input("Enter the type of mask you want:")
         if mask=="N95 Mask":
             print("Colours that are avalabile for this mask")
             print("Grey")
             print("Black")
             print("White")
             print("Write exactly as it is said above")
             colmask=input("Enter the colour you want for the mask")
             if colmask=="Grey":
                 print("Congrats!Your Grey mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
             if colmask=="Black":
                 print("Congrats!Your Black mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
             if colmask=="White":
                 print("Congrats!Your White mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
        
         elif mask=="Cotton Mask":
             print("Colours that are avalabile for this mask")
             print("Red")
             print("Black")
             print("White")
             print("Blue")
             print("Write exactly as it is said above")
             cotmask=input("Enter the colour you want for the mask")
             if cotmask=="Red":
                 print("Congrats!Your Red mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
             if cotmask=="Black":
                 print("Congrats!Your Black mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
             if cotmask=="White":
                 print("Congrats!Your White mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
        
             if cotmask=="Blue":
                 print("Congrats!Your Blue mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
        
         elif mask=="Cloth Mask":
             print("Colours that are avalabile for this mask")
             print("Red ")
             print("Black")
             print("White")
             print("Blue")
             print("Pink")
             print("Yellow")
             print("Write exactly as it is said above")
             clotmask=input("Enter the colour you want for the mask:")
             if clotmask=="Red":
                 print("Congrats!Your Red mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
             if clotmask=="Black":
                 print("Congrats!Your Black mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
             if clotmask=="White":
                 print("Congrats!Your White mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
        
             if clotmask=="Blue":
                 print("Congrats!Your Blue mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
                                                             
             if clotmask=="Pink":
                 print("Congrats!Your Pink mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered") 
             if clotmask=="Yellow":
                 print("Congrats!Your Yellow mask has been placed will be arriving in sometime(Keep in mind that only 1 mask has been ordered")
    if opt=="Helper":
        print("Which type of Helper would you like")
        print("Cleaning Helper")
        print("Cooking Helper")
        print("Gardening Helper")
        print("Pet helper")
        print("Write it exactly how it is above")
        helper=input("Enter the helper you want from above:")
        if helper=="Cleaning Helper":
            #Add numbers to adress
            adresss=input("Enter your adress,it is so that the helper can reach you")
            #Make new program on helper deatils and what time will she work
        if helper=="Cooking Helper":
            #Add numbers to adress
            adress=input("Enter your adress,it is so that the helper can reach you")
            
            
            #Make new program on helper deatils and what time will she work
        if helper=="Gardening Helper":
            #Add numbers to adress
            adresss=input("Enter your adress,it is so that the helper can reach you")
            
            #Make new program on helper deatils and what time will she work
        if helper=="Pet Helper":
            #Add numbers to adress
            adresss=input("Enter your adress,it is so that the helper can reach you")
            #Make new program on helper deatils and what time will she work
    if opt=="Education":
        
        print("What  Subject Teacher would you like for online class")
        print("Maths")
        print("English")
        print("Chemistry")
        print("Physics")
        print("Biology")
        print("Enter it exactly how it is said above")
        
        teacher=input("Enter the Subject Teacher you want")
        if teacher=="Maths":
            print("What grade level do they need help in")
            print("1.5th grade")
            print("2.6th grade")
            print("3.7th Grade")
            print("4.8th grade")
            print("5.9th grade")
            print("6.10th Grade")
    
            grade=int(input("Enter the number option  you want"))
            
            if grade==1:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
             
            if grade==2:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
             
             
            if grade==3:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
                 
             
            if grade==4:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
              
                      
             
            if grade==5:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
        
            
             
            if grade==6:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        if teacher=="English":
            print("What grade level do they need help in")
            print("1.5th grade")
            print("2.6th grade")
            print("3.7th Grade")
            print("4.8th grade")
            print("5.9th grade")
            print("6.10th Grade")
    
            grade=int(input("Enter the number option  you want"))
            
            if grade==1:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
             
            if grade==2:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
             
             
            if grade==3:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
                 
             
            if grade==4:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
              
                      
             
            if grade==5:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
        
            
             
            if grade==6:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        if teacher=="Chemistry":
            print("What grade level do they need help in")
            print("1.5th grade")
            print("2.6th grade")
            print("3.7th Grade")
            print("4.8th grade")
            print("5.9th grade")
            print("6.10th Grade")
    
            grade=int(input("Enter the number option  you want"))
            
            if grade==1:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
             
            if grade==2:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
             
             
            if grade==3:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
                 
             
            if grade==4:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
              
                      
             
            if grade==5:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
        
            
             
            if grade==6:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
            
            
        if teacher=="Physics":
            print("What grade level do they need help in")
            print("1.5th grade")
            print("2.6th grade")
            print("3.7th Grade")
            print("4.8th grade")
            print("5.9th grade")
            print("6.10th Grade")
    
            grade=int(input("Enter the number option  you want"))
            
            if grade==1:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
             
            if grade==2:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
             
             
            if grade==3:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
                 
             
            if grade==4:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
              
                      
             
            if grade==5:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
        
            
             
            if grade==6:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        if teacher=="Biology":
            print("What grade level do they need help in")
            print("1.5th grade")
            print("2.6th grade")
            print("3.7th Grade")
            print("4.8th grade")
            print("5.9th grade")
            print("6.10th Grade")
    
            grade=int(input("Enter the number option  you want"))
            
            if grade==1:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
             
            if grade==2:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
             
             
            if grade==3:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
                 
             
            if grade==4:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
              
                      
             
            if grade==5:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
        
            
             
            if grade==6:
                
                print("1-2pm")
                print("2-3pm")
                print("3-4pm")
                print("4-5pm")
                time=input("What option you want. Pls enter it the way it is said")
                if time=="1-2pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
                if time=="2-3pm":
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")

                if time=="3-4pm":
                    
                

                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
        
                if time=="4-5pm":
                    
                    email=input("pls enter your email/phone number so that the teacher can reach out to you")
            
##            
##    if opt=="Helper for Company":
##        print("What type of online helper which will keep you company would you like")
##        print("1.60+=Senior Citizen Company Helper")
##        print("2.22+=Adults Company helper")
##        print("3.13+ Teen  Company Helper")
##        print("4.7+=Kids helper")
##        helperrr=int(input("pls enter which helper would you like. Only write the number beside it"))
##        if helperrr==1:
##            interest=input("pls say what insterst the senior citzen likes")
##            
##        
##            
        
                                        
                    
                
                
                
                
                   
                                    
                                    

                               
                                    
                                
                                 
                                    

                                 
                                 
                                 
                                 
                                            
                                
                            
                                
                                
                               
                                
                                    
                                        
                                                            
                                        
                                    
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                    
                                
                                    
                                        
                                                
                                                          
                                            
                                        
                                        

                                            
                                            
                                
                                
                                



