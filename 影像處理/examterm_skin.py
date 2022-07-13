import numpy as np
import cv2


	
def skin_color_detection( f, method ):
	g = f.copy()
	g.fill( 0 )
	nr, nc = f.shape[:2]
    
	gray = cv2.cvtColor( f, cv2.COLOR_BGR2GRAY )
	face_cascade = cv2.CascadeClassifier( 'haarcascade_frontalface_default.xml' )
	faces = face_cascade.detectMultiScale( gray, 1.1, 5 )
	for ( x0, y0, w, h ) in faces:
		g = cv2.rectangle( g, ( x0, y0 ), ( x0 + w, y0 + h ), ( 255, 0, 0 ), 2 )
	x1,y1=x0+w,y0+h

	if method == 1:  # RGB Approach
		for x in range( nr ):
			for y in range( nc ):
				B = int( f[x,y,0] )
				G = int( f[x,y,1] )
				R = int( f[x,y,2] )
				if R > 95 and G > 40 and B > 20 and \
					max(R,G,B) - min(R,G,B) > 15 and \
					abs( R- G ) > 15 and R > G and R > B and y>x0 and x>y0 and y<x1 and x<y1:
                    
					g[x,y,0] = g[x,y,1] = g[x,y,2] = 255

	elif method == 2:  # HSV Approach
		hsv = cv2.cvtColor( f, cv2.COLOR_BGR2HSV )
		for x in range( nr ):
			for y in range( nc ):
				H = int( hsv[x,y,0] * 2 )
				S = float( hsv[x,y,1] / 255 )
				if ( ( ( H > 0 and H < 50 ) or \
					   ( H > 320 and H < 360 ) ) and 
					   ( S > 0.23 and S < 0.68 ) ):
					g[x,y,0] = g[x,y,1] = g[x,y,2] = 255

	else:  # YCrCb Approach
		ycrcb = cv2.cvtColor( f, cv2.COLOR_BGR2YCrCb )
		for x in range( nr ):
			for y in range( nc ):
				Cr = int( ycrcb[x,y,1] )
				Cb = int( ycrcb[x,y,2] )
				if ( Cb >= 77 and Cb <= 127 and \
					 Cr >= 133 and Cr <= 173 ):
					g[x,y,0] = g[x,y,1] = g[x,y,2] = 255
	return g

def main( ):
	img1 = cv2.imread( "Akiyo.bmp", -1 )
	img2 = skin_color_detection( img1, 1 )
    
	cv2.imshow( "Face Detection Image", img1 )
   
	cv2.imshow( "Skin Color Detection", img2 )
	cv2.waitKey( 0 )

main( )