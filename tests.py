#inserir 3 valores para somente assim conhecer de fato os erros na estrutura de dados, um no meio 1 no início e 1 no fim
#se tiver RAISE tem de testar caminho de erro

#Decantalarathunay

#
class Other:
    def calc(self):
        return x + 1


class Target:
    def __init__(self, outra:Other):
        self.other = outra 
    

    def eval(self, x):
        return x + self.other.calc(x)
    

class Test_Target(unittest.TestCase):
    @patch('tests.')
    def setUp(self, other):
        self.target = Target(other)
    
    def test_eval(self):
        self.other.calc.return_value = 1
        self.assertEqual(3, self.target.eval(2))
    