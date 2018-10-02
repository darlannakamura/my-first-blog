from rest_framework import serializers

from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #author = serializers.ReadOnlyField(source='author.user')
        fields = ('pk', 'title', 'slug', 'image', 'text',
         'created_date', 'published_date',)