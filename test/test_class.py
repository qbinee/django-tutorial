class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')

    def test_three(self):
        self.value = 1
        assert self.value == 1

