import xml.etree.ElementTree as ET
def funcion():
    #CREAMOS EL ARCHIVO XML Y ROOT
    p = ET.Element('students')

    #CREAMOS LOS CHILDS CON SUS SUBCHILDS Y ATRIBUTOS

    c = ET.SubElement(p, 'student')     #CHILD
    c.set('class', 'DAM1')              #ATRIBUTO
    n = ET.SubElement(c, 'name')        #SUBCHILD
    n.text = "Marta"     
    s = ET.SubElement(c, 'surname')
    s.text ="Fernandez"
    e = ET.SubElement(c, 'email')
    e.text = "martafernandez@gmail.com"
    d = ET.SubElement(c, 'dni')
    d.text = "3728939X"


    c = ET.SubElement(p, 'student')
    c.set('class', 'DAM2')  
    n = ET.SubElement(c, 'name')
    n.text = "Lucio"
    s = ET.SubElement(c, 'surname')
    s.text ="Perez"
    e = ET.SubElement(c, 'email')
    e.text = "lucioperez@gmail.com"
    d = ET.SubElement(c, 'dni')
    d.text = "73474923Y"

    c = ET.SubElement(p, 'student')
    c.set('class', 'DAW1')  
    n = ET.SubElement(c, 'name')
    n.text = "Carla"
    s = ET.SubElement(c, 'surname')
    s.text ="Lopez"
    e = ET.SubElement(c, 'email')
    e.text = "carlalopez@gmail.com"
    d = ET.SubElement(c, 'dni')
    d.text = "47272290S"

    c = ET.SubElement(p, 'student')
    c.set('class', 'DAw2')  
    n = ET.SubElement(c, 'name')
    n.text = "Manuel"
    s = ET.SubElement(c, 'surname')
    s.text ="Herrero"
    e = ET.SubElement(c, 'email')
    e.text = "manuelherrero@gmail.com"
    d = ET.SubElement(c, 'dni')
    d.text = "824948J"

    c = ET.SubElement(p, 'student')
    c.set('class', 'DAM1')  
    n = ET.SubElement(c, 'name')
    n.text = "Arturo"
    s = ET.SubElement(c, 'surname')
    s.text ="Rodrigez"
    e = ET.SubElement(c, 'email')
    e.text = "arturorodrigez@gmail.com"
    d = ET.SubElement(c, 'dni')
    d.text = "2749247K"


    tree = ET.ElementTree(p)
    tree.write("actividad12_A.xml")
    ET.indent(p)
    ET.dump(p)




funcion()