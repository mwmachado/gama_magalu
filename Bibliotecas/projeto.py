#math, random
import geometria #arquivo __init__.py
geometria.outra_funcao()
print(geometria.PI)

#import pasta.arquivo
#import livro.capitulo
import geometria.areas_geometricas 

quadrado = geometria.areas_geometricas.area_quadrado(10)
print(f'a área do quadrado é {quadrado}')

triangulo = geometria.areas_geometricas.area_triangulo(2, 5)
print(f'a área do triangulo é {triangulo}')

retangulo = geometria.areas_geometricas.area_retangulo(2,5)
print(f'a área do triangulo é {retangulo}')
