from PIL import Image
import os
import random

def val_tuple(x):
    return x[0]

def getImageMatrix_tuple(image):#it takes the image having tuples as pixels
    im = Image.open(image)  # Can be many different formats.
    pix = im.load()
    image_size = im.size #Get the width and height of the image for iterating over
    print("Image Size : ",image_size)
    image_matrix = []
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
            try:
                row.append((binarySequence((val_tuple(pix[width,height])))))
            except:
                row=[(binarySequence((val_tuple(pix[width,height]))))]
        try:
            image_matrix.append(row)
        except:
            image_matrix = [row]
    return image_matrix  #return binary sequence of pixel values of an image

def getImageMatrix_list(image):#it takes the image as lists
    im = Image.open(image)  # Can be many different formats.
    pix = im.load()
    image_size = im.size #Get the width and height of the image for iterating over
    print("Image Size : ",image_size)
    image_matrix = []
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
            try:
                row.append((binarySequence((pix[width,height]))))
            except:
                row=[(binarySequence((pix[width,height])))]
        try:
            image_matrix.append(row)
        except:
            image_matrix = [row]
    return image_matrix  #return binary sequence of pixel values of an image

def getChaoticSequence(image):#it takes image as input
    im = Image.open(image)  # Can be many different formats.
    image_size = im.size #Get the width and hight of the image for iterating over
    print("Image Size : ",image_size)
    image_matrix = []
    x=0.2 #seed value
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
            try:
                xn = (x*(1-x)*random.uniform(3.5,4))
                x = xn
                row.append(genKEY(binarySequence(int(xn*255)),RightShiftRegister(binarySequence(int(xn*255)))))
            except:
                row=[genKEY(binarySequence(int(xn*255)),RightShiftRegister(binarySequence(int(xn*255))))]
        try:
            image_matrix.append(row)
        except:
            image_matrix = [row]
    return image_matrix  #returns the key of image in binary

def getCipher_im(image_mat,key_mat):
    cipher=[]
    for i in range(im_width):
        for j in range(im_height):
            try:
                cipher.append(DeciOfBin(genKEY(image_mat[i][j],key_mat[i][j])))
            except:
                cipher = [DeciOfBin(genKEY(image_mat[i][j],key_mat[i][j]))]
    return cipher # returns cipher in decimal

def getCipher(image_mat,key_mat):
    cipher=[]
    for i in range(im_width):
        for j in range(im_height):
            try:
                cipher.append((genKEY(image_mat[i][j],key_mat[i][j])))
            except:
                cipher = [(genKEY(image_mat[i][j],key_mat[i][j]))]
    return cipher # returns cipher in binary
    
def RightShiftRegister(binary):
    take = [1,0,1,0,1,0,1,0]
    count=0
    for i in range(len(binary)):
        if take[i]==1 and binary[i]==1:
            count = count +1# even parity
    if(count%2!=0):#odd number # XOR operation
        appendbit=1
    else:
        appendbit=0
    for i in range(6,-1,-1):
        binary[i+1] = binary[i]
    binary[0]=appendbit
    return binary  #Returns right shifted bits by appending XOR bit infront
    
def binarySequence(n):#it takes decimal values
    counter=8
    bitseq=[]
    while(True):
        q=n/2
        r=n%2
        n=q
        counter = counter-1
        try:
            bitseq.append(int(r))
        except:
            bitseq = [r]
        if(counter<=0):
            break
    try:
        bitseq.reverse()
    except:
        bitseq= []
    return bitseq # Converts the decimal value of pixels in binary

def genKEY(list1,list2):#it takes two lists for XOR
    key=[]
    for i in range(len(list1)):
        try:
            key.append(list1[i] ^ list2[i])
        except:
            key = [list1[i] ^ list2[i]]
    return key    # Returns Key in Binary

def DeciOfBin(binary):
    decimal = 0
    for bit in binary:
        decimal = decimal * 2 + int(bit)
    return decimal
###############################################GLOBAL Variables######################################
file_name="1.png"
cipher_file_name="*new_cipher.bmp"
im = Image.open(file_name)  # Can be many different formats.
size = im.size
im_width=size[0]
im_height=size[1]
#####################################################################################################
def LogMapEncrypt(size,cipher_mat):#it takes cipher matrix as input
    r=0
    j=0
    c=0
    im = Image.new("L", (size[0],size[1]))
    pix = im.load()
    for i in range(0,im_width*im_height):
        if c<im_height:
            pix[r,c]=cipher_mat[j]
            j=j+1
            c=c+1
        else:
            r=r+1
            c=0
            pix[r,c]=cipher_mat[j]
            j=j+1
    im.save(cipher_file_name,"BMP")
    absPath = os.path.abspath(cipher_file_name)
    return absPath #generates thr path of encrypted image
#########################################################################################################
def MatrixToImage(size,matrix):#input as matrix of form : [[1,2,3...],[1,2,3,....]]values in decimals
    im = Image.new("L", (size[0],size[1]))
    pix = im.load()
    for i in range(int(size[0])):
        for j in range(int(size[1])):
            pix[i,j]=matrix[i][j]
    im.save(cipher_file_name,"BMP")
    absPath = os.path.abspath(cipher_file_name)
    return absPath #generates thr path of image
                
    
##########################################################################################################
def compare_list(x,y):#it compares [1,0]and[0,1]
    if x[0]==y[0] and x[1]==y[1]:
        z=1
    else:
        z=0
    return z

def PositionToBase(x):#it takes position value 
    if x==0:
        z='A'     #00
    elif x==1:
        z='C'     #01
    elif x==2:
        z='G'     #10
    else:
        z='T'     #11
    return z  # returns 'base' according to its position
      
def make_DNA_strand(strand):#[[1,2,3,4],[1,2,3,4],[],[],[],[]]
    whole_strand=[]
    for i in range(im_width*im_height):
        base_strand=[]
        for j in range(0,8,2):
            base = []
            try:
                base.append(strand[i][j])
                base.append(strand[i][j+1])
                base_strand.append(base)
            except:
                base = [strand[i][j]]
                base = [strand[i][j+1]]
                base_strand = [base]
        try:
            whole_strand.append(base_strand)
        except:
            whole_strand = [base_strand]
    return whole_strand   #[[[1],[2],[3],[4]],[[1],[2],[3],[4]],[[],[],[],[]],[[],[],[],[],[]]]
            
def DNA_encoding(whole_strand):#[[[1],[2],[3],[4]],[[1],[2],[3],[4]],[[],[],[],[]],[[],[],[],[],[]]]
    dna_cipher=[]
    for i in range(im_width*im_height):
        try:
            dna_cipher.append(strand_DNA(whole_strand[i],i%8))#rules keeps changing in different strands
        except:
            dna_cipher = [strand_DNA(whole_strand[i],i%8)]
    return dna_cipher #[['a','t','c','g'],['a','t','c','g']]

def strand_DNA(strand,rule):#[[1,0],[0,1],[1,1],[0,0]]
    DNA_seq=[]   #DNA=[A,T,C,G]
    for i in range(4):
       for j in range(4):
           if compare_list(strand[i],DNA[rule][j])==1:#if matched
               position=j
               try:
                   DNA_seq.append(PositionToBase(position))
               except:
                   DNA_seq = [PositionToBase(position)]
    return DNA_seq# return list [ ''base','base'.....  ]
###########################################################################################################
DNA=[[[0,0],[1,1],[0,1],[1,0]],[[0,0],[1,1],[1,0],[0,1]],[[1,1],[0,0],[0,1],[1,0]],[[1,1],[0,0],[1,0],[0,1]],[[0,1],[1,0],[0,0],[1,1]],[[0,1],[1,0],[1,1],[0,0]],[[1,0],[0,1],[0,0],[1,1]],[[1,0],[0,1],[1,1],[0,0]]]
###########################################################################################################

def ListIntoString(DNA_strands):#converts list into string
    dna_string=""
    for j in range(len(DNA_strands)):
        for i in range(4):
            dna_string=dna_string+DNA_strands[j][i]
    return dna_string

def main():
    im = Image.open(file_name)# open the image file
    pix=im.load()             #load its pixels
    if type(pix[0,0]) is tuple:     #check for tuple or not
        im=(getImageMatrix_tuple(file_name))
    else:
        im=(getImageMatrix_list(file_name))
        
#    print(MatrixToImage(size,im))
    im_key=getChaoticSequence(file_name)
#    print(im_key)
#    im=getImageMatrix_tuple(file_name)
#    print(im)
#    print(LogMapEncrypt(size,getCipher_im(im,im_key)))
    file = open('DNA_sequence.doc','w') 
    file.write(ListIntoString(DNA_encoding(make_DNA_strand(getCipher(im,im_key)))))
    print("File saved")
    file.close() 
    
if __name__ == "__main__":
    main()