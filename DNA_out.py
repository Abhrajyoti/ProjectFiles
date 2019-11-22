from PIL import Image
import os
import random
#from itertools import chain 
from functools import reduce

def getImageMatrix(image):#it takes the image
    im = Image.open(image)  # Can be many different formats.
    pix = im.load()
    #print(type(pix[0,1]))
    #print(pix[0,1][0])
    
    image_size = im.size #Get the width and height of the image for iterating over
    print("Image Size : ",image_size)
    image_matrix = []
    row = []
    if(type(pix[0,1]) == type(5)):
        for width in range(int(image_size[0])):
            row = []
            for height in range(int(image_size[1])):
                try:
                    row.append(binarySequence(pix[width,height]))
                except:
                    row=[binarySequence(pix[width,height])]
            try:
                image_matrix.append(row)
            except:
                image_matrix = [row]
        return tuple(i for i in image_matrix)  #return binary sequence of pixel values of an image Changed here
    else:
        for width in range(int(image_size[0])):
            row = []
            for height in range(int(image_size[1])):
                try:
                    row.append(binarySequence(pix[width,height][0]))
                except:
                    row=[binarySequence(pix[width,height][0])]
            try:
                image_matrix.append(row)
            except:
                image_matrix = [row]
                
#    print(row)
#    print(LogMapEncrypt(size,row))
#        image_mat=[image_matrix]
    return image_matrix #Changed here



def getChaoticSequence(image):#it takes image as input
    im = Image.open(image)  # Can be many different formats.
    image_size = im.size #Get the width and hight of the image for iterating over
    print("Image Size : ",image_size)
    image_matrix = []
    x=random.random() #seed value
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
            try:
                xn = (x*(1-x)*4)
                x = xn
                row.append(genKEY(binarySequence(int(xn*255)),RightShiftRegister(binarySequence(int(xn*255)))))
            except:
                row=[genKEY(binarySequence(int(xn*255)),RightShiftRegister(binarySequence(int(xn*255))))]
        try:
            image_matrix.append(row)
        except:
            image_matrix = [row]
    return image_matrix  #returns the key of image in binary

def getCipher(image_mat,key_mat):
    cipher=[]
    for i in range(im_width):
        for j in range(im_height):
            try:
                cipher.append(genKEY(image_mat[i][j],key_mat[i][j]))
            except:
                cipher = [(genKEY(image_mat[i][j],key_mat[i][j]))]
#    cipher_matrix=[cipher]
    return cipher # returns cipher in binary Changed here
    
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
    return binary  #Returns right shifted bits by appending XOR bit infront Changed here
    
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
    return bitseq # Converts the decimal value of pixels in binary Chnaged here

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
###############################################GLOBAL Variables
file_name="1.png"
cipher_file_name="1_cipher.bmp"
image_org = "Image_int.bmp"
im = Image.open(file_name)  # Can be many different formats.
#r,g,b = im.split()
#im = Image.merge("RGB",(r,g,b))
#im.save("tesMRI.bmp")
size = im.size
im_width=size[0]
im_height=size[1]
image_mat=[]
#cipher_matrix = []
###############################################
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
#    im.save(image_org,"BMP")
    absPath = os.path.abspath(cipher_file_name)
    return absPath #generates thr path of encrypted image

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
    return dna_cipher #[['a','t','c','g'],['a','t','c','g']] CHanging here

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
    return DNA_seq# return list [ ''base','base'.....  ] CHanged here
###########################################################################################################
DNA=[[[0,0],[1,1],[0,1],[1,0]],[[0,0],[1,1],[1,0],[0,1]],[[1,1],[0,0],[0,1],[1,0]],[[1,1],[0,0],[1,0],[0,1]],[[0,1],[1,0],[0,0],[1,1]],[[0,1],[1,0],[1,1],[0,0]],[[1,0],[0,1],[0,0],[1,1]],[[1,0],[0,1],[1,1],[0,0]]]
###########################################################################################################
def main():
    im_key=getChaoticSequence(file_name)
    im=getImageMatrix(file_name)
    lst = []
    print(type(lst))
    str=""
#    print(LogMapEncrypt(size,getCipher(im,im_key)))
    lst = (DNA_encoding(make_DNA_strand(getCipher(im,im_key))))
#    print(lst)
    f = open("output5.txt","w+")
    # Image converted to a integer image
    for i in range(len(lst)):
#        f.write('(')
        f.write(str.join(lst[i]))
#        f.write(')')
#        f.write(lst[i])
    
#    print(lst)
    f.close()
if __name__ == "__main__":
    main()