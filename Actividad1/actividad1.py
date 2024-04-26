###########################################
# Victoria Rodríguez de León              #                                       
# A01656328                               #                                        
# Actividad 1  |  Video functions         #                                       
###########################################

import cv2

# GRABADO Y GUARDADO DE PRIMER VIDEO
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('act1_normalvid.mp4', cv2.VideoWriter_fourcc(*'mp4v'),20,(width,height))
while True:
    ret,frame = cap.read() # Lectura de frames
    if cv2.waitKey(1)&0xFF == ord('q'): # cuando aprietas tecla q y pasa un segundo se cierra
        break
    writer.write(frame)
    cv2.imshow('frame',frame)
cap.release()
writer.release()
cv2.destroyAllWindows()

# VIDEO EN REVERSA
cap = cv2.VideoCapture("act1_normalvid.mp4")
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# grab current frame
check,vid = cap.read()
frame_list = []

while(check):
    check,vid = cap.read()
    frame_list.append(vid)
frame_list.pop()
frame_list.reverse()

# create videowriter2
writer2 = cv2.VideoWriter('act1_reversed.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

for frame in frame_list:
    # por cada frame ya invertido, se muestra en pantalla y se guarda.
    writer2.write(frame)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
writer2.release()
cv2.destroyAllWindows()

# JOINED VIDEO
writer_comb = cv2.VideoWriter('act1_combined.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))
cap = cv2.VideoCapture("act1_normalvid.mp4")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    writer_comb.write(frame)

cap.release()  
cap = cv2.VideoCapture("act1_reversed.mp4")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    writer_comb.write(frame)
cap.release()  

writer_comb.release()
cv2.destroyAllWindows()
