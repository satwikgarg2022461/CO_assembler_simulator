# -------------------------------------------satwik starts----------------------------------------------------------
# ---------------------------------------------variable declaration--------------------------------------------------
R0=0
R1=0
R2=0
R3=0
R4=0
R5=0
R6=0
FLAGS="0000000000000000"
# ----------------------------------integer_to_binary_with_padding for registers 16 bits(used in satwik's funtion)----------------------
def integer_to_binary_with_padding(value):
    binary_number=format(int(value),'b')
    return str(binary_number).rjust(16,'0')


def integer_to_binary_with_padding_for_dictionary(value):
# ----------------------------------integer_to_binary_with_padding for dictionary 7 bits(used in satwik's funtion)----------------------
    binary_number=format(int(value),'b')
    return str(str(binary_number).rjust(7,'0'))


def mem_dum():
    for i in range(0,len(mem_dump),1):
        if(i==len(mem_dump)):
            print(mem_dump[i],end="")
       	else:
       	    print(mem_dump[i])
    


def assigning_value_in_global_var(s,x):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    # print("-------------assigning--------------")
    # print("x",x)
    # print("s",s)
    
    # global FLAGS,R1,R2,R3,R4,R5,R6,R0
    if(s=="000"):
        R0=x
    elif(s=="001"):
        # print("hi")
        R1=x
    elif(s=="010"):
        R2=x
    elif(s=="011"):
        R3=x
    elif(s=="100"):
        R4=x
    elif(s=="101"):
        R5=x
    elif(s=="110"):
        R6=x
    # print("R0",R0)
    # print("R1",R1)
    # print("R2",R2)
    # print("R3",R3)
    # print("R4",R4)
    # print("R5",R5)
    # print("R6",R6)
    # print("FLAGS",FLAGS)
    # print("R1",R1)
#     reg_dic={"000": R0,"001":R1,"010":R2,"011":R3,"100":R4,"101":R5,"110":R6,"111":FLAGS}

# # ------------------------------------------register dictionary for accessing the value of the registers-------------------------
# reg_dic={"000": R0,"001":R1,"010":R2,"011":R3,"100":R4,"101":R5,"110":R6,"111":FLAGS}

def reg_dic(s):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    # print("---------reg_dic---------------")
    # print("R0",R0)
    # print("R1",R1)
    # print("R2",R2)
    # print("R3",R3)
    # print("R4",R4)
    # print("R5",R5)
    # print("R6",R6)
    # print("FLAGS",FLAGS)
    if(s=="000"):
        return R0
    elif(s=="001"):
        return R1
    elif(s=="010"):
        return R2
    elif(s=="011"):
        return R3
    elif(s=="100"):
        return R4
    elif(s=="101"):
        return R5
    elif(s=="110"):
        return R6
    elif(s=="111"):
        return FLAGS
    else:
    	return 0

counter=0

def print_output(x,c):
    # ---------------------------use to print (<PC (7 bits)><space><R0 (16 bits)><space>...<R6 (16 bits)><space><FLAGS (16 bits)>.)--------------------------------
    # ---------------------------with instruction(i) as argument x-------------------------------------------------------
    global FLAGS,R1,R2,R3,R4,R5,R6,R0,counter
    # print("-------------print_output--------------")
    # print("R0",R0)
    # print("R1",R1)
    # print("R2",R2)
    # print("R3",R3)
    # print("R4",R4)
    # print("R5",R5)
    # print("R6",R6)
    # print("FLAGS",FLAGS)
    # print("x",x)
    # for i in data_dic:
    #     print("dic",data_dic[i])
    #     if(data_dic[i]==x):
    #         key=i
    # print("key",key)
    # if(counter<=len(data_dic)):
    print(str(integer_to_binary_with_padding_for_dictionary(c))+"        "+integer_to_binary_with_padding(R0),integer_to_binary_with_padding(R1),integer_to_binary_with_padding(R2),integer_to_binary_with_padding(R3),integer_to_binary_with_padding(R4),integer_to_binary_with_padding(R5),integer_to_binary_with_padding(R6),FLAGS)
        # counter+=1
    # print()
    # print()




# ---------------------------------the value of all register is in integer except for FLAGS register--------------------------------r
# --------------------------------- I have made all the register variables as global variable so use the same name as global variable(i.e. R0,R1,R3.......FLAGS) for assigning the value to the registers -------------------- 
# ---------------------------------data_dic is the global dictionay with key as program counter and value as instruction-------------------
# ---------------------------------data_list is the global list with the instruction----------------------------------------------
# ---------------------------------use print_output function only for printing the output----------------------------------
# ------------------------------------pass i as parameter in print_output function---------------------------
# ------------------------------------i is the instruction code in all the ISA function given below----------------------------
# -----------------------------------just run the program and u will understand it--------------------------------





# -------------------------------------------write your code in the given function--------------------------------
def add(i,c):
    # print("add")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg1 = reg_dic(str(i[7:10]))
    reg2 = reg_dic(str(i[10:13]))
    reg3 = reg_dic(str(i[13:]))
    reg1 = int(reg2) + int(reg3)
    if(reg1<0 or reg1>127):
        FLAGS="0000000000001000"
        reg1=0
        assigning_value_in_global_var(i[7:10],reg1)
    else:
        assigning_value_in_global_var(i[7:10],reg1)
        FLAGS="0000000000000000"
    # print(reg1)
    print_output(i,c)

# -------------------------------------------satwik ends---------------------------------------------------------
# -------------------------------------------Sarthak strivatav starts--------------------------------------------
def sub(i,c):
    # print("sub")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg1 = reg_dic(str(i[7:10]))
    reg2 = reg_dic(str(i[10:13]))
    reg3 = reg_dic(str(i[13:]))
    reg1 = int(reg2) - int(reg3)
    if(reg1<0 or reg1>127):
        FLAGS="0000000000001000"
        reg1=0
        assigning_value_in_global_var(i[7:10],reg1)
    else:
        assigning_value_in_global_var(i[7:10],reg1)
        FLAGS="0000000000000000"
    print_output(i,c)

def mov_imm(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    # print("mov_imm")
    # print(i)
    reg = reg_dic(str(i[6:9]))
    imm_bin = ((i[9:]))
    imm_int = int(imm_bin, 2)
    reg = imm_int
    # print(reg)
    assigning_value_in_global_var(i[6:9], reg)
    FLAGS="0000000000000000"
    # print(reg_dic)
    print_output(i,c)

def mov_reg(i,c):
    # print("mov_reg")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg1 = reg_dic(str(i[10:13]))
    reg2 = reg_dic(str(i[13:]))
    # print("reg1",reg1)
    # print("reg2",int(reg2))
    reg1 = int(reg2)
    
    assigning_value_in_global_var(i[10:13],reg1)
    FLAGS="0000000000000000"
    print_output(i,c)

def load(i,c):
    # print("load")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg = reg_dic(str(i[6:9]))
    mem_addr = int(i[9:],2)
    reg=int(mem_dump[mem_addr],2)
    assigning_value_in_global_var(str(i[6:9]), reg)
    FLAGS="0000000000000000"
    print_output(i,c)
    # print(i)

def store(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg = reg_dic(str(i[6:9]))
    mem_addr = int(i[9:],2)
    mem_dump[mem_addr]=integer_to_binary_with_padding(reg)
    #assigning_value_in_global_var(str(i[6:9]), reg)
    FLAGS="0000000000000000"
    print_output(i,c)
    # print("store")
    # print(i)

def multiply(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg1=reg_dic(i[10:13])*reg_dic(i[13:])
    assigning_value_in_global_var(i[7:10],reg1)
    FLAGS="0000000000000000"
    if(reg1<0 or reg1>127):
        FLAGS="0000000000001000"
        reg1=0
    
    print_output(i,c)
    # print("mulyiply")
    # print(i)

def divide(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    if(reg_dic(i[13:])==0):
        FLAGS="0000000000001000"
        reg0=0
        reg1=0
        assigning_value_in_global_var("000", reg0)
        assigning_value_in_global_var("001", reg1)
    else:
        reg0=int(reg_dic(i[10:13]))//int(reg_dic(i[13:]))
        reg1=int(reg_dic(i[10:13]))%int(reg_dic(i[13:]))
        assigning_value_in_global_var("000", reg0)
        assigning_value_in_global_var("001", reg1)
        FLAGS="0000000000000000"
    print_output(i,c)
    # print("divide")
    # print(i)

def right_shift(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg=reg_dic(i[6:9])
    # print(reg)
    imm=int((i[9:]),2)
    # print(imm)
    # # imm=int(imm,2)
    reg=reg>>imm
    # print(reg)
    assigning_value_in_global_var(i[6:9], reg)
    FLAGS="0000000000000000"
    print_output(i,c)
    # print("right shift")
    # print(i)

def left_shift(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg=reg_dic(i[6:9])
    # print(reg)
    imm=int((i[9:]),2)
    # print(imm)
    # # imm=int(imm,2)
    reg=reg<<imm
    # print(reg)
    assigning_value_in_global_var(i[6:9], reg)
    FLAGS="0000000000000000"
    print_output(i,c)
    # print("left shift")

    # print(i)

# -------------------------------------------Sarthak strivatav ends------------------------------------------------------------
# -------------------------------------------Saarthak saxena starts------------------------------------------------------------
def exclusive_OR(i,c):
    # print("exculsive or")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    # reg1=reg_dic[i[7:10]]
    reg2=reg_dic(i[10:13])
    reg3=reg_dic(i[13:])
    reg1=int(reg2)^int(reg3)
    assigning_value_in_global_var(i[7:10],reg1)
    FLAGS="0000000000000000"
    print_output(i,c)
    # return reg1
    
def OR(i,c):
    # print("or")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    # reg1=reg_dic[i[7:10]]
    reg2=reg_dic(i[10:13])
    reg3=reg_dic(i[13:])
    reg1= int(reg2)|int(reg3)
    assigning_value_in_global_var(i[7:10],reg1)
    FLAGS="0000000000000000"
    print_output(i,c)
    # return reg1
    

def AND(i,c):
    # print("And")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0    
    reg2=reg_dic(i[10:13])
    reg3=reg_dic(i[13:])
    reg1= reg2&reg3
    assigning_value_in_global_var(i[7:10],reg1)
    FLAGS="0000000000000000"
    print_output(i,c)
    # return reg1
    
def invert(i,c):
    # print("Invert")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    # reg1=reg_dic(i[10:13])
    # print("    ",i[10:13])
    reg1=""
    reg2=reg_dic(i[13:])
    reg2_bin=integer_to_binary_with_padding_for_dictionary(reg2)
    for j in reg2_bin:
        if(j=="0"):
            reg1+="1"
        else:
            reg1+="0"
    reg1=int((reg1),2)
    # print("r1",reg1)
    # print("r2",reg2)
    s=i[10:13]
    # print("s",s)
    assigning_value_in_global_var(s,reg1)
    FLAGS="0000000000000000"
    print_output(i,c)
    # return reg1

def compare(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    # print("compare")
    reg1=reg_dic(str(i[10:13]))
    reg2=reg_dic(i[13:])
    # print(reg1,reg2)
    if(int(reg1)<int(reg2)):
        FLAGS="0000000000000100"
    elif(int(reg1)>int(reg2)):
        FLAGS="0000000000000010"
    elif(int(reg1)==int(reg2)):
        FLAGS="0000000000000001"
    print_output(i,c)


def unconditional_jump(i,c):
    # print("jmp")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    
    
    mem_add=i[9:]
    # print("            ",int(mem_add,2))
    FLAGS="0000000000000000"
    print_output(i,c)
    return int(mem_add,2)-1

def jump_if_less_than(i,c):
    # print("jlt")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    
    
    if(FLAGS[-3]=="1"):
        mem_add=i[9:]
        FLAGS="0000000000000000"
        print_output(i,c)
        return int(mem_add,2)-1
    FLAGS="0000000000000000"
    print_output(i,c)
    return data_list.index(i)
    

def jump_if_greater_than(i,c):
    # print("jgt")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    
    
    if(FLAGS[-2]=="1"):
        # print("hi")
        mem_add=i[9:]
        # print(int(mem_add,2)-1)
        FLAGS="0000000000000000"
        print_output(i,c)
        return int(mem_add,2)-1
    FLAGS="0000000000000000"
    print_output(i,c)
    return data_list.index(i)

def jump_if_equal(i,c):
    # print("je")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    
    
    if(FLAGS[-1]=="1"):
        mem_add=i[9:]
        FLAGS="0000000000000000"
        print_output(i,c)
        return int(mem_add,2)-1
    FLAGS="0000000000000000"
    print_output(i,c)
    return data_list.index(i)

def halt(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    FLAGS="0000000000000000"
    print_output(i,c)
    mem_dum()
    # print(mem_dump)
    

# -------------------------------------------Saarthak saxena ends------------------------------------------------------------
# -------------------------------------------Satkeerat starts------------------------------------------------------------

def addf(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg2=reg_dic(i[10:13])
    reg3=reg_dic(i[13:])
    reg1=reg2+reg3
    if(reg1<0 or reg1>127):
        FLAGS="0000000000001000"
        reg1=0
        assigning_value_in_global_var(i[7:10],reg1)
    else:
        assigning_value_in_global_var(i[7:10],reg1)
        FLAGS="0000000000000000"
    print_output(i,c)

def subf(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg2=reg_dic(i[10:13])
    reg3=reg_dic(i[13:])
    reg1=reg2-reg3
    if(reg3>reg2):
        FLAGS="0000000000001000"
        reg1=0
        assigning_value_in_global_var(i[7:10],reg1)
    else:
        assigning_value_in_global_var(i[7:10],reg1)
        FLAGS="0000000000000000"
    print_output(i,c)

# def movf(i):
#     reg1=



def call_other_function(data_dic,data_list):
    c=0
    k=0
    # ----------------------------------function used for calling other functions------------------
    # for i in range(0,len(data_dic),1):
        # print(i)
    while(k<100 and c<len(data_dic)):
        # print(c)
        # print((integer_to_binary_with_padding_for_dictionary(c)))
        if(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="00000"):
            (add(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="00001"):
            # print(c)
            # print(data_dic[integer_to_binary_with_padding_for_dictionary(c)])
            (sub(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="00010"):
            (mov_imm(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="00011"):
            (mov_reg(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="00100"):
            (load(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="00101"):
            (store(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="00110"):
            (multiply(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="00111"):
            (divide(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="01000"):
            (right_shift(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="01001"):
            (left_shift(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="01010"):
            (exclusive_OR(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="01011"):
            (OR(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="01100"):
            (AND(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="01101"):
            (invert(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="01110"):
            compare(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c)
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="01111"):
            c=int(unconditional_jump(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
            # print(("c",c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="11100"):
            c=int(jump_if_less_than(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
            # print(("c",c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="11101"):
            c=int(jump_if_greater_than(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
            # print(("c",c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="11111"):
            c=int(jump_if_equal(data_dic[integer_to_binary_with_padding_for_dictionary(c)],c))
            # print(("c",c))
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="10000"):
            # print(print_output(data_dic[integer_to_binary_with_padding_for_dictionary(c)]))
            addf((data_dic[integer_to_binary_with_padding_for_dictionary(c)]),c)
            
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="10001"):
            # print(print_output(data_dic[integer_to_binary_with_padding_for_dictionary(c)]))
            subf((data_dic[integer_to_binary_with_padding_for_dictionary(c)]),c)
            
        # elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="10010"):
        #     # print(print_output(data_dic[integer_to_binary_with_padding_for_dictionary(c)]))
        #     movf((data_dic[integer_to_binary_with_padding_for_dictionary(c)]))
            
        elif(data_dic[integer_to_binary_with_padding_for_dictionary(c)][:5]=="11010"):
            # print(print_output(data_dic[integer_to_binary_with_padding_for_dictionary(c)]))
            halt((data_dic[integer_to_binary_with_padding_for_dictionary(c)]),c)
            quit()
        
        c+=1
        k+=1
        
        

# --------------------------------main function---------------------------------------
# ---------------------------------taking input------------------------------------------------
data_list=[]
# print("HI")
while True:
    try:
        testline=input()
        data_list.append(testline)
        # print(data_list)
    except EOFError:
        break
# for i in range(0,7,1):
#     inp=input()
#     data_list.append(inp)
    # print(data_list)
data_dic={}
# dictionary with key as binary 7bit number(counter) and value as opcode

k=0
for i in data_list:
    data_dic[str(format(k,'b').rjust(7,'0'))]=i 
    k+=1

# print(data_dic)

mem_dump=[]
for i in data_list:
    mem_dump.append(i)
    # print(mem_dump)

for i in range(len(data_list),128,1):
    mem_dump.append(integer_to_binary_with_padding(0))
# print(len(mem_dump))    

# ------------------------------------just print these two and u will understand the input data-------------------
# print("data_dic    ",data_dic)
# print("data_list    ",data_list)

call_other_function(data_dic, data_list)

#--------------------------------------------------Satkeerat ends -------------------------------------------------

