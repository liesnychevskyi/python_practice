import os


def get_details_for_each_tomcat(server_xml):
    global tcf, th  # global variables
    tcf = server_xml
    th = os.path.dirname(os.path.dirname(server_xml))
    return tcf, th


def display_details():
    print(f"The tomcat config file is: {tcf}\nThe tomcat home is: {th}")
    return None


def main():
    tomcat7 = '/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/tomcat_home/tomcat7/tomcat7.xml'
    tomcat9 = '/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/tomcat_home/tomcat9/tomcat9.xml'
    tomcat7_tcf, tomcat7_th = get_details_for_each_tomcat(tomcat7)
    get_details_for_each_tomcat(tomcat9)

    display_details()
    display_details()

    return None


if __name__ == '__main__':
    main()