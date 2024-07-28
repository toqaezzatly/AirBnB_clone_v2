#/usr/bin/python3
"""state file"""
class State(BaseModel, Base):

    if models.storage_t != 'db':
        @property
        def cities(self):
            from models import storage
            from models.city import City
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
