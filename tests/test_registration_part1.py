from pages.registration_page import RegistrationPage


def test_student_registration_mid_level():
    (RegistrationPage()
     .open()
     .fill_first_name('Yasha')
     .fill_last_name('Kramarenko')
     .fill_email('yashaka@gmail.com')
     .select_gender('Male')
     .fill_mobile('1234567890')
     .fill_date_of_birth(1990, 'January', 1)
     .add_subjects('Computer Science', 'Maths')
     .select_hobbies('Sports', 'Reading')
     .upload_picture('test.jpg')
     .fill_address('Some Address 123')
     .select_state('NCR')
     .select_city('Delhi')
     .submit()
     .should_have_registered(
         StudentName='Yasha Kramarenko',
         StudentEmail='yashaka@gmail.com',
         Gender='Male',
         Mobile='1234567890'
     ))