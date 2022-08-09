gr, sc = map(int, input("졸업학점과 이수학점를 입력하세요:").split(','))
# gr = int(input()) 
# sc = int(input())

print("졸업학점은",gr)
print("이수학점은",sc)
if gr>=2 and sc>=140 :
  print("졸업가능")
elif gr<2 and sc >= 140:
  print("졸업학점 부족으로 인한 졸업 불가능")
elif gr>=2 and sc < 140:
  print("이수학점 부족으로 인한 졸업 불가능")
else:
  print("졸업학점과 이수학점 둘 다 부족합니다. 졸업불가능")