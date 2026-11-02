# import random
# def number():
#     num=random.randint(1,100)
#     return num
# print(number()) 

# title = input("Link title: ")
# url = input("Link URL: ")
# rating = int(input("Rating (1-5): "))
# print(f"{title} - {url} - rated {rating}/5")
# print("*" * rating)

# url = input("enter the url: ")
# clean_url = url.lower().strip()
# print(clean_url.startswith("https"))
# domain = clean_url.split("//")[-1].split("/")[0]
# print(domain)

#basic loops

# rating =4
# if rating>=4 and rating <=5:
#     print("hello")

# rating=int(input("enter a num(1-5)"))
# if rating <2 :
#     print("user not satisfied")
# elif rating >= 3:
#     print("user satisfied")
# else:
#     print("invalid output")

url = input("enter the url: ")
domain = url.replace("https://", "").replace("http://", "").split("/")[0]
if domain.endswith(".com"):
    print("its a domain")
else:
    print("not a domain")