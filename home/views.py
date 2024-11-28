from datetime import timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Availability
from .serializers import AvailabilitySerializer


class Register(APIView):
    # def get(self, request):
    #     availability = Availability.objects.all()
    #     serializer = AvailabilitySerializer(availability, many=True)
    #     return Response(serializer.data)

    """
    This view provides a way to create new records for users 
    (candidates or interviewers) using a POST request.

    """
    
    def post(self, request):
        """
        Accepts a JSON payload containing user details
        {
            "email": "example@example.com",
            "phone_number": 9876543210,
            "role": "Interviewer", / "Candidate"
            "start_time": "00:00:00",
            "end_time": "23:00:00"
        }    
        and validates the data using the AvailabilitySerializer. 
        If the data is valid, it saves the record to the database and returns the serialized 
        data..

        Args:
            request (Request): The HTTP request object containing the availability data 
            in the request body.

        Returns:
            Response: A JSON response containing the serialized data of the newly created 
            availability record with a status of 201, or validation errors with a status of 400.
        """
        serializer = AvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetSlots(APIView):
    def get(self, request, candidate_id, interviewer_id):

        """
        Get the available time slots for an interview between a candidate and an interviewer based on their provided IDs.
        It calculates the overlapping time range between their available times and returns a list of possible 1-hour time slots. 
        If no overlap is found, it returns a message indicating that no available slots are present.

        Args:
            request (Request): The HTTP request object.
            candidate_id (int): The ID of the candidate.
            interviewer_id (int): The ID of the interviewer.

        Returns:
            Response: A JSON response containing the available time slots or an error message.
                - If the candidate or interviewer is not found, it returns a 404 status with an error message.
                - If no overlapping time slots are found, it returns a message indicating that no slots are available.
                - Otherwise, it returns a list of available time slots with a 200 status.
        """

        candidate = Availability.objects.filter(user_id=candidate_id, role='Candidate').first()
        interviewer = Availability.objects.filter(user_id=interviewer_id, role='Interviewer').first()

        if not candidate or not interviewer:
            return Response({"error": "Candidate or Interviewer not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            candidate_start = candidate.start_time
            candidate_end = candidate.end_time
            interviewer_start = interviewer.start_time
            interviewer_end = interviewer.end_time

            possible_start_time = max(candidate_start, interviewer_start)
            possible_end_time = min(candidate_end, interviewer_end)

            print(possible_start_time, possible_end_time)

            if possible_start_time >= possible_end_time:
                return Response("No possible time slots available.", status=status.HTTP_200_OK)
            else:
                start_hour = possible_start_time.hour
                end_hour = possible_end_time.hour
                slots = [(start_hour, start_hour + 1), (end_hour - 1, end_hour)]
                print(slots)
                response_data = {
                    "Available time slots": slots
                }
                return Response(response_data, status=status.HTTP_200_OK)
