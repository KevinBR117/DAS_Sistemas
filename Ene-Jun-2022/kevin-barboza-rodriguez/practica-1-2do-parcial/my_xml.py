import xml.etree.ElementTree as ET
import copy

tree = ET.parse('./Ene-Jun-2022/kevin-barboza-rodriguez/practica-1-2do-parcial/sample.xml')
root = tree.getroot()
tree2 = copy.deepcopy(tree)
root2 = tree2.getroot()

if __name__ == "__main__":
    #print(root.tag)
    #lista de personas con id par
    print("-----------personas con id par ----------- \n")
    i = 0
    for person in root:
        if ((int(root[i][0].text) % 2) == 0):
            print("---person data------")
            print("id: ",(root[i][0].text))
            print("first name: ", root[i][1].text)
            print("last name: ", root[i][2].text)
            print("company: ", root[i][3].text)
            print("email: ", root[i][4].text)
            print("ip address: ", root[i][5].text)
            print("phone number: ", root[i][6].text)
            print("")
        i += 1

    #lista de personas con correo de dominio .edu o .gov
    print("-----------personas con correo de dominio .edu o .gov ----------- \n")
    i = 0
    for person in root:
        dominio = root[i][4].text[len(root[i][4].text)-3:len(root[i][4].text)]
        if (dominio == 'edu' or dominio == 'gov'):
            print("---person data------")
            print("id: ",(root[i][0].text))
            print("first name: ", root[i][1].text)
            print("last name: ", root[i][2].text)
            print("company: ", root[i][3].text)
            print("email: ", root[i][4].text)
            print("ip address: ", root[i][5].text)
            print("phone number: ", root[i][6].text)
            print("")
        i += 1
    
    #lista de personas con compañia entre 4 y 6 caracteres
    print("-----------personas con con compañia entre 4 y 6 caracteres ----------- \n")
    i=0
    for person in root:
        company = root[i][3].text
        if ( len(company) >= 4 and len(company) <= 6):
            print("---person data------")
            print("id: ",(root[i][0].text))
            print("first name: ", root[i][1].text)
            print("last name: ", root[i][2].text)
            print("company: ", root[i][3].text)
            print("email: ", root[i][4].text)
            print("ip address: ", root[i][5].text)
            print("phone number: ", root[i][6].text)
            print("")
        i += 1

    
    i=0
    for person in root2:    
        root2[i][5].text = "127.0.0.1"
        root2[i][5].set('updated', 'yes')    
        i += 1
    tree2.write('./Ene-Jun-2022/kevin-barboza-rodriguez/practica-1-2do-parcial/sample1.xml')