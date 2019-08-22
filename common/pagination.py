from rest_framework.pagination import PageNumberPagination

class CustomerAndSupplierPaginator(PageNumberPagination):
    def get_page_size(self,request):
        page_size = request.query_params["page_size"]
        return page_size