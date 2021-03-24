# Chase Hospitals
This is a gui-based system which provide best solution for future's computerised intractions plus this Software uses offline Text to Speech software so that handicapped patients will have greater ease of access while running this software. All the data's are stored in tabular form in a relational database i.e. MySQL database with tkinter based gui written in Python.

Talking about the features of this Hospital Management System, this project is aimed for a completely computerised management of our fictional hospital CHASE HOSPITALS. A patient can register themselves, view their details and modify their details as well. They can see the Details of Doctors, view the Services offered by the hospital. They can also make an appointment to a particular doctor

## Developers:
This project is created by **Udit Pati** and **Robin Vats** as part of their 12th CS project 2020 - 2021, under the able and very helpful guidance of PGT Mr. ML Meena Sir, Kendriya Vidyalaya No. 2 Delhi Cantt. 
All codes in this file is completely written by Udit Pati and Robin Vats only. All images and icons used under CC license

## Screenshots
- **Main Window**     

![main window](https://github.com/LuciferChase/chase_hospitals/blob/master/Data/Images/Screenshots/main_window.jpg)

- **Registration**     

![registration](https://github.com/LuciferChase/chase_hospitals/blob/master/Data/Images/Screenshots/registration.jpg)

- **Patient Details (after searching)**     

![patient details](https://github.com/LuciferChase/chase_hospitals/blob/master/Data/Images/Screenshots/patient_details.jpg)

- **Modify Details (after verifying**     

![modify details](https://github.com/LuciferChase/chase_hospitals/blob/master/Data/Images/Screenshots/modify_details.jpg)

- **Appointment**      

![appointment](https://github.com/LuciferChase/chase_hospitals/blob/master/Data/Images/Screenshots/appointment.jpg)

- **About Us**     

![about us](https://github.com/LuciferChase/chase_hospitals/blob/master/Data/Images/Screenshots/about.jpg)

## Installation
Clone or fork this project. Make sure to download the complete project. See dependencies to install additional libraries.

## Default Data:
Database Used 	- 	chase_hospitals      
Tables Used 	-	patient_details, doctor_details, appointment, rooms

- Table 1: (patient_details)
```
+-----------+-------------------------+-----+--------+------------+------------+-------------+
| pid       | name                    | age | gender | contact    | address    | blood_group |
+-----------+-------------------------+-----+--------+------------+------------+-------------+
| 313570101 | Mr. Udit Pati           |  17 | M      | 8375054875 | Delhi      | O+          |
| 313570102 | Mr. Robin Vats          |  17 | M      | 7567563156 | Delhi      | O+          |
| 313570103 | Mr. Rahul Roy           |  18 | M      | 8345671848 | Mumbai     | A+          |
| 313570104 | Mr. Aditya Manas        |  16 | M      | 7534586798 | Jaipur     | B+          |
+-----------+-------------------------+-----+--------+------------+------------+-------------+
```

- Table 2: (doctor_details)
```
+-----+-------------------+-----+------------+------------------+--------------------------------------------+
| did | name              | age | contact    | specialisation   | qualification                              |
+-----+-------------------+-----+------------+------------------+--------------------------------------------+
| 101 | Dr. Rakesh Sharma |  35 | 7658424743 | Dentist          | Bachelor of Dental Surgery                 |
| 102 | Dr. Patiiii       |  67 | 9427365092 | Ayurveda         | Bachelor of Ayurvedic Medicine and Surgery |
| 103 | Dr. P.K Sharma    |  40 | 7248743423 | Medicine         | MBBS Ph.D                                  |
| 104 | Dr. K.P Kohli     |  44 | 8493883433 | Cardiologists    | MBBS M.Phil M.D                            |
| 105 | Dr. S.K Patil     |  44 | 7839478943 | Surgeon          | MBBS                                       |
| 106 | Dr. D.K Tripathi  |  46 | 9173826433 | Orthopaedics     | MBBS                                       |
| 107 | Dr. Rahul Poonia  |  30 | 9485757483 | Cardiologists    | MBBS                                       |
| 108 | Dr. Unnikrishnan  |  23 | 9876346843 | Osteopathologist | MBBS DO Phd M.D                            |
| 109 | Dr. Batra         |  32 | 9874758843 | Radiologist      | MBBS DMSC MMSc                             |
| 110 | Dr. Manoj         |  27 | 9546738843 | General Surgeon  | MBBS MD(Res) MS MSurg                      |
| 111 | Dr. Yadav         |  39 | 9578495743 | Medicine         | MM MMed                                    |
| 112 | Dr. Pal           |  34 | 9856784938 | Medicine         | MBBS MMedSc MM                             |
| 113 | Dr. Shukla        |  45 | 8756493756 | General Surgeon  | MBBS MPhil MChir                           |
| 114 | Dr. Singh         |  37 | 8564789456 | Ayurveda         | Bachelor of Ayurvedic Medicine             |
| 115 | Dr. Amit          |  38 | 8452378940 | Cardiologists    | MBBS MPhil MD D.O                          |
| 116 | Dr. Shyam         |  41 | 7456328975 | Neurologists     | MBBS MPhil DO                              |
+-----+-------------------+-----+------------+------------------+--------------------------------------------+
```

## Dependencies:
```
1. python 3.x
2. mysql.connector	-	connect with MySQL database
3. easygui		-	gui
4. Pillow		-	display pictures
5. pyttsx3		-	text-to-speech 
6. pypiwin32		-	pyttsx3 may not run without this
7. pyglet		-	display different font style
8. Evogria.otf		-	font style
9. Images
```

## System Used:
```
+----+-------------------------------------------+
| No | System_Used                               |
+----+-------------------------------------------+
|  1 | Processor - AMD A6 RADEON 5 Core 2.50 GHz |
|  2 | Operating System - Windows 10             |
|  3 | RAM - 8 GB                                |
|  4 | Python - 3.8.2                            |
|  5 | mysql-connector-python 8.0.20             |
+----+-------------------------------------------+
```





