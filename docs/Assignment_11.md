### Problem Statement: Smart Home Automation System

#### Objective:
Design and implement a **Smart Home Automation System** using Object-Oriented Programming (OOP) principles. The system will allow users to control various smart devices (such as lights, thermostats, security cameras, and smart locks) in their home. The system should enable users to manage device states (on/off), adjust settings, and monitor the status of devices through a unified platform. The system should also support scheduling tasks, enabling automated actions based on specific conditions (e.g., turn off lights at a certain time or adjust the thermostat based on the time of day).

#### Requirements:

### 1. **Class Definitions**

#### 1.1 **SmartDevice Class**
- **Attributes:**
    - `device_id` (string): A unique identifier for each device (e.g., "LIGHT001").
    - `device_name` (string): The name of the device (e.g., "Living Room Light", "Thermostat").
    - `device_type` (string): The type of device (e.g., "Light", "Thermostat", "Security Camera", "Smart Lock").
    - `status` (bool): The current status of the device (True = On, False = Off).
    
- **Methods:**
    - **Constructor (`__init__`)**: Initializes the smart device with `device_id`, `device_name`, `device_type`, and initial `status`.
    - **`turn_on()`**: Turns the device on (sets status to True).
    - **`turn_off()`**: Turns the device off (sets status to False).
    - **`toggle()`**: Toggles the device between on and off states.
    - **`get_status()`**: Returns the current status of the device (on/off).
    - **`__str__()`**: Returns a string representation of the device, including its name, type, and current status.

#### 1.2 **Light Class (Inherits from SmartDevice)**
- **Attributes:**
    - `brightness` (int): The brightness level of the light (0 to 100).
    
- **Methods:**
    - **Constructor (`__init__`)**: Initializes the light with `device_id`, `device_name`, `status`, and `brightness`.
    - **`set_brightness(level)`**: Adjusts the brightness of the light.
    - **`increase_brightness()`**: Increases the brightness by 10%.
    - **`decrease_brightness()`**: Decreases the brightness by 10%.
    - **`__str__()`**: Returns a string representation of the light, including its name, type, status, and brightness.

#### 1.3 **Thermostat Class (Inherits from SmartDevice)**
- **Attributes:**
    - `temperature` (float): The current temperature set on the thermostat.
    - `mode` (string): The operating mode of the thermostat (e.g., "Cooling", "Heating", "Off").
    
- **Methods:**
    - **Constructor (`__init__`)**: Initializes the thermostat with `device_id`, `device_name`, `status`, `temperature`, and `mode`.
    - **`set_temperature(temp)`**: Sets the temperature of the thermostat.
    - **`set_mode(mode)`**: Changes the mode of the thermostat.
    - **`increase_temperature()`**: Increases the temperature by 1 degree.
    - **`decrease_temperature()`**: Decreases the temperature by 1 degree.
    - **`__str__()`**: Returns a string representation of the thermostat, including its name, type, status, temperature, and mode.

#### 1.4 **SecurityCamera Class (Inherits from SmartDevice)**
- **Attributes:**
    - `camera_quality` (string): The quality of the camera (e.g., "1080p", "4K").
    - `is_recording` (bool): Whether the camera is currently recording.
    
- **Methods:**
    - **Constructor (`__init__`)**: Initializes the camera with `device_id`, `device_name`, `status`, `camera_quality`, and `is_recording`.
    - **`start_recording()`**: Starts the camera recording.
    - **`stop_recording()`**: Stops the camera recording.
    - **`__str__()`**: Returns a string representation of the camera, including its name, type, status, and camera quality.

#### 1.5 **SmartLock Class (Inherits from SmartDevice)**
- **Attributes:**
    - `lock_status` (bool): The status of the lock (True = Locked, False = Unlocked).
    
- **Methods:**
    - **Constructor (`__init__`)**: Initializes the lock with `device_id`, `device_name`, `status`, and `lock_status`.
    - **`lock()`**: Locks the smart lock (sets status to True).
    - **`unlock()`**: Unlocks the smart lock (sets status to False).
    - **`toggle_lock()`**: Toggles the lock status between locked and unlocked.
    - **`__str__()`**: Returns a string representation of the smart lock, including its name, type, status, and lock status.

#### 1.6 **HomeAutomationSystem Class**
- **Attributes:**
    - `devices` (list): A list of all smart devices in the home.
    - `scheduled_tasks` (list): A list of tasks scheduled to execute at specific times (e.g., turn on lights at a certain time, adjust thermostat settings).
    
- **Methods:**
    - **Constructor (`__init__`)**: Initializes the system with an empty list of devices and scheduled tasks.
    - **`add_device(device)`**: Adds a new device to the system.
    - **`remove_device(device_id)`**: Removes a device from the system based on its `device_id`.
    - **`get_device_status(device_id)`**: Returns the status of a device based on its `device_id`.
    - **`schedule_task(task, time)`**: Schedules a task to occur at a specific time (e.g., "turn on the living room light at 7:00 PM").
    - **`view_all_devices()`**: Displays a list of all devices in the home, including their current status.
    - **`__str__()`**: Returns a string representation of the system, including a summary of devices and scheduled tasks.

### 2. **Features**

#### 2.1 **Device Control**
- The system should allow users to turn devices on and off, adjust settings (e.g., brightness for lights, temperature for thermostats), and monitor the status of each device.
    
#### 2.2 **Device Types**
- The system supports various types of devices:
    - **Lights**: Control on/off status and adjust brightness.
    - **Thermostats**: Adjust temperature and mode (cooling, heating).
    - **Security Cameras**: Start/stop recording, view camera status.
    - **Smart Locks**: Lock and unlock doors, or toggle lock status.

#### 2.3 **Task Scheduling**
- Users should be able to schedule tasks to occur at specific times. For example:
    - Turn on the lights at a certain time.
    - Set the thermostat to a specific temperature at night.

#### 2.4 **Monitoring**
- The system should allow users to monitor the status of all devices in real-time, view device settings, and receive updates about scheduled tasks.

### 3. **Sample Usage**

```python
# Create a smart home system
home_system = HomeAutomationSystem()

# Add some devices to the system
light1 = Light("LIGHT001", "Living Room Light", "Light", False, 50)
thermostat = Thermostat("THERMO001", "Main Thermostat", "Thermostat", False, 22.5, "Cooling")
camera = SecurityCamera("CAM001", "Front Door Camera", "Security Camera", False, "1080p", False)
lock = SmartLock("LOCK001", "Front Door Lock", "Smart Lock", False, False)

home_system.add_device(light1)
home_system.add_device(thermostat)
home_system.add_device(camera)
home_system.add_device(lock)

# Control devices
light1.turn_on()
thermostat.set_temperature(25)
camera.start_recording()
lock.lock()

# View the status of all devices
home_system.view_all_devices()

# Schedule tasks
home_system.schedule_task(lambda: light1.turn_on(), "19:00")
home_system.schedule_task(lambda: thermostat.set_temperature(21), "22:00")

# Get specific device status
print(home_system.get_device_status("LIGHT001"))
```

### 4. **Expected Output**

```
Device: Living Room Light, Type: Light, Status: On, Brightness: 50
Device: Main Thermostat, Type: Thermostat, Status: Off, Temperature: 25°C, Mode: Cooling
Device: Front Door Camera, Type: Security Camera, Status: Off, Quality: 1080p, Recording: No
Device: Front Door Lock, Type: Smart Lock, Status: Off, Lock Status: Locked

Scheduled tasks:
- Turn on Living Room Light at 19:00
- Set Thermostat temperature to 21°C at 22:00
```

### 5. **Constraints:**
- The system should allow for easy addition and removal of devices.
- Devices should be controllable and their status should be up-to-date.
- Scheduled tasks should be executed at the correct time without user intervention.
- Each device type should have its specific set of controllable attributes (e.g., brightness for lights, temperature for thermostats).

---

This **Smart Home Automation System** allows users to control and monitor various smart devices in their home. It provides real-time control and scheduling capabilities, making it a versatile solution for home automation.