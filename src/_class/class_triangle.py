class Triangle:
    def __init__(self, side_a: int, side_b: int, side_c: int) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _check_values(self) -> str | None:
        """Checa se os valores são inteiros e positivos"""
        side_list = [self.side_a, self.side_b, self.side_c]
        for side in side_list:
            if not isinstance(side, int):
                return "Os números devem ser inteiro."
            if side <= 0:
                return "Os números devem ser positivos."
        return None

    def _triangle_validation(self) -> bool:
        """Checa se os valores são validos para um triângulo"""
        if not self.side_a + self.side_b > self.side_c:
            return False
        if not self.side_a + self.side_c > self.side_b:
            return False
        if not self.side_b + self.side_c > self.side_a:
            return False
        return True

    def _triangle_is_valid(self) -> str | None:
        """Checagem completa"""
        if self._check_values() is not None:
            return self._check_values()
        if not self._triangle_validation():
            return "Os valores não formam um triângulo."
        return None

    def triangle_type(self) -> str:
        """Retorna o tipo do triângulo, caso os valores sejam validos"""
        if self._triangle_is_valid() is not None:
            return self._triangle_is_valid()
        if self.side_a == self.side_b and self.side_b == self.side_c:
            return "Equilátero"
        elif self.side_a == self.side_b or self.side_a == self.side_c or self.side_b == self.side_c:
            return "Isósceles"
        else:
            return "Escaleno"