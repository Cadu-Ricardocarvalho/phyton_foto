import cv2
img = cv2.imread("shirek_color.jpg"   , cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
enhance = cv2.detailEnhance(img)
cv2.imshow('shirek', enhance)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("shirek_result.jpg", img)
