public_toilet = "PB"

def home():
    private_toilet = "PT"
    print(private_toilet)

def stranger():
    print(public_toilet)
    #print(private_toilet) (local variable defined in above function can't be used here)
#print(private_toilet)(local variable defined in above function can't be used outside)
home()
stranger()
