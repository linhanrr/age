driving = input('你有沒有開過車?')
if driving != '有' and driving != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit 
age = input('你今年幾歲?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('你通過測驗了')
    else:
        print('??你怎麼會有開過車??')
elif driving == '沒有':
    if age >= 18:
        print('奇怪，你可以考駕照了，怎麼還不去考阿')
    else:
        print('很好，再過幾年就可以去考了')

