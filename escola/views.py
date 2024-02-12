from rest_framework import viewsets, generics
from escola.models import *
from .serializer import *


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os Cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo Todas as matriculas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno (generics.ListAPIView):
    """Listando Matriculas de um  Aluno ou aluna"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset