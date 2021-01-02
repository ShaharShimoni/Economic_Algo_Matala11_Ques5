import string
from typing import List

class department:
    students=[];
    flag=0; #Is matched
    My_name=" ";
    My_student=" ";

class student:
    department=[];
    flag=0;   #Is matched
    My_name=" ";
    My_department_Name=" ";

# These three functions exist because a class/student cannot
# #hold an object of the second class in order not to have access to the order of their lists.

def index_of_student( Dep:department,Student:string): #Position of a student on the list of the department
    count=0;
    for i in Dep.students:
        if(i==Student):
            return count;
        else:
            count=count+1;

def Name_to_dep( Dep:department,Name:string):  #Returns the class object by its name
    for i in Dep:
        if(i.My_name==Name):
            return i;

def Name_to_student( Student:student,Name:string):  #Returns the class object by its name
    for i in Student:
        if(i.My_name==Name):
            return i;

def Matchmaking(Student:List[student],Department:List[department]):
    """
    :param Student: List of students
    :param Department: List of departments
    :return: Stable match

   # fram class
    >>> Rafi = student();
    >>> Shlomo = student();
    >>> Tomer = student();

    >>> Rafi.My_name="Rafi";
    >>> Shlomo.My_name="Shlomo";
    >>> Tomer.My_name="Tomer";

    >>> Rafi.department=["Aviva","Galia","Batia"];
    >>> Shlomo.department=["Aviva","Batia","Galia"];
    >>> Tomer.department=["Batia","Galia","Aviva"];

    >>> Aviva = department();
    >>> Batia = department();
    >>> Galia = department();

    >>> Aviva.My_name = "Aviva";
    >>> Batia.My_name = "Batia";
    >>> Galia.My_name = "Galia";

    >>> Aviva.students=["Rafi","Shlomo","Tomer"];
    >>> Batia.students=["Shlomo","Rafi","Tomer"];
    >>> Galia.students=["Shlomo","Tomer","Rafi"];

    >>> Student=[Rafi,Shlomo,Tomer];
    >>> Dep=[Aviva,Batia,Galia];

    >>> Matchmaking(Student,Dep);
    Rafi with Aviva
    Shlomo with Batia
    Tomer with Galia

   # one Student replace the other one
    >>> Rafi = student();
    >>> Tomer = student();

    >>> Rafi.My_name="Rafi";
    >>> Tomer.My_name="Tomer";

    >>> Rafi.department=["Aviva","Batia"];
    >>> Tomer.department=["Aviva","Batia"];

    >>> Aviva = department();
    >>> Batia = department();

    >>> Aviva.My_name = "Aviva";
    >>> Batia.My_name = "Batia";

    >>> Aviva.students=["Rafi","Tomer"];
    >>> Batia.students=["Rafi","Tomer"];

    >>> Student = [ Tomer,Rafi];
    >>> Dep = [Aviva, Batia];

    >>> Matchmaking(Student, Dep);
    Tomer with Batia
    Rafi with Aviva

    >>> Rafi = student();
    >>> Rafi.My_name="Rafi";
    >>> Rafi.department=["Aviva"];
    >>> Aviva = department();
    >>> Aviva.My_name = "Aviva";
    >>> Aviva.students=["Rafi"];
    >>> Student = [Rafi];
    >>> Dep = [Aviva];
    >>> Matchmaking(Student, Dep);
    Rafi with Aviva

    # More Students than departments
    >>> Rafi = student();
    >>> Shlomo = student();
    >>> Tomer = student();
    >>> Rafi.My_name="Rafi";
    >>> Shlomo.My_name="Shlomo";
    >>> Tomer.My_name="Tomer";
    >>> Rafi.department=["Aviva"];
    >>> Shlomo.department=["Aviva"];
    >>> Tomer.department=["Aviva"];

    >>> Aviva = department();
    >>> Aviva.students=["Rafi","Shlomo","Tomer"];

    >>> Student=[Tomer,Rafi,Shlomo];
    >>> Dep =[Aviva];
    >>> Matchmaking(Student, Dep);
    Cant find a match
   """

    if(len(Student)!= len(Department)):
        print("Cant find a match");
        return;
    count=0;  # The amount of students being matched
    while(count != len(Student)):
        for i in Student:
            for j in i.department:
                Dep=Name_to_dep(Department,j); #Returns the department according to its name
                if(i.flag==0): # Student who isnt matched
                    if(Dep.flag==0 ): # dep doesnt match- save details
                        Dep.flag=1;
                        i.flag=1;
                        i.My_department_Name=Dep.My_name;
                        Dep.My_student=i.My_name;
                        count=count+1;
                        break;
                    else:  # dep match already - Need to check which student prefers more
                        index_s= index_of_student(Dep,Dep.My_student); #place of old student on the list
                        index_new_s= index_of_student(Dep,i.My_name); #place of new student on the list
                        if(index_new_s<index_s):  #replace student
                            Stud=Name_to_student(Student,Dep.My_student);
                            Stud.flag=0;  # last student is no longer matched
                            Dep.My_student=i.My_name; #new student name
                            i.flag=1;
                            i.My_department_Name=Dep.My_name;
                            break;

    for i in Student:
        print(i.My_name+" with "+i.My_department_Name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
