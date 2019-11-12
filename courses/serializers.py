from rest_framework import serializers
from .models import Course, Branch, Category, Contact

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','img_path')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ("latitude","longitude","address",)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('type','value')

class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        branches = validated_data.pop('branches')
        contacts = validated_data.pop('contacts')
        course = Course.objects.create(**validated_data)
        for branch in branches:
            Branch.objects.create(course=course, **branch)
        for contact in contacts:
            Contact.objects.create(course=course, **contact)
        return course
