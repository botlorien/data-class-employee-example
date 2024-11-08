from typing import NamedTuple, List

Funcionario = NamedTuple(
    'Funcionario',
    nome=str,
    cargo=str,
    salario=float,
    data_admissao=str,
    beneficios=float
    )

def validar_funcionarios(func):
    def wrapper(funcionarios,*args,**kwargs):
        if not funcionarios or not isinstance(funcionarios,list):
            raise ValueError(f'Invalid value for funcionarios: {funcionarios}. Expected a List[Funcionarios]')
        for funcionario in funcionarios:
            match funcionario:
                case Funcionario(_):...
                case _: raise TypeError(f'Invalid type for funcionario:{type(funcionario)}. Expected type {Funcionario}')
        return func(funcionarios,*args, **kwargs)
    return wrapper

@validar_funcionarios
def calcular_media_salarial(funcionarios:List[Funcionario]):
    salarios = [funcionario.salario for funcionario in funcionarios]
    return sum(salarios)/len(salarios)

@validar_funcionarios
def filtrar_por_cargo(funcionarios:List[Funcionario],cargo:str):
    return [funcionario for funcionario in funcionarios if funcionario.cargo == cargo]

@validar_funcionarios
def calcular_total_beneficios(funcionarios:List[Funcionario]):
    return sum(funcionario.beneficios for funcionario in funcionarios)

if __name__=='__main__':
    # Lista de funcionários para teste
    funcionarios = [
        Funcionario(nome="Alice", cargo="Desenvolvedor", salario=5000, data_admissao="2021-06-10", beneficios=800),
        Funcionario(nome="Bob", cargo="Analista", salario=4500, data_admissao="2020-03-15", beneficios=600),
        Funcionario(nome="Carlos", cargo="Gerente", salario=7000, data_admissao="2019-07-20", beneficios=1000),
        Funcionario(nome="Diana", cargo="Desenvolvedor", salario=5200, data_admissao="2022-01-05", beneficios=800),
        Funcionario(nome="Eva", cargo="Designer", salario=4000, data_admissao="2021-11-25", beneficios=500)
    ]
    
    # Cálculo e exibição da média salarial
    media_salarial = calcular_media_salarial(funcionarios)
    print(f"Média Salarial: R${media_salarial:.2f}")
    
    # Exibindo o total de benefícios
    total_beneficios = calcular_total_beneficios(funcionarios)
    print(f"Total de Benefícios: R${total_beneficios:.2f}")
    
    # Filtrando e exibindo funcionários com cargo "Desenvolvedor"
    desenvolvedores = filtrar_por_cargo(funcionarios, "Desenvolvedor")
    print("Desenvolvedores:")
    for desenvolvedor in desenvolvedores:
        print(desenvolvedor)
    