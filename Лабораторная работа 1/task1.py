numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
before_none= numbers[:4]
after_none= numbers[5:]
without1=before_none+after_none
total=sum(without1)
count=len(without1)+1
average=total/count
numbers[4]=average
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)

