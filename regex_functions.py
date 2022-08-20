import re

def modify_name_to_standart(contact_list: list)-> list:
    '''modify list with right names'''

    for contact in contact_list[1:]:
        new_list = []
        for data in contact[:3]:
            #create list of name, father name, 2nd name
            a = re.split(" ", data)
            new_list.extend(a)
        new_list.append('')
        new_list = new_list[:3]
        contact[0], contact[1], contact[2] = new_list[0], new_list[1], new_list[2]
    return(contact_list)

def fill_list(list1: list, list2: list) -> list:
    #if element is empty - fill from 2nd list
    new_list = [list1[i] or list2[i] for i in range(len(list1))]
    return new_list

def delete_duplicates(contact_list: list) -> list:
    temp_list = []
    numbers = set() #position of duplicate elements
    title = contact_list.pop(0)
    for i in range(len(contact_list)):
        if i in numbers: #check if element was repeated
            continue
        temp_list.append(contact_list[i])
        # find repeated elements in 2nd cycle and update data
        for j in range(len(contact_list)):
            if temp_list[-1][0] == contact_list[j][0] and temp_list[-1][1] == contact_list[j][1]:
                temp_list[-1] = fill_list(temp_list[-1], contact_list[j])
                numbers.add(j) #set of suplicate elements
    temp_list.insert(0, title)
    return temp_list

def modify_phone_number(phone_number: str) -> str:
    '''reformate number to: +7(999)999-99-99 доб.9999;'''
    regex_phone = r"(\+7|8)+\s*\(?([\d]+)\)?[\s-]*([\d]*)-*([\d]*)-*([\d]*)"
    sub_phone = r'+7\2\3\4\5'
    phone_number = re.sub(regex_phone, sub_phone, phone_number)
    regex_add_number = r'(,\s|\sдоб.|\s\(доб.)+\s*([\d]+)\)?'
    sub_add_number = r' доб.\2'
    phone_number = re.sub(regex_add_number, sub_add_number, phone_number)
    regex_finish_format = r'(\+7)+([\d]{3})([\d]{3})([\d]{2})([\d]{2})'
    sub_finish_format = r'\1(\2)\3-\4-\5'
    phone_number = re.sub(regex_finish_format,sub_finish_format, phone_number)
    return phone_number
