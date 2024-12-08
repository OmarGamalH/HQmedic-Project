# HQmedic Project

## Description
HQmedic is a web application designed to simplify the process of finding doctors, communicating with them, and accessing medical advice written by healthcare professionals. The application serves two main types of users: patients and doctors. It allows patients to find doctors categorized by specialty, communicate privately with doctors, and view useful medical advice. Doctors can provide medical advice, interact with patients, and manage requests from patients. 

## Distinctiveness and Complexity
The HQmedic platform stands out for its dual-user functionality, allowing both patients and doctors to have distinct, yet interconnected roles. The complexity lies in the dynamic interaction between users: a patient can request to consult with a doctor, who can either confirm or reject the request. This system is further complicated by the feature that allows doctors to also register as patients with the same account, enabling them to experience the platform from both perspectives. The application leverages Django's robust backend capabilities, including authentication, forms, and models to manage user interactions, while providing a responsive and user-friendly front-end experience built with JavaScript, HTML, and CSS. Furthermore, the application integrates real-time elements such as updating the doctor's likes and providing private messaging functionality between patients and doctors, adding another layer of interactivity and complexity to the user experience.

## Project Folder Contents:
The project is structured into two main folders, **first_app** and **HQmedic**, which together handle the functionality and configuration of the web application.

- **first_app** contains:
  - **static** folder: includes CSS and JavaScript files.
  - **migrations** folder: holds database migration files.
  - **profile_images** folder: stores the default user profile image and individual user profile pictures.
  - **templates** folder: contains HTML files, in a subfolder **first_app** housing various templates like `advices.html`, `index.html`, `layout.html`, `login.html`, `pending.html`, `profile.html`, and others.
  - **`__init__.py`**: a Django-specific file for initialization.
  - **admin.py**: handles settings for the Django admin panel.
  - **apps.py**: another configuration file for Django applications.
  - **backends.py**: implements user authentication logic.
  - **decorators.py**: defines the decorators used in the views.
  - **models.py**: contains the database models for users, doctors, patients, and other entities.
  - **tests.py**: includes unit tests for the project functionality.
  - **urls.py**: defines the URLs and links them to corresponding views.
  - **views.py**: contains backend logic and handles HTTP requests, form rendering, and user interaction.

- **HQmedic** folder: includes Django settings files such as `__pycache__.py`, `__init__.py`, `asgi.py`, `settings.py`, `urls.py`, and `wsgi.py`.

- **db.sqlite3**: the SQLite database storing all project data.

- **manage.py**: the script used to perform various Django management tasks like running the server, migrating databases, creating admin users, and using the shell.

## How to Run the Application:
To run the application locally, simply execute the following command in the terminal: **py manage.py runserver** , This will start the Django development server and serve the application.


## Patient Experience:
- The patient can **view all doctors** categorized by their specialties.
- The patient can **like a doctor**, and HQmedic will rank doctors based on the number of likes they receive, showcasing the most popular and highly-rated doctors.
- The patient can **request to add a doctor** (private consultation) and interact with the doctor via private messages, ensuring that only the doctor and the patient can see the conversation.
- The patient has access to an **advice page**, where they can view medical tips and advice shared by doctors from different specialties.
- The patient can **login as a doctor** too, since a single email can be associated with both patient and doctor profiles.
- Each patient has a **profile page** where they can update their photo and has personal information such as gender, email, phone number, and name.
- The patient also has a **pending page**, which displays the doctors they have requested and are waiting for confirmation from.

## Doctor Experience:
- Doctors who register on the platform will appear in the patient directory, making it easy for patients to find them.
- Doctors can **write medical advice** for patients and other healthcare professionals to view.
- Doctors have access to a **pending page**, where they can manage requests from patients by either confirming or rejecting them.
- Only patients whose requests have been confirmed can communicate privately with the doctor.
- Each doctor has a **profile page** showcasing their personal details, written advice, and more.
- Doctors can also register as patients, allowing them to use the platform as both a healthcare provider and a user.

## Project Details:
- The application is built using the **Django framework** (Python) for the backend and **JavaScript**, **HTML**, and **CSS** for the frontend.
- The project uses **Django models** to manage database records for users, doctors, patients, and other data entities which is basically using sqlite for query the database.
- **Backend authentication** is employed to handle user login, registration.
- The frontend utilizes JavaScript APIs to enable dynamic features like adding doctors, confirming requests, and providing users’ profile images.
- The web application is **responsive**, ensuring a smooth user experience on mobile devices.

## video link:
a [video link](https://youtu.be/JLnQNy-zmX0) shows implementation of the project.

