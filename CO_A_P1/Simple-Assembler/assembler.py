# --------------------------------------------------------Satwik Garg start--------------------------------
def inpu():
# ------------------------------------taking input from the file and storing it in final data-----------------------------------------
    # f=open("example.txt",'r')
    # data=f.readlines()
    # print("data",data)
    l1=[]
    l2=[]
    l3=[]
    no_of_lines=0
    data_for_error_function_dic={}
    data_for_error_function_list=[]
    key=0
    final_data=[]
    var_data=[]
    var_dic={}
    data=[]

    test=[]

    while True:
        try:
            testline=input()
            test.append(testline)
        except EOFError:
            break
    # print(test)

    for i in test:
        # for j in i:
        l3.append(i.split())
        # l1.append(l4)
        # l4=[]
            

    

    # print("data",data)
    for i in data:
        l3.append(i.split())
    
    for i in l3:
        if(i!=[]):
            l1.append(i)
    # print("l1",l1)
# --------------------------------------data for error function-------------------------------------------------------------------
    for i in l1:
        if(i!=[]):
            
            data_for_error_function_list.append(i)    #dictionary of all the data with line number
            data_for_error_function_dic[key]=i    #list of all the data
            key+=1

# --------------------------------------------------data for all other funtions----------------------------------------------
    for i in l1:
        if((i!=[]) and i[0]!='var'):
            final_data.append(i)
            no_of_lines+=1

    for i in l1:
        if(i[0]=="var"):
            var_data.append(i[1])
    k=0
    for i in var_data:
        k=k+1
        var_dic[i]=str(format((no_of_lines+k-1),'b')).rjust(7,'0')

    # f.close()
    return final_data,no_of_lines-1,var_dic,data_for_error_function_dic,data_for_error_function_list


# I have created all_ISA, register, variable, and label lists. Now u guys have to write the code for the errors.


def error(data_for_error_function_dic,data_for_error_function_list):
    # -------------------------------------------------------write the error code here------------------------------------------------------
    all_isa=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
    reg_lst = ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]
    jump_statements=["jmp","jlt","jgt","je"]
    three_register=["add","sub","mul","xor","or","and"]
    two_register=["div","not","cmp"]
    imm_register=["ld","st","rs","ls"]
    register_dollar=["ls","rs"]
    register_with_variables=["ld","st"]
    var_list=[]#list for variables
    label_list=[]#list for lables

    for i in data_for_error_function_list:
        if(i[0]=="var"):
            var_list.append(i[1])
    
    # print()
    # print("variable list",var_list)

    for i in data_for_error_function_list:
        if(i[0][-1]==":" ):
            label_list.append(i[0][:len(i[0])-1])
    # print()
    # print("label list",label_list)
    # print()
    # -----------------------------------------more bits in mov-------------------------------
    for i in data_for_error_function_list:
        if(i[0]=="mov" and i[2][0]=="$"):
            if(int(i[2][1:])>127):
                print("Illegal Immediate values (more than 7 bits)")
                print("line no ",data_for_error_function_list.index(i))
                quit()
    # -----------------------------------------------------$ in ls and rs------------------------------------------------------
    for i in data_for_error_function_list:
        if(i[0]=="ls" or i[0]=="rs"):
            if(i[2][0]!="$"):
                print("no dollar sign")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
            
    # ------------------------------------------- no of registers ------------------
    for i in data_for_error_function_list:
        if(i[0] in three_register and len(i)!=4):
            print("inncorrect number of registers")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()
        if((i[0] in two_register or i[0] in imm_register or i[0]=="mov") and len(i)!=3):
            print("incorrect number of registers")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()

    # --------------------------------------------------------    A     ------------------------------------------------------------
    for i in data_for_error_function_list:
        if(i[0] not in all_isa and (i[0])[:len(i[0])-1] not in label_list and i[0] not in reg_lst and i[0]!="var"):
            print(i[0])
            print("Typos in instruction name")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()
    
    for i in data_for_error_function_list:
        if(i[0] in three_register):
            # print(i)
            if(i[1] not in reg_lst or i[2] not in reg_lst or i[3] not in reg_lst):
                print("Typos in register name")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif(i[0] in two_register):
            if(i[1] not in reg_lst or i[2] not in reg_lst):
                print("Typos in register name")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif(i[0] in imm_register):
            if(i[1] not in reg_lst):
                print("Typos in register name")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif((i[0])[:len(i[0])-1] in label_list):
            if(i[1] in three_register):
                if(i[2] not in reg_lst or i[3] not in reg_lst or i[4] not in reg_lst):
                    print("Typos in register name")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
            elif(i[1] in two_register):
                if(i[2] not in reg_lst or i[3] not in reg_lst):
                    print("Typos in register name")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
            elif(i[1] in imm_register):
                if(i[2] not in reg_lst):
                    print("Typos in register name")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
        elif(i[0]=="mov" and i[1] not in reg_lst):
            print("Typos in register name")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()
        elif(i[0]=="mov" and i[2] not in reg_lst and (i[2])[0]!="$"):
            print("Typos in register name")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()

# ----------------------------------------------------       B              --------------------------------------------------
    for i in data_for_error_function_list:
        if(i[0] in register_with_variables):
            if(i[2] not in var_list):
                print("Use of undefined variables")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif((i[0])[:len(i[0])-1] in label_list and i[1] in register_with_variables):
            if(i[3] not in var_list):
                print("Use of undefined variables")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
# --------------------------------------------Satwik Garg end------------------------------------
# --------------------------------------------Satkeerat Singh start-------------------------------------
# ---------------------------------------------------        C               --------------------------------------------
    for i in data_for_error_function_list:
        if(i[0] in jump_statements):
            if(i[1] not in label_list):
                print("Use of undefined labels")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
            
# ------------------------------------------------------       D             ------------------------------------------------
    for i in data_for_error_function_list:
        if(i[0] in three_register):
            # print(i)
            if(i[1]=="FLAGS" or i[2]=="FLAGS" or i[3]=="FLAGS"):
                print("Illegal use of FLAGS register")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif(i[0] in two_register):
            if(i[1]=="FLAGS" or i[2]=="FLAGS"):
                print("Illegal use of FLAGS register")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif(i[0] =="FLAGS"):
            if(i[1] not in reg_lst):
                print("Illegal use of FLAGS register")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif((i[0])[:len(i[0])-1] in label_list):
            if(i[1] in three_register):
                if(i[2]=="FLAGS" or i[3]=="FLAGS" or i[4]=="FLAGS"):
                    print("Illegal use of FLAGS register")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
            elif(i[1] in two_register):
                if(i[2]=="FLAGS" or i[3]=="FLAGS"):
                    print("Illegal use of FLAGS register")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
            elif(i[1] in imm_register):
                if(i[2]=="FLAGS"):
                    print("Illegal use of FLAGS register")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
        elif(i[0]=="mov" and i[1]=="FLAGS"):
            print("Illegal use of FLAGS register")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()



# ---------------------------------------------          E                ---------------------------------------
    for i in data_for_error_function_list:
        #print(i[0])
        if(i[0] in register_dollar):
            if(int(i[2][1:])>128):
                print("Illegal Immediate values (more than 7 bits)")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif((i[0])[:len(i[0])-1] in label_list):
            if(i[1] in register_dollar and int(i[3][1:])>128):
                print("Illegal Immediate values (more than 7 bits)")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()

# -----------------------------------------------            F                   --------------------------------------
    for i in data_for_error_function_list:
        if((i[0] in register_with_variables and i[2] in label_list) or (i[0])[:len(i[0])-1] in var_list):
            print("Misuse of labels as variables or vice-versa")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()

# -----------------------------------------     G                     --------------------------------------------------------------------
    k=0
    for i in data_for_error_function_list:
        if(i[0]=="var"):
            k+=1
        else:
            k=0
        if(k==1 and data_for_error_function_list.index(i)!=0):
            print("Variables not declared at the beginning")    
            print("line no",data_for_error_function_list.index(i)+1)
            quit()

#--------------------------------------------------------      I               ----------------------------------
    for i in data_for_error_function_list:
        if(i[0]=="hlt"):
            if(data_for_error_function_list.index(i)!=len(data_for_error_function_list)-1):
                print("hlt not being used as the last instruction")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
# ----------------------------------------------            H               --------------------------------------------
    try:
        if((data_for_error_function_list[len(data_for_error_function_list)-1][1]!="hlt")):
            print("Missing hlt instruction")
            print("Last line")
            quit()

    except:
        if((data_for_error_function_list[len(data_for_error_function_list)-1][0]!="hlt")):
            # print(data_for_error_function_list[len(data_for_error_function_list)-1][1])
            # print(data_for_error_function_list[len(data_for_error_function_list)-1][0])
            print("Missing hlt instruction")
            print("Last line")
            quit()
    





        

        
# --------------------------creating a list of all registers-------------------------
reg_lst = ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]


# --------------------------returns registers address-------------------
def register(r):
    if(r=="R0"):
        return "000"
    elif(r=="R1"):
        return "001"
    elif(r=="R2"):
        return "010"
    elif(r=="R3"):
        return "011"
    elif(r=="R4"):
        return "100"
    elif(r=="R5"):
        return "101"
    elif(r=="R6"):
        return "110"
    elif(r=="FLAGS"):
        return "111"

# --------------------------------------------------return variable address----------------------------------------------
def variable(var,var_dic):
    for i in var_dic.keys():
        if(i==var):
            return var_dic[var]


# ----------------------------------integer_to_binary_with_padding(used in satwik's funtion)----------------------
def integer_to_binary_with_padding(value):
    binary_number=format(int(value),'b')
    return str(binary_number).rjust(7,'0')



# --------------------------taking_input_in_label_dictionary with value as line number(used in satwik's function)----------------
def taking_input_in_label_dictionary(key,label_name_dictionary,data):
    k=0
    for i in data:
        k+=1
        if((i[0])[:len(key)]==key):
            value=integer_to_binary_with_padding(k-1)
    
    label_name_dictionary[key]=value
# -----------------------------------------------------Satkeerat Singh end--------------------------------------------
# -------------------------------------------------Sarthak Srivastav start--------------------------------------

# ----------------------extra function(used in satwik's function IGNORE IT) ----------------------------------------------------------------------
def key(instruction):
    all_isa=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
    for i in range(1,len(instruction)):
        if(instruction[i] not in all_isa):
            key=i
    return key



# -------------------------------------ISA(called function)----------------
def addition(r1, r2, r3):
    if r1 in reg_lst and r2 in reg_lst and r3 in reg_lst:
        return "0000000"+register(r1)+register(r2)+register(r3)

def subtraction(r1, r2, r3):
    if r1 in reg_lst and r2 in reg_lst and r3 in reg_lst:
        return "0000100"+register(r1)+register(r2)+register(r3)

def move_immediate(r, imm_val):
    # print("                   hi                           ")
    # print("imm value",imm_val[1:])
    # print("imm_val binary",integer_to_binary_with_padding(imm_val[1:]))
    
    if r in reg_lst:
        return "000100"+register(r)+integer_to_binary_with_padding(imm_val[1:])



def move_register(r1, r2):
    # print("              ",r2)
    if r1 in reg_lst and r2 in reg_lst:
        return "0001100000"+register(r1)+register(r2)

def load(r,var, var_dic):
    return "001000"+register(r)+var_dic[var]

def store(r,var,var_dic):
    return "001010"+register(r)+var_dic[var]

def multiply(r1,r2,r3):
    
    return "0011000"+register(r1)+register(r2)+register(r3)



def divide(r1,r2):
    return "0011100000"+register(r1)+register(r2)

def right_shift(r1,imm):
    
    return "010000"+register(r1)+integer_to_binary_with_padding(imm)



def left_shift(r1,imm):
    
    return "010010"+register(r1)+integer_to_binary_with_padding(imm)



def exclusive_OR(r1,r2,r3):
    if r1 in reg_lst and r2 in reg_lst and r3 in reg_lst:
        return "0101000"+register(r1)+register(r2)+register(r3)



def Or(r1,r2,r3):
    if r1 in reg_lst and r2 in reg_lst and r3 in reg_lst:
        return "0101100"+register(r1)+register(r2)+register(r3)



def And(r1,r2,r3):
     if r1 in reg_lst and r2 in reg_lst and r3 in reg_lst:
        return "0110000"+register(r1)+register(r2)+register(r3)


def invert(r1,r2):
    if r1 in reg_lst and r2 in reg_lst:
        return "0110100000"+register(r1)+register(r2)


def compare(r1,r2):
    # print("             r1",r1)
    # print("             r2",r2)
    if r1 in reg_lst and r2 in reg_lst:
        return "0111000000"+register(r1)+register(r2)


def unconditional_jump(instruction,label_name_dictionary,data):
    k=key(instruction)
    taking_input_in_label_dictionary(instruction[k],label_name_dictionary,data)
    return "011110000"+label_name_dictionary[instruction[k]]


def jump_if_less_than(instruction,label_name_dictionary,data):
    k=key(instruction)
    taking_input_in_label_dictionary(instruction[k],label_name_dictionary,data)
    return "111000000"+label_name_dictionary[instruction[k]]



def jump_if_greater_than(instruction,label_name_dictionary,data):
    k=key(instruction)
    taking_input_in_label_dictionary(instruction[k],label_name_dictionary,data)
    return "111010000"+label_name_dictionary[instruction[k]]



def jump_if_equal(instruction,label_name_dictionary,data):
    k=key(instruction)
    taking_input_in_label_dictionary(instruction[k],label_name_dictionary,data)
    return "111110000"+label_name_dictionary[instruction[k]]



def halt():
    return "1101000000000000"


# -------------------------------------------------Sarthak Srivastav end---------------------------------------------
# ----------------------------------------------------Saarthak Saxena start---------------------------------
# -------------------------calling all the different functions-----------
def calling_other_functions(data,no_of_lines,label_name_dictionary,var_dic):
    # f1=open("output.txt","w")
    for i in data:
        # print(i)
        if(i[0]=="add"):
            st=addition(i[1], i[2], i[3])
            # f1.write(st)
            print(addition(i[1], i[2], i[3]))
            # f1.write("\n")
        elif(i[0]=="sub"):
            # f1.write(subtraction(i[1], i[2], i[3]))
            print(subtraction(i[1], i[2], i[3]))
            # f1.write("\n")
        elif(i[0]=="mov" and (i[2])[0]=="$"):
            # f1.write(move_immediate(i[1], i[2]))
            print(move_immediate(i[1], i[2]))
            # f1.write("\n")
        elif(i[0]=="mov" and ((i[2])[:1]=="R" or (i[2])[:1]=="F")):
            # f1.write(move_register(i[1], i[2]))
            print(move_register(i[1], i[2]))
            # f1.write("\n")
        elif(i[0]=="ld"):
            # f1.write(load(i[1],i[2],var_dic))
            print(load(i[1],i[2],var_dic))
            # f1.write("\n")
        elif(i[0]=="st"):
            # f1.write(store(i[1],i[2],var_dic))
            print(store(i[1],i[2],var_dic))
            # f1.write("\n")
        elif(i[0]=="mul"):
            # f1.write(multiply(i[1],i[2],i[3]))
            print(multiply(i[1],i[2],i[3]))
            # f1.write("\n")
        elif(i[0]=="div"):
            # f1.write(divide(i[1],i[2]))
            print(divide(i[1],i[2]))
            # f1.write("\n")
        elif(i[0]=="rs"):
            # f1.write(right_shift(i[1],i[2][1:]))
            print(right_shift(i[1],i[2][1:]))
            # f1.write("\n")
        elif(i[0]=="ls"):
            # f1.write(left_shift(i[1],i[2][1:]))
            print(left_shift(i[1],i[2][1:]))
            # f1.write("\n")
        elif(i[0]=="xor"):
            # f1.write(exclusive_OR(i[1], i[2], i[3]))
            print(exclusive_OR(i[1], i[2], i[3]))
            # f1.write("\n")
        elif(i[0]=="or"):
            # f1.write(Or(i[1], i[2], i[3]))
            print(Or(i[1], i[2], i[3]))
            # f1.write("\n")
        elif(i[0]=="and"):
            # f1.write(And(i[1], i[2], i[3]))
            print(And(i[1], i[2], i[3]))
            # f1.write("\n")
        elif(i[0]=="not"):
            # f1.write(invert(i[1], i[2]))
            print(invert(i[1], i[2]))
            # f1.write("\n")
        elif(i[0]=="cmp"):
            # f1.write(compare(i[1], i[2]))
            print(compare(i[1], i[2]))
            # f1.write("\n")
        elif(i[0]=="jmp"):
            # f1.write(unconditional_jump(i,label_name_dictionary,data))
            print(unconditional_jump(i,label_name_dictionary,data))
            # f1.write("\n")
        elif(i[0]=="jlt"):
            # f1.write(jump_if_less_than(i,label_name_dictionary,data))
            print(jump_if_less_than(i,label_name_dictionary,data))
            # f1.write("\n")
        elif(i[0]=="jgt"):
            # f1.write(jump_if_greater_than(i,label_name_dictionary,data))
            print(jump_if_greater_than(i,label_name_dictionary,data))
            # f1.write("\n")
        elif(i[0]=="je"):
            # f1.write(jump_if_equal(i,label_name_dictionary,data))
            print(jump_if_equal(i,label_name_dictionary,data))
            # f1.write("\n")
        elif(i[0]=="hlt"):
            # f1.write(halt())
            print(halt())
            # f1.write("\n")
        else: 
            if(i[1]=="add"):
                # f1.write(addition(i[2], i[3], i[4]))
                print(addition(i[2], i[3], i[4]))
                # f1.write("\n")
            elif(i[1]=="sub"):
                # f1.write(subtraction(i[2], i[3], i[4]))
                print(subtraction(i[2], i[3], i[4]))
                # f1.write("\n")
            elif(i[1]=="mov" and (i[3])[0]=="$"):
                # print("                    mie                          ")
                # f1.write(move_immediate(i[2], i[3]))
                print(move_immediate(i[2], i[3]))
                # f1.write("\n")
            elif(i[1]=="mov" and (i[2])[:1]=="R"):
                # f1.write(move_register(i[2], i[3]))
                print(move_register(i[2], i[3]))
                # f1.write("\n")
            elif(i[1]=="ld"):
                # f1.write(load(i[2],i[3],var_dic))
                print(load(i[2],i[3],var_dic))
                # f1.write("\n")
            elif(i[1]=="st"):
                # f1.write(store(i[2],i[3],var_dic))
                print(store(i[2],i[3],var_dic))
                # f1.write("\n")
            elif(i[1]=="mul"):
                # f1.write(multiply(i[2],i[3],i[4]))
                print(multiply(i[2],i[3],i[4]))
                # f1.write("\n")
            elif(i[1]=="div"):
                # f1.write(divide(i[2],i[3]))
                print(divide(i[2],i[3]))
                # f1.write("\n")
            elif(i[1]=="rs"):
                # f1.write(right_shift(i[2],i[3][1:]))
                print(right_shift(i[2],i[3][1:]))
                # f1.write("\n")
            elif(i[1]=="ls"):
                # f1.write(left_shift(i[2],i[3][1:]))
                print(left_shift(i[2],i[3][1:]))
                # f1.write("\n")
            elif(i[1]=="xor"):
                # f1.write(exclusive_OR(i[2], i[3], i[4]))
                print(exclusive_OR(i[2], i[3], i[4]))
                # f1.write("\n")
            elif(i[1]=="or"):
                # f1.write(Or(i[2], i[3], i[4]))
                print(Or(i[2], i[3], i[4]))
                # f1.write("\n")
            elif(i[1]=="and"):
                # f1.write(And(i[2], i[3], i[4]))
                print(And(i[2], i[3], i[4]))
                # f1.write("\n")
            elif(i[1]=="not"):
                # f1.write(invert(i[2], i[3]))
                print(invert(i[2], i[3]))
                # f1.write("\n")
            elif(i[1]=="cmp"):
                # f1.write(compare(i[2], i[3]))
                print(compare(i[2], i[3]))
                # f1.write("\n")
            elif(i[1]=="jmp"):
                # f1.write(unconditional_jump(i,label_name_dictionary,data))
                print(unconditional_jump(i,label_name_dictionary,data))
                # f1.write("\n")
            elif(i[1]=="jlt"):
                # f1.write(jump_if_less_than(i,label_name_dictionary,data))
                print(jump_if_less_than(i,label_name_dictionary,data))
                # f1.write("\n")
            elif(i[1]=="jgt"):
                # f1.write(jump_if_greater_than(i,label_name_dictionary,data))
                print(jump_if_greater_than(i,label_name_dictionary,data))
                # f1.write("\n")
            elif(i[1]=="je"):
                # f1.write(jump_if_equal(i,label_name_dictionary,data))
                print(jump_if_equal(i,label_name_dictionary,data))
                # f1.write("\n")
            elif(i[1]=="hlt"):
                # f1.write(halt())
                print(halt())
                # f1.write("\n")
    # f1.close()
#------------------------------------Saarthak Saxena end-----------------------------------------------
# --------------------------------Sarthak Srivastav start-----------------------------------
def main():
    label_name_dictionary={}
    data , no_of_lines,var_dic,data_for_error_function_dic,data_for_error_function_list=inpu()#here data doesn't contain "var" list
    error(data_for_error_function_dic,data_for_error_function_list)
    calling_other_functions(data,no_of_lines,label_name_dictionary,var_dic)
if __name__ == "__main__":
    main()
# -----------------------------------Sarthak Srivastav end----------------------------------------------------
