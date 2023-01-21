def funargs(normal, *argswisher, **kwargswisher):
    print(normal)
    for item in argswisher:
        print(item)
    print("\nLet's introduce some of our members:")
    for key,value in kwargswisher.items():
        print(f"{key} is a {value}")
n = "These are our Students"
withargs = ["Bhushan", "Tanmay","Aadi", "Goti", "Rushi"]
withkw = {"Leader": "Badshah", "Coleader":"Panther", "Elite":"Thor","Member":"Iconic"}

funargs(n,*withargs,**withkw)