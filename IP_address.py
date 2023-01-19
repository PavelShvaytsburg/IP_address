import sys

class Error(Exception):
    pass

class NumberTooLarge(Error):
    pass

class Address:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask
        self.test()

    def test(self):
        try:
            for n, k in zip(self.ip.split("."), self.mask.split(".")):
                if int(n) > 255 or int(k) > 255:
                    raise NumberTooLarge
                else:
                    continue
        except ValueError:
            sys.exit("Адресс не должен включать в себя буквы")
        except NumberTooLarge:
            sys.exit("Число в адрессе не может превышать 255")
        

    def network(self):
        binary_network_id = ""
        network_id = ""
        binaric = self.binary()
        for id, mask in zip(binaric[0].split('.'), binaric[1].split('.')):
            for n,k in zip(id, mask):
                if int(n) == 1 and int(k) == 1:
                    binary_network_id+="1"
                else:
                    binary_network_id+="0"
            binary_network_id+="."
        
        for i in binary_network_id.split(".")[:len(binary_network_id)-1]:
            amount = 0
            for j in range(0,len(i)):
                amount = amount + int(i[j])*(2**(len(i)-j-1))
            network_id+=str(amount) + "."

        return network_id, binary_network_id

    def binary(self):
        result_id = ""
        result_mask = ""
        list_id = list(map(int, self.ip.split(".")))
        list_mask = list(map(int, self.mask.split(".")))
        
        for i in range(len(list_id)):
            string = ""
            count = 0
            if list_id[i] > 0:
                while list_id[i] > 0:
                    string = str(list_id[i]%2) +string
                    list_id[i] = list_id[i] //2
                    count +=1
                if count < 8:
                    result_id+=string+(8-count)*"0"+"."
                else:
                    result_id+=string+"."
            else:
                result_id+=string+(8-count)*"0"+"."

        for i in range(len(list_mask)):
            string = ""
            count = 0
            if list_mask[i] > 0:
                while list_mask[i] > 0:
                    string = str(list_mask[i]%2) +string
                    list_mask[i] = list_mask[i] //2
                    count +=1
                if count < 8:
                    result_mask+=string+(8-count)*"0"+"."
                else:
                    result_mask+=string+"."
            else:
                result_mask+=string+(8-count)*"0"+"."
        return result_id[0:len(result_id)-1], result_mask[0:len(result_mask)-1]
    
    def get_binary(self):
        binaric = self.binary()
        return f"IP-адресс: {binaric[0]}\nМаска: {binaric[1]}"

    def get_network(self):
        networks = self.network()
        return f"Адресс сети: {networks[0]}\nАдресс сети в двичном виде: {networks[1]}"

    def get_all(self):
        networks = self.network()
        return f"IP-адресс: {self.ip}\nМаска: {self.mask}\nАдресс сети: {networks[0]}"

    def get_all_binary(self):
        networks = self.network()
        binaric = self.binary()
        return f"IP-адресс: {binaric[0]}\nМаска: {binaric[1]}\nАдресс сети: {networks[1]}"
            

my_address = Address("213.180.193.3", "255.255.255.0")
print(my_address.get_all())
print("\n")
print(my_address.get_all_binary())
print("\n")
wrong_adress_number = Address("q13.180.193.3", "355.255.255.0")


