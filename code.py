#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
expander_1 = Triport(Ports.PORT1)
controller_1 = Controller(PRIMARY)
# vex-vision-config:begin
vision_5 = Vision(Ports.PORT5, 50)
# vex-vision-config:end
distance_6 = Distance(Ports.PORT6)
bumper_a = Bumper(brain.three_wire_port.a)
limit_switch_h = Limit(brain.three_wire_port.h)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
limit_switch_g = Limit(brain.three_wire_port.g)
inertial_4 = Inertial(Ports.PORT4)
rotation_7 = Rotation(Ports.PORT7, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration
#robot movement calculation
def _send_robot_commands ( self ):
v_1, v_r = self._uni_to_diff( v, omega )
self.robot.set_wheel_drive_rates( v_1, v_r )

def _uni_to_diff( self, v, omega ):
    #v is the translational velocity in m/s, omega is the angular velocity in rad/s
R = self.robot_wheel_radius
L = self.robot_wheel_base_length

v_1 = ( (2.0 * v) - (omega*L) ) / (2.0 * R)
v_r = ( (2.0 * v) + (omega*L) ) / (2.0 * R)
return v_1, v_r
    #response for bumper_a: move backwards and turn
def autonomous():
    pass
    remote_control_code_enabled = False
    if condition: bumper_a.pressing()
        pass 
        motor_2.spin(FORWARD,-90,DEGREES)
        motor_3.spin(FORWARD,90,DEGREES)
        pass
        motor_2.spin(FORWARD,90,DEGREES)
        motor_3.spin(FORWARD,90,DEGREES)

