

import cv2
 
# 读取图像  
image = cv2.imread("opencv_logo.jpg")  
  
# 检查图像是否正确读取  
if image is None:  
    print("Error: Could not read the image.")  
    exit()  
  
# 分别显示蓝色、绿色和红色通道  
cv2.imshow("blue", image[:, :, 0])  
cv2.imshow("green", image[:, :, 1])  
cv2.imshow("red", image[:, :, 2])  
  
# 转换为灰度图像并显示  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
cv2.imshow("gray", gray)  
  
# 等待按键事件，0 表示无限等待  
cv2.waitKey(0)  
  
# 销毁所有窗口  
cv2.destroyAllWindows()

