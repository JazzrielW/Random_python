#GLOBAL VARIABLES
expand = 5  #how many primes we'll be counting/2
liars_list = []
liars_list = [[0,0] for i in range(2*expand)] # counts how many times a witness lies/tells the truth
#

def power_mod(base,power,mod): #obtaining the modulo of large numbers without calculating
    residue = 1
    count = 1
    while count<=power:
        residue = residue*base
        residue = residue%mod
        count += 1
    return(residue)

def test_number(prime):
    #print(prime)
    divisible = True
    temp = prime-1
    power = 0
    while divisible:
        if temp%2 == 0:
            power +=1
            temp = temp/2
        else:
            divisible=False
    # prime = 2^power * temp +1
    #print(str(prime)+"= 2**"+str(power)+" *"+str(temp)+"+1")
    witness=1
    results = [True] #Index 0 reserved. If True number is prime
    while witness<prime:
        #print(witness)
        twos_test=False
        for extra_twos in range(power):
            exponential_twos =temp*2**extra_twos #will test for every exponent multiplied by pwrs of 2<power
            modulo = power_mod(witness,exponential_twos,prime)
            #print(modulo)
            modulo_test =  modulo==1 or modulo+1 == prime
            twos_test = twos_test or modulo_test #if modulo_test ever gives true, the whole test is positive
        if twos_test:
            results.append(True) #Passed the test
        else:
            results.append(False) #Failed the test
            results[0] = False #As soon as it fails, index 0 i.e. not prime
        witness +=1
    #print(results)
    return results


def count_lying(prime_results):
    witcheck = 0
    is_prime = prime_results[0]
    for i in prime_results[1:]:
        witcheck +=1
        if i == True and is_prime:
            liars_list[witcheck][0] +=1 #index 0 witness told the truth count
        if i== True and not is_prime:
            liars_list[witcheck][1] +=1 #index 1 witness lied count
        else:
            pass
        ################   to count a negative test as a "truth". Also remove else: poass
        #if i== False:
        #   liars_list[witcheck][0] +=1
        ################


    #print(liars_list)

def list_to_csv(counted_list):
    name ="liar_witness_"+str(2*expand-1)+".csv"
    f = open(name,"wt")
    f.write("Lies counted up to number (only odds): "+ str((expand-1)*2+1)+"\n")
    f.write("witness,truths,lies\n")
    for witty in range(1,2*expand):
        f.write(str(witty)+","+str(liars_list[witty][0])+","+str(liars_list[witty][1])+"\n")


for check in range(1,expand):
    primeness = check*2+1
    print("checking for primeness: " + str(primeness))
    primeness_results = test_number(primeness)
    count_lying(primeness_results)
list_to_csv(liars_list)
