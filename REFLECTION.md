# Reflection - Student Course Registration System

## 1. What was the hardest part of this project?

The hardest part was implementing the registration system while ensuring that students cannot register for the same course twice and that courses do not exceed their capacity.

---

## 2. Which classes did you create and why?

- Person: Used as a base class to avoid repeating common attributes.
- Student: Represents a student and inherits from Person.
- Course: Represents a course with its details.
- SchoolSystem: Handles all system operations like adding students, courses, and registrations.

---

## 3. How does your registration logic prevent duplicate registrations?

Before adding a new registration, the system checks if a student-course pair already exists in the registrations list. If it does, the system prevents duplicate entry.

---

## 4. How does your system check if a course is full?

The system counts how many students are already registered for a course. If the number reaches the course capacity, new registrations are blocked.

---

## 5. What bugs did you face and how did you fix them?

I faced issues with incorrect data handling between students and courses, especially when linking them in registrations. I fixed this by using consistent IDs and validating data before storing it.

---

## 6. Which part would you improve if I had more time?

I would improve the user interface and add features like deleting students, updating course details, and improving data storage using a database instead of JSON files.


This work was done a few hours before submission, it might be done in a rush or not be to certain standards. But I tried my best.