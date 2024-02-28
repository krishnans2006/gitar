#include <Stepper.h>

// Parameters
const int rotationDegrees = 72;

#define STEPS 200
Stepper stepper(STEPS, 4, 5, 6, 7);

const int numSteps = (rotationDegrees * STEPS)/ 360;

void setup() {
  Serial.begin(9600);
  // setSpeed(60) apparently sets the speed of the motor to 30 RPMs
  stepper.setSpeed(30);
}

void loop() {
  Serial.println("Forward");
  stepper.step(numSteps);
  delay(500);
  Serial.println("Backward");
  stepper.step(-numSteps);
  delay(5000);
}
