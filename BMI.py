#計算BMI程式
print('計算您的BMI')
height = float(input('請輸入您的身高(cm)'))
weight = float(input('請輸入您的體重(kg)'))
bmi = weight /((height / 100)*(height / 100))
#bmi = float(weight / (height / 100) ^ 2)
print('您的BMI為 %3d' % (bmi))
if bmi < 18.5 :
	print('太瘦了喔~')
elif 18.5 <= bmi < 24 :
	print('您的身材剛剛好~')
elif 24 <= bmi < 27 :
	print('您有點胖喔')
elif 27 <= bmi < 30 :
	print('輕度肥胖喔')
elif 30 <= bmi < 35 :
	print('中度肥胖喔')
else:
	print('太胖嚕~')