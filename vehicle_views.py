import mysql.connector
from mysql import connector
import datetime

class Dbconnect:
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host = "localhost",
                user = "root",
                password = "Sana#2004",
                database = "vehicle_db"
            )
            return self.connection
        except Exception as e:
            print(e)
            return None

class VehicleServiceManager(Dbconnect):
    def post(self, **kwargs):
        try:
            self.connect = super().get_connected()

            if self.connect is None:
                return

            self.cursor = self.connect.cursor()

            query = """
            INSERT INTO vehicle_service
            (owner_name, phone, vehicle_number, vehicle_model,
             service_date, service_cost, fuel_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connect.commit()

            print("Vehicle service added successfully")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM vehicle_service"

            self.cursor.execute(query)

            records = self.cursor.fetchall()
            # for record in records:
            #     print(record)
            return records

        except Exception as e:(
            print(e))
    def get_object(self, id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connection.cursor()
            query = "select * from vehicle_service where id = %s"
            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            return record

        except Exception as e:
            return None
    def retrieve(self, id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM vehicle_service WHERE id = %s"
            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            if record is not None:
                print(record)
            else:
                print("vehicle_service not found...")

        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            record = self.get_object(id =id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder=" "
                for k in kwargs.keys():
                    placeholder += k + " = %s,"
                    placeholder = placeholder.strip(",")
                    query = f"update vehicle_service set {placeholder} where id=%s"
                    values = [v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query, values)
                    self.connection.commit()
                    print("vehicle_service details updated successfully...!!")
            else:
                print("vehicle_service details not updated successfully...!!")
        except Exception as e:
            print(e)
    def delete(self, id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()

            # Check whether member exists
            query = "SELECT * FROM vehicle_service WHERE id = %s"
            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            if record is not None:

                query = "DELETE FROM vehicle_service WHERE id = %s"

                self.cursor.execute(query, values)
                self.connect.commit()

                print("vehicle_service deleted successfully...!")

            else:
                print("vehicle_service not found...")

        except Exception as e:
            print(e)

vehicle = VehicleServiceManager()

# vehicle.post(
#     owner_name="Arun Kumar",
#     phone="9876543210",
#     vehicle_number="KL07AB1234",
#     vehicle_model="Honda City",
#     service_date="2026-10-21",
#     service_cost=3500.00,
#     fuel_type="petrol"
# )
#
# vehicle.post(
#     owner_name="Anjali Menon",
#     phone="9123456781",
#     vehicle_number="KL01CD5678",
#     vehicle_model="Hyundai Creta",
#     service_date="2026-10-15",
#     service_cost=4500.00,
#     fuel_type="diesel"
# )
#
# vehicle.post(
#     owner_name="Rahul Das",
#     phone="9012345678",
#     vehicle_number="KL05EF9012",
#     vehicle_model="Tata Nexon EV",
#     service_date="2026-10-10",
#     service_cost=2500.00,
#     fuel_type="electric"
# )
#
# vehicle.post(
#     owner_name="Meera Nair",
#     phone="9898765432",
#     vehicle_number="KL03GH3456",
#     vehicle_model="Toyota Hyryder",
#     service_date="2026-10-05",
#     service_cost=3000.00,
#     fuel_type="hybrid"
# )
print("___________get________________________")
vehicle.get()
print("----------------retrieve----------------")
vehicle.retrieve(1)
print("----------put/update---------------")
vehicle.put(1,owner_name="Sana p Anwar")
vehicle.get()
print("------------delete-------------")
vehicle.delete(6)
vehicle.get()
