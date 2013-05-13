

class ProjectDescription(object):
    '''---------------------------------'''
    '''         Modify here           '''
    '''---------------------------------'''
    iCSE_PROJECT_NAME = u'Project name'
    iCSE_YEAR = u'2013'
    iCSE_AUTHOR_NAME = u'Chuck Norris'
    '''--------------------------------'''

    iCSE_FILE_NAME = ''
    iCSE_SKRYPTDOC_NAME = ''
    iCSE_SKRYPT_DOCUMENTATION_NAME = ''

    def __init__(self):
        no_space_project_name = ''.join(self.iCSE_PROJECT_NAME.split())

        self.iCSE_FILE_NAME = '_'.join(self.iCSE_PROJECT_NAME.lower().split())       
        self.iCSE_SKRYPTDOC_NAME = no_space_project_name
        self.iCSE_SKRYPT_DOCUMENTATION_NAME = no_space_project_name + "-Skrypt"


class SphinxConf(object):

    def __init__(self, project_description):
        self.in_file = None
        self.out_file = None
        self.is_no_error = True
        self.content = []
        self.__open_files()

    def __open_files(self):
        try:
             self.in_file = open(u'conf_template.py', "r")        
             self.out_file = open(u'./source/conf.py', "w")       

             self.content = self.in_file.readlines()
        except IOError as e:
            print "Error: file does not exist !!!"

    def __close_files(self):
        self.in_file.close()
        self.out_file.close()

    def __set_names(self):
        self.content = map(lambda x: x.replace("iCSE_PROJECT_NAME", project_description.iCSE_PROJECT_NAME),  self.content) 
        self.content = map(lambda x: x.replace("iCSE_YEAR", project_description.iCSE_YEAR),  self.content) 
        self.content = map(lambda x: x.replace("iCSE_AUTHOR_NAME", project_description.iCSE_AUTHOR_NAME),  self.content)
        self.content = map(lambda x: x.replace("iCSE_SKRYPTDOC_NAME", project_description.iCSE_SKRYPTDOC_NAME),  self.content) 
        self.content = map(lambda x: x.replace("iCSE_FILE_NAME", project_description.iCSE_FILE_NAME),  self.content) 
        self.content = map(lambda x: x.replace("iCSE_SKRYPT_DOCUMENTATION_NAME", project_description.iCSE_SKRYPT_DOCUMENTATION_NAME),  self.content)  

        self.out_file.write("")
        self.out_file.write("".join(self.content))

    def run(self):
        self.__set_names()
        self.__close_files()


if __name__ == "__main__":
    project_description = ProjectDescription()
    sphinx_conf = SphinxConf(project_description)
    sphinx_conf.run()



