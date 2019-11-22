from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
def entropy(signal):
    '''
    function returns entropy of a signal
    signal must be a 1-D numpy array
    '''
    lensig=signal.size
    symset=list(set(signal))
    numsym=len(symset)
    propab=[np.size(signal[signal==i])/(1.0*lensig) for i in symset]
    ent=np.sum([p*np.log2(1.0/p) for p in propab])
    return ent
colorIm=Image.open('chest-xary-cipher.jpg')
greyIm=colorIm.convert('L')
colorIm=np.array(colorIm)
greyIm=np.array(greyIm)
N=5
S=greyIm.shape
E=np.array(greyIm)
for row in range(S[0]):
    for col in range(S[1]):
        Lx=np.max([0,col-N])
        Ux=np.min([S[1],col+N])
        Ly=np.max([0,row-N])
        Uy=np.min([S[0],row+N])
        region=greyIm[Ly:Uy,Lx:Ux].flatten()
        E[row,col]=entropy(region)
                
plt.subplot(1,3,1)
plt.imshow(colorIm)
plt.xlabel('Original Image')
#plt.subplot(1,4,2)
#plt.imshow(greyIm, cmap=plt.cm.gray)

plt.subplot(1,3,3)
plt.imshow(E, cmap=plt.cm.jet)
plt.xlabel('Entropy in 10x10 neighbourhood')
plt.colorbar()

plt.show()