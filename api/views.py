from rest_framework import viewsets, status
from .models import Subscriber, Service, Subscription, Bill
from .serializers import SubscriberSerializer, ServiceSerializer, SubscriptionSerializer, BillSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    @action(detail=True, methods=['post'], url_path='block_subscriber')
    def block_subscriber(self, request, pk=None):
        if not request.user.is_staff:
            return Response({'status': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)

        subscriber = self.get_object()
        subscriber.is_active = False
        subscriber.save()
        return Response({'status': 'subscriber blocked'})

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

@api_view(['GET'])
def unpaid_bills(request):
    if request.user.is_staff:
        unpaid_bills = Bill.objects.filter(is_paid=False)
        serializer = BillSerializer(unpaid_bills, many=True)
        return Response(serializer.data)
    else:
        return Response(status=403)

