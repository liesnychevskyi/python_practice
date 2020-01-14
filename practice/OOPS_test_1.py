import os

tomcat7_cf = '/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/tomcat_home/tomcat7/tomcat7.xml'
tomcat9_cf = '/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/tomcat_home/tomcat9/tomcat9.xml'


class Tomcat:

    def get_details_for_each_tomcat(self, server_xml):
        self.tcf = server_xml
        self.th = os.path.dirname(os.path.dirname(server_xml))
        return None

    def display_details(stas):  # stas = self
        print(f"The tomcat config file is: {stas.tcf}\nThe tomcat home is: {stas.th}")
        return None


def main():
    tomcat7 = Tomcat()  # Object of Tomcat class
    tomcat9 = Tomcat()  # Object of Tomcat class
    # ----------------------------------------------------------------------------------------------------------------||
    tomcat7.get_details_for_each_tomcat(tomcat7_cf)
    # It looks like this
    # get_details_for_each_tomcat('tomcat7', # (self)
    # "/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/tomcat_home/tomcat7/tomcat7.xml")
    # ----------------------------------------------------------------------------------------------------------------||
    tomcat9.get_details_for_each_tomcat(tomcat9_cf)
    # It looks like this
    # get_details_for_each_tomcat('tomcat9', # (self)
    # "/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/tomcat_home/tomcat9/tomcat9.xml")
    # ----------------------------------------------------------------------------------------------------------------||
    tomcat7.display_details()
    tomcat9.display_details()

    return None


if __name__ == '__main__':
    main()
