#include "Wire.h"
#include "compass.h"

const int middle_ir_sensor = A0;
const int left_ir_sensor = A1;
const int right_ir_sensor = A2;
const int led = 13;

bool send_data = false;
int offset_angle = 0;
int current_angle = 0;
int middle_distance = 0;
int left_distance = 0;
int right_distance = 0;


void setup(){
    //initialize serial communications at 9600 bps
    Serial.begin(9600);
    Wire.begin();
    pinMode(led, OUTPUT);
}

void loop(){
    char receive_char = Serial.read();

    switch (receive_char){
        case '0':
            blink_led(1,100);
            Serial.println("hello arduino");
            break;
        case '1':
            Serial.println("compass_calibration_start");
            on_led();
            compass_calibration();
            off_led();
            Serial.println("compass_calibration_finsh");
            break;
        case '2':
            blink_led(3,100);
            set_compass_base_angle();
            Serial.println("setting_compass_base_angle");
            break;
        case '3':
            Serial.println("start_send_data");
            blink_led(5,50);
            delay(2);
            send_data = true;
            break;
        case '4':
            send_data = false;
            Serial.println("stop_send_data");
            blink_led(5,50);
            break;
    }

    if (send_data == true){
        fade_led();
        read_sensor();
        output_data();
    }
}

int ir_volt_to_distance(int average_count,int ir_sensor) {
    int sum = 0;
    for (int i=0; i<average_count; i++) {
        int sensor_value = analogRead(ir_sensor);  //read the sensor value
        int distance_cm = pow(3027.4/sensor_value, 1.2134); //convert readings to distance(cm)
        if (distance_cm != 0 and distance_cm < 1000)
            sum = sum + distance_cm;
    }
    sum = sum/average_count;
    if (sum > 80)
        sum = 80;
    return sum;
}

void compass_calibration(){
    compass_x_offset = 76.70;
    compass_y_offset = 191.02;
    compass_z_offset = 353.62;
    compass_x_gainError = 0.97;
    compass_y_gainError = 0.99;
    compass_z_gainError = 0.92;
    compass_init(2);
    compass_debug = 0;
    compass_offset_calibration(3);
}

void set_compass_base_angle(){
    compass_heading();
    offset_angle = bearing;
}

void read_sensor(){
    compass_heading();
    current_angle = bearing - offset_angle;
    // if (current_angle < 0)
        // current_angle += 360;
    middle_distance = ir_volt_to_distance(50,middle_ir_sensor);
    left_distance = ir_volt_to_distance(50,left_ir_sensor);
    right_distance = ir_volt_to_distance(50,right_ir_sensor);
}

void output_data(){
    Serial.print(current_angle);
    Serial.print(",");
    Serial.print(middle_distance);
    Serial.print(",");
    Serial.print(left_distance);
    Serial.print(",");
    Serial.print(right_distance);
    Serial.println();
}

void fade_led(){
    int value2 ;
    int ledpin2 = 13;                           // light connected to digital pin 11
    long time=0;
    int periode = 2000;
    int displace = 500;
    time = millis();
    value2 = 128+127*cos(2*PI/periode*(displace-time));
    analogWrite(ledpin2, value2);           // sets the value (range from 0 to 255)
}

void blink_led(int blink_times,int interval){
    for (int i=0; i < blink_times; i++){
        digitalWrite(led, HIGH);
        delay(interval);
        digitalWrite(led, LOW);
        delay(interval);
    }
}

void on_led(){
    digitalWrite(led, HIGH);
}

void off_led(){
    digitalWrite(led, LOW);
}
