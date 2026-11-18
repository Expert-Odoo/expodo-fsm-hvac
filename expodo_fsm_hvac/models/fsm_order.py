from odoo import models, fields


class FsmOrder(models.Model):
    _inherit = "expodo.fsm.order"

    # Equipment serviced
    equipment_kind = fields.Selection(
        [
            ("split", "Split system"),
            ("multi_split", "Multi-split"),
            ("ducted", "Ducted / central"),
            ("vrf", "VRF / VRV"),
            ("rooftop", "Rooftop unit"),
            ("heat_pump", "Heat pump"),
            ("chiller", "Chiller"),
            ("air_handler", "Air handling unit"),
            ("cold_room", "Cold room / refrigeration"),
            ("other", "Other"),
        ],
        string="Equipment Type",
    )
    equipment_brand = fields.Char(string="Brand")
    equipment_model = fields.Char(string="Model Reference")
    serial_number = fields.Char(string="Serial Number", index=True)
    unit_location = fields.Char(
        string="Unit Location", help="Where the unit is installed (roof, plant room, floor...)"
    )
    install_date = fields.Date(string="Install Date")
    last_service_date = fields.Date(string="Last Service Date")

    # Refrigerant / F-Gas tracking
    refrigerant_type = fields.Selection(
        [
            ("r32", "R32"),
            ("r410a", "R410A"),
            ("r407c", "R407C"),
            ("r134a", "R134a"),
            ("r290", "R290 (propane)"),
            ("r744", "R744 (CO2)"),
            ("r717", "R717 (ammonia)"),
            ("r1234ze", "R1234ze"),
            ("other", "Other"),
        ],
        string="Refrigerant",
    )
    refrigerant_charge_kg = fields.Float(
        string="Charge (kg)", help="Total refrigerant charge of the system, in kilograms"
    )
    refrigerant_added_kg = fields.Float(
        string="Added (kg)", help="Refrigerant added during this job"
    )
    refrigerant_recovered_kg = fields.Float(
        string="Recovered (kg)", help="Refrigerant recovered during this job"
    )
    leak_test_done = fields.Boolean(string="Leak Test Passed")
