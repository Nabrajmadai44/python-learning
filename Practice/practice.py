# #String slicing
# word = 'Navya'
# sl=word[1:5]
# print(sl)
# sl1 = word[1:4:2]
# print(sl1)
# w = "amazing"
# sll=w[1:6:2]
# print(sll)


# #string functions 

# word = "python hello devil"
# w=len(word)
# print(w)
# w1=word.count("python")
# print(w1)
# print(word.capitalize())
# print(word.endswith("on"))
# print(word.find("devil"))
# print(word.replace("hello","language is"))

# Name = input("Good Morning ")
# print(Name)




# def GFG(name, num):
#     print("Hello from ", name + ', ' + num)

# GFG("geeks for geeks", "25")



#  WAF to convert USD to NPR

value = int(input("Enter USD that you want to convert: "))
def converter(usd_value):
    NPR_value = usd_value * 138 # 1 usd = 138 npr
    print(f'{usd_value} USD = {NPR_value} NPR')

converter(value)



