from pages import RegistrationPage

def test_student_registration_fluent():
    first_name = 'Yasha'
    last_name = 'Kramarenko'
    email = 'yashaka@gmail.com'
    mobile = '1234567890'

    (RegistrationPage()
     .open()
     .fill_first_name(first_name)
     .fill_last_name(last_name)
     .fill_email(email)
     .fill_gender()
     .fill_mobile(mobile)
     .submit()
     .should_have_registered(
         ('Student Name', f'{first_name} {last_name}'),
         ('Student Email', email),
         ('Mobile', mobile)
     ))