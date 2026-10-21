import streamlit as st
from vehicle_views import VehicleServiceManager
vehicle = VehicleServiceManager()
tab1, tab2 = st.tabs(["ADD", "VIEW"])
with tab1:
    st.title("Add New Vehicle Service")

    owner_name = st.text_input("Enter Owner Name")
    phone = st.text_input("Enter Phone Number")
    vehicle_number = st.text_input("Enter Vehicle Number")
    vehicle_model = st.text_input("Enter Vehicle Model")
    service_date = st.date_input("Enter Service Date (yyyy/mm/dd)")
    service_cost = st.number_input("Enter Service Cost", min_value=0.0)
    fuel_type = st.selectbox(
        "Select Fuel Type",
        ["petrol", "diesel", "electric", "hybrid"]
    )

    if st.button("Add Vehicle Service"):
        vehicle.post(
            owner_name=owner_name,
            phone=phone,
            vehicle_number=vehicle_number,
            vehicle_model=vehicle_model,
            service_date=service_date,
            service_cost=service_cost,
            fuel_type=fuel_type
        )
        st.success("Vehicle Service Added Successfully")
with tab2:
    st.title("View Vehicle Service Details")

    records = vehicle.get()

    if records:
        st.table(records)
    else:
        st.warning("No Vehicle Service Records Found..!")