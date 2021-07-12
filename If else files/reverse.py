
# reverse the 4 digit number

number=int(input("Enter the  4 didgit number"))
first=number%10
second=(number//10)%10
third=(number//100)%10
fourth=(number//1000)%10
reverse=(first*1000)+(second*100)+(third*10)+(fourth*1)

# if the number is of 4 digit so it will reverse

if number>=1000 and number<=10000:
    print(reverse)
else:
    print("you can't reverse the 5 digit number")
