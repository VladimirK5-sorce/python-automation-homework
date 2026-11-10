class StringUtils:
    """
    Класс с полезными утилитами для обработки строк
    """

    def capitalize(self, string: str) -> str:
        """
        Принимает на вход строку, возвращает её же, 
        но с заглавной первой буквой.
        Пример: "skypro" -> "Skypro"
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Принимает на вход строку, удаляет пробелы в начале 
        и возвращает измененную строку.
        Пример: "   skypro" -> "skypro"
        """
        return string.lstrip()

    def to_list(self, string: str, delimeter=",") -> list[str]:
        """
        Принимает на вход строку с разделителями, 
        возвращает список строк.
        Пример: "a,b,c,d" -> ["a", "b", "c", "d"]
        """
        if self.is_empty(string):
            return []
        return string.split(delimeter)

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает True, если строка содержит искомый символ, 
        и False — если не содержит.
        Пример: "SkyPro", "P" -> True
        """
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки.
        Пример: "SkyPro", "Pro" -> "Sky"
        """
        if self.contains(string, symbol):
            return string.replace(symbol, "")
        return string

    def is_empty(self, string: str) -> bool:
        """
        Возвращает True, если строка пустая или состоит 
        только из пробелов, иначе — False.
        Пример: "" -> True, " " -> True, "abc" -> False
        """
        if string is None:
            return True
        return string.strip() == ""
