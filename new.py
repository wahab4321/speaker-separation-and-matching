
 imgOld = cv2.imread('th.jpg') # read image into a numpy array imgNew =
 imgOld (imgH, imgW, imgC) = imgOld.shape # imgC = 2 or 4 (RGB or RGBA)
 
 plt.imshow(imgOld, vmin=0, vmax=255) plt.show()
 
 # blur for y in range(imgH):
     for x in range(imgW):
         xLast = 0
         yLast = 0
         if x != 0 and y != 0:
             xLast = (x-1) % imgW
             yLast = (y-1) % imgH
         else:
             xLast = 0
             yLast = 0
         xNext = (x+1) % imgW
         yNext = (y+1) % imgH
         rgb = imgNew[y,x]
 
         aux_r = (imgOld[yLast,xLast,2],
                       imgOld[yLast,x,2],
                       imgOld[yLast,xNext,2],
                       imgOld[y,xLast,2],
                       imgOld[y,x,2],
                       imgOld[y,xNext,2],
                       imgOld[yNext,xLast,2],
                       imgOld[yNext,x,2],
                       imgOld[yNext,xNext,2])
         r = sum(aux_r)
         r = r/9
         aux_g = (imgOld[yLast,xLast,1],
                       imgOld[yLast,x,1],
                       imgOld[yLast,xNext,1],
                       imgOld[y,xLast,1],
                       imgOld[y,x,1],
                       imgOld[y,xNext,1],
                       imgOld[yNext,xLast,1],
                       imgOld[yNext,x,1],
                       imgOld[yNext,xNext,1])
         g = sum(aux_g)
         g = g/9
 
         aux_b = (imgOld[yLast,xLast,0],
                       imgOld[yLast,x,0],
                       imgOld[yLast,xNext,0],
                       imgOld[y,xLast,0],
                       imgOld[y,x,0],
                       imgOld[y,xNext,0],
                       imgOld[yNext,xLast,0],
                       imgOld[yNext,x,0],
                       imgOld[yNext,xNext,0])
         b = sum(aux_b)
         b = b/9
             
         imgNew[y,x] = [b,g,r] plt.imshow(imgNew, vmin=0, vmx=255) plt.show()