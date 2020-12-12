# SecondTech (Exam Project)

Web catalog for used electronic devices

# Login and Register functionality
1. Extended Django User via OneToOne relation
2. Each user has full CRUD on their account/profile
3. Each user has the ability to edit their profile and change their password
4. Forms for login and register
5. Form validation is included (First name, Last name, Phone number)
6. The admin has full CRUD on each account/profile

# Public part for all users
1. Landing page
2. About Us page
3. All devices page

# Private part for authenticated users
1. Profile Details page
2. Device Details page
3. Create device page


# Admin part
1. Built-in Django Admin Page
2. Custom Admin page which contains all objects created by the users (Devices, Accounts, Profiles, Comments)

# Devices
1. Each device has: Title, Image, Description, Type, Brand, Model, Storage capcity, RAM, CPU Speed, OS, Price, Color
2. Each device has form validations for: CPU Speed, Price, RAM, Storage Capacity

# Comment
1. Each comment has: Submitter, Text, Receiver, Creation Date
2. Each comment has form validations for: Text

# User
1. Each user has: Username, First name, Last name, Password, E-mail, Profile picture, Location, Phone Number
2. Each user has form validations for: First name, Last name, Phone number

# More information about the project
1. Each authenticated user has the ability to create/edit/delete devices
2. Each device has a details page with all of it's aditional info
3. Each profile has details page with all of it's additional info
4. Each authenticated user has the ability to leave comments under every profile
5. Comment creators have full CRUD on their comments
6. Comment receivers have the ability to delete comments on their profile
7. The admin has full CRUD on each comment

# Additional features and functionality
1. PostgreSQL
2. Custom CSS and Bootstrap
3. Extended Django User
4. Form validations
5. Search bar

