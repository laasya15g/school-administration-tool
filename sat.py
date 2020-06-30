# school admninstration tool
import csv

def write_into_csv(i_list):  #to write into csv file
    with open('student_info.csv','a', newline='') as csv_file: #csv file is an object
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","phonenumber","Email ID"])
        
        writer.writerow(i_list)

        
#convert it to a function
if __name__ == '__main__':
    i=True
    s_num=1
    while(i):
        s_info =input("enter the s info for the student #{} in the following formats (name,age,contact_number,e-mail):".format(s_num))
        #comma seperated file 

        #split function 
        s_i_list=s_info.split(' ')
        print("splited up information"+str(s_i_list))

        print ("\n the entered informatiton is-\nName: {}\nAge: {}\nPNo: {}\nE-mail ID:{}"
               .format(s_i_list[0],s_i_list[1],s_i_list[2],s_i_list[3]))
        
        cc=input("is the entered info correct? y/n ")
        
        if cc=='y':
            write_into_csv(s_i_list)
            
            condition_check = input("continue by entering s_info mention by Y/N")
            if condition_check == 'Y':
                i=True
                s_num+=1
            elif condition_check == 'N':
                i=False
        elif cc=='no':
            print("renter the values")
#output should look like csv file ,file input output operations can be done
