# IoT Garage Door Simulator

A **desktop-based IoT Garage Door simulation** built with Python and Tkinter.  
This project allows you to **simulate opening and closing a garage door** and logs all actions with timestamps.

---

## 🔥 Features

- Open/Close the garage door using GUI buttons  
- Real-time **Door Status** indicator (Red = Closed, Green = Open)  
- **Action Log** displaying timestamps of all operations  
- Fully desktop-based simulation (no hardware required)  
- Easy to extend with multiple doors or networked IoT simulation  

---

## 🛠 Tools & Technologies

- **Programming Language:** Python 3.x  
- **GUI Library:** Tkinter  
- **OS:** Linux, Windows, macOS  

---

## ⚙️ Setup Instructions
 1. Clone the repository

git clone https://github.com/marthanjoel/IoT-garage-door.git
cd IoT-garage-door
2. Install Python 3
Make sure Python 3.x is installed:
python3 --version
3. Run the simulation
python3 app.py
You will see a window with:
Door Status
Open Door / Close Door buttons
Action Log
Click the buttons to simulate opening and closing the garage door.
<img width="1366" height="768" alt="Screenshot from 2025-09-10 10-45-21" src="https://github.com/user-attachments/assets/07d124e9-3080-4266-8125-da10932abb03" />

<img width="1366" height="768" alt="Screenshot from 2025-09-10 10-45-58" src="https://github.com/user-attachments/assets/a2a36e03-b39a-4283-b2fe-6eff8ac68359" />

--

##🧩 How It Works##
The door state is stored in a variable (Open or Closed).

Clicking Open or Close updates the state.

The status label changes color:

Red = Closed

Green = Open

Every action is logged with a timestamp in the action log.


--
##💡 Future Improvements##
Add multiple garage doors simulation

Integrate a Flask web dashboard for remote control

Add real-time notifications or IoT integration


Add keyboard shortcuts to control the door
