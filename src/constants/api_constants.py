#keep all the urls

class APIConstants:

    def base_url(self):
        return "https://restful-booker.herokuapp.com"


    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"


 # UPDATE/ DELETE/ PUT/PATCH/DELETE

    def url_patch_put_delete(self, booking_id ):
        return "https://restful-booker.herokuapp.com/booking" + str(booking_id)
