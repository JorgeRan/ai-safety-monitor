# AI Vision-Based Safety Monitor
An embedded real-time computer vision system that detects safety risks using an ESP32 + camera.  
Designed for industrial or lab environments where PPE compliance, unsafe posture, or dangerous proximity must be monitored continuously.

## 🚀 Features
- Real-time object detection (YOLO-based, on-device optimized)
- Safety rule engine (e.g., missing gloves, no lab coat, no safety glasses)
- Fall / collapse detection using pose estimation
- Automatic audio/visual alerts through speaker + LEDs
- Logs events to SD card (timestamped JPEG + JSON metadata)
- WiFi dashboard for reviewing alerts in real time

## 🧠 System Architecture
Camera → ESP32 (inference + rule engine) → SD card logger
↘ WiFi → Web Dashboard
↘ Speaker/LEDs → Alerts

## 🛠️ Tech Stack
- **ESP32-CAM**
- **MicroPython / C++ (ESP-IDF)**
- **TinyYOLO / MobileNet-SSD** optimized for microcontrollers
- **Web dashboard**: HTML/CSS/JS
- **SD card logging**
- **Optional cloud sync** (Firebase)

## 📂 Repository Structure
```
prosthetic-arm/
├── firmware
│   ├── main.ino
├── models
├── src
├── tests
├── web-dashboard
├── public
├── api
├── js
├── data
├── sample-images
├── annotations
```
## 🧪 How It Works
1. Camera captures frame → model runs locally
2. Detected classes converted to “rules”
3. If a violation is triggered → buzzer, LEDs, and log entry
4. Dashboard polls ESP32 endpoint for updates

## ▶️ Demo (Planned)
- “Missing PPE detection” test scenario
- “Fall detection using pose angles”
- Real-time alerting demo with video

## 📌 Roadmap
- [ ] Add helmet detection
- [ ] BLE broadcast for mobile alerts
- [ ] Cloud alert dashboard

