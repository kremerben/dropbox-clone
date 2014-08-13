from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication, Authentication, SessionAuthentication
from tastypie.authorization import Authorization
from tastypie.cache import SimpleCache
# from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.fields import ToManyField, ToOneField
from tastypie.resources import ModelResource
from tastypie.validation import Validation
from dropbox.api.authorization import UserObjectsOnlyAuthorization
from dropbox.models import Media



class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = "user"
        excludes = ['password', 'is_superuser']
        allowed_methods = ['get', 'post', 'put']  # Limit the possible REST actions
        # authorization = Authorization()
        # validation = Validation()
        # authentication = SessionAuthentication()
        # authorization = UserObjectsOnlyAuthorization()

        ordering = ['first_name']         # FIELDS ALLOWED ORDERING Default the order of the objects returned in this list
        # filtering = {
        #     'first_name': ALL_WITH_RELATIONS,
        #     'last_name': ALL_WITH_RELATIONS,
        #     'email': ALL_WITH_RELATIONS,
        #     'username': ALL_WITH_RELATIONS,
        # }


class MediaResource(ModelResource):
    owner = ToOneField(UserResource, 'owner', full=False)

    class Meta:
        # cache = SimpleCache(timeout=60)
        queryset = Media.objects.all()
        resource_name = "media"
        allowed_methods = ['get', 'post', 'put', 'delete']  # Limit the possible REST actions
        always_return_data = True          # Whether data should be returned when a POST is made
        limit = 10                         # Number of objects per call in the list for pagination
        # validation = Validation()
        # authentication = SessionAuthentication()
        # authorization = UserObjectsOnlyAuthorization()

        filtering = {
            'owner': ['exact'],
            'description': ['contains', 'icontains'],
            'created': ['gt','lt','gte','lte' ]
        }

