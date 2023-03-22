class Usuario:
    """
   Clase que representa un usuario de la aplicacion
   """

    def __init__(self, usr_name, pwd, cod=None):
        """
       Funcion Constructora de la clase usuario
       :param cod: int
       :param usr_name:
       :param pwd:
       """
        self.__cod = cod
        self.__usr_name = usr_name
        self.__pwd = pwd

    # Getters
    def get_cod(self):
        """
       Funcion que devuelve el codigo del usuario
       :return: int
       """
        return self.__cod

    def get_usr_name(self):
        """

       :return:
       """
        return self.__usr_name

    def get_pwd(self):
        """

       :return:
       """
        return self.__pwd

    # Setters
    def set_usr_name(self, usr_name):
        """

       :param usr_name:
       :return:
       """
        self.__usr_name = usr_name


    def set_pwd(self, pwd):
        """

        :param pwd:
        :return:
        """
        self.__pwd = pwd


    def __repr__(self):
        return f"Username:\t {self.__usr_name} \nPassword:\t {self.__pwd}"
