# Self Driving Car
### What is the idea?
We wanted to make a self-driving delivery car. Our car would take food or other objects and make its way around the room while carrying the item and avoiding obstacles. 
### What does it do?
We modified an Elegoo smart car equipped with an Arduino to function as our car. We used ultrasonic sensors to check for obstacles directly in front of it, such as feet or walls. When it detected a wall or foot, it looked around for a different path to take. Similarly, we implemented Google's Teachable AI by training a model to recognise a stop sign. When the model detected the stop sign and the confidence was high enough, our car would stop. We trained our model by using various photos of our makeshift stop sign and using a second class, "rando" which consisted of things that were not the stop sign but things that the smart car may encounter.
### How it works
All code was done in Visual Studio in Python. After you turn the car on, you must connect to the car via wifi and upload your code. The car uses its camera to detect and upload photos, which are then compared to the AI model. The output is seen when it tells us whether its detecting, "rando" or "stop"
### Other features
We 3D printed a box to go on top of our car to serve as the "delivery basket"
### Systems used
- Visual Studio
- Keras
- TensorFlow
- PySerial
- Python 3
- Elegoo Smart Car


