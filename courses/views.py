from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .serializers import CourseSerializer
from .models import Course

class CourseListView(ListCreateAPIView):
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SingleCourseView(RetrieveDestroyAPIView):
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer




#   def get(self, request, *args, **kwargs):
#       return self.list(request, *args, **kwargs)
#
#   def perform_create(self, serializer):
#       category = get_object_or_404(Category, id=self.request.data.get('category_id'))
#       return serializer.save(author=author)
#   def post(self, request, *args, **kwargs):
#       return self.create(request, *args, **kwargs)