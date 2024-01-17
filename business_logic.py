
class BusinessLogic:
    @staticmethod
    def get_source_id():
        return "pilot04"

    @staticmethod
    def get_downloads(client_id, destination_id):
        if destination_id != "befit_1":
            return []
        else:
            return []
