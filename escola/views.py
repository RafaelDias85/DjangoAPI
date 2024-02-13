from rest_framework import viewsets, generics
from escola.models import *
from escola.serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os Cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo Todas as matriculas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno (generics.ListAPIView):

    """Listando Matriculas de um  Aluno ou aluna"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculasAlunoSerializer
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados (generics.ListAPIView):
    """Listando alunos e alunas cadastrados em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaAlunosMatriculadosSerializers
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


